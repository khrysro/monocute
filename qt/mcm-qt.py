# - coding: utf-8 -
#

'''
Main Script for mccm

 '''

import PyQt5
import logging
import os
import sys
import pexpect
import webbrowser
import gettext
import locale
#pygtk.require("2.0")

from common.connections import *
from common.export import *
from common.utils import *
import common.constants

from qt.qt.mainwindow import *
from qt.widgets_2 import *


class Mccmqt(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dao = Dao()
        self.connections = self.dao.read_xml()
        menubar = QToolBar("mytoolbar")
        self.addToolBar(menubar)


    def about_event(self, widget):
        about = self.widgets['about']
        about.connect("response", lambda d, r: d.hide())
        about.run()

    def add_event(self, widget):
        id = self.get_last_id()
        dlg = AddConnectionDialog(id, list(self.connections.keys()), groups(self.connections), types(self.connections))
        dlg.run()
        if dlg.response == QMessageBox.AcceptRole:
            cx = dlg.new_connection
            self.connections[cx.alias] = cx
            self.draw_tree()

    def clear_cluster_event(self, widget):
        entry = self.widgets['cluster_entry']
        entry.set_text("")

    def close_tab_event(self, accel_group, window, keyval=None, modifier=None, unk=None):
        terminals = self.widgets['terminals']
        index = terminals.get_current_page()
        terminals.remove_page(index)
        if terminals.get_n_pages() <= 0:
            terminals.hide()
        return True

    def cluster_backspace(self, widget):
        """Call this event when the backspace key is pressed on the entry widget"""
        return self.cluster_send_key('\b')

    def cluster_event(self, widget):
        """Call this event when any key is pressed on the entry widget"""
        command = widget.get_text()
        widget.set_text("")
        if len(command) < 1:
            return False
        return self.cluster_send_key(command)

    def cluster_intro_event(self, widget):
        """Call this event when the enter key is pressed on the entry widget"""
        return self.cluster_send_key('\n')

    def cluster_send_key(self, key):
        """This method is in charge of sending the keys to the selected
        terminals from the entry widget"""
        # Now get the notebook and all the tabs
        cluster_tabs = {}
        terminals = self.widgets['terminals']
        pages = terminals.get_n_pages()
        for i in range(pages):
            scroll = terminals.get_nth_page(i)
            checkbox = terminals.get_tab_label(scroll)
            if checkbox.get_active():
                term = scroll.get_child()
                cluster_tabs[i] = term

        for term in list(cluster_tabs.values()):
            term.feed_child(key)
        return True

    def connect_event(self, widget, path=None, vew_column=None):
        alias = None
        name = gtk.Buildable.get_name(widget)

        if name == 'connect_button' or name == 'mb_connect' or name == 'connections_tree':
            alias = self.get_tree_selection()
        else:
            alias = widget.props.name

        # OMG Someone broke this on GTK 2.17
        #if widget.props.name == 'connect_button' or widget.props.name == 'mb_connect' or widget.props.name == 'connections_tree':
        #    alias = self.get_tree_selection()
        #else:
        #    alias = widget.props.name

        self.do_connect(self.connections[alias])

    def delete_event(self, widget):
        alias = self.get_tree_selection()
        dlg = UtilityDialogs()
        response = dlg.show_question_dialog(constants.deleting_connection_warning % alias, constants.are_you_sure)
        if response == gtk.RESPONSE_OK:
            del self.connections[alias]
            self.draw_tree()

    def die_term_event(self, scroll, terminals):
        term = scroll.get_child()
        raw_text = term.get_text(self.die_term_callback, True)
        err_msg = raw_text[0].strip().split('\n')
        #print err_msg
        #terminals = self.widgets['terminals']
        index = terminals.get_current_page()
        terminals.remove_page(index)
        if terminals.get_n_pages() <= 0:
            terminals.hide()
        return True

    def die_term_callback(self, term, col, row, data):
        ''' We don't do anything with any of this since we don't have any use for it'''
        return True

    def do_connect(self, connection):
        '''Here I create a ScrolledWindow, attach a VteTerminal widget and all this gets attached
        to a new page on a NoteBook widget. Instead of using a label, I use a custom CheckButton widget
        since the default CheckButton widget covered the whole tab, making it very difficult to switch
        tabs by clicking on them.'''
        # Check for VNC Connections
        if connection:
            if connection.get_type() == "VNC":
                conf = MccmConfig()
                client, options, embedded = conf.get_vnc_conf()
                if embedded:
                    return self.vnc_connect(connection)

        # Not VNC continue
        scroll = QScrollArea()#ScrolledWindow()
        # By setting the POLICY_AUTOMATIC, the ScrollWindow resizes itself when hidding the TreeView
        scroll.setVerticalScrollBarPolicy(None) #set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        v = pexpect.spawn('bash -i') #vte.Terminal()
        #scroll.add(v)
        terminals = self.widgets['terminals']
        label = None
        menu_label = None
        if connection == None:
            label = MccmCheckbox('localhost')
            menu_label = QLabel('localhost')
        else:
            label = MccmCheckbox(connection.alias)
            label.set_tooltip_text(connection.description)
            menu_label = QLabel(connection.alias)
        self.set_window_title(label.get_title())
        index = terminals.append_page_menu(scroll, label, menu_label)
        terminals.set_tab_reorderable(scroll, True)

        # Send the scroll widget to the event so the notebook know which child to close
        v.connect("child-exited", lambda term: self.die_term_event(scroll, terminals))
        v.connect("button-press-event", self.do_popup_console_menu)
        v.connect("key-press-event", self.terminal_key_event)
        pid = v.fork_command()
        if connection != None:
            v.feed_child(connection.gtk_cmd())
        self.assign_key_binding(constants.tabs_switch_keys % (index + 1), self.switch_tab)
        self.assign_key_binding(constants.terminal_copy_keys, self.do_copy)
        self.assign_key_binding(constants.terminal_paste_keys, self.do_paste)
        terminals.show_all()
        terminals.set_current_page(index)
        self.draw_consoles()
        v.grab_focus()

    def do_localhost(self, accel_group, window=None, keyval=None, modifier=None):
        self.do_connect(None)
        return True

    def do_popup_console_menu(self, widget, event):
        '''Draw a Menu ready to be inserted in a vteterminal widget'''
        if event.button == 1:
            return False
        elif event.button == 3:
            menu = QMenu()
            copy = QAction(constants.copy)
            paste = QAction(constants.paste)
            search = QAction(constants.google_search)
            title = QAction(constants.set_title)
            menu.append(copy)
            menu.append(paste)
            menu.append(search)
            menu.append(QMenu.addSeparator())
            menu.append(title)
            copy.connect('activate', self.do_copy)
            paste.connect('activate', self.do_paste)
            search.connect('activate', self.do_search)
            title.connect('activate', self.do_set_title)
            menu.show_all()
            menu.popup(None, None, None, 3, event.time)
            return True
        else:
            return False

    def do_popup_connections_menu(self, widget, event):
        print("Click!")
        return False
    def draw_connection_widgets(self, alias):
        if alias == None:
            return
        connection = None
        try:
            connection = self.connections[alias]
        except KeyError:
            return
        label = self.widgets['cx_type']
        label.set_label("<b>%s</b>" % connection.get_type())
        label = self.widgets['alias_label']
        label.set_label("<b>%s</b>" % alias)
        self.draw_entry('user_entry', connection.user)
        self.draw_entry('host_entry', connection.host)
        self.draw_entry('port_entry', connection.port)
        self.draw_entry('password_entry', connection.password)
        self.draw_entry('options_entry', connection.options)
        self.draw_entry('description_entry', connection.description)

    def draw_tree(self):
        tree = self.widgets['cx_tree']
        if len(tree.get_columns()) == 0:
            self.draw_column(tree, "Alias", 0)
        tree_store = QStandardItemModel(str, str)
        tree.set_model(tree_store)

        groups = set()
        for cx in list(self.connections.values()):
            groups.add(cx.group)

        for grp in groups:
            grp_node = tree_store.append(None, [grp, None])
            for cx in list(self.connections.values()):
                if grp == cx.group:
                    tree_store.append(grp_node, [cx.alias, None])

    def edit_event(self, widget):
        id = self.get_last_id()
        alias = self.get_tree_selection()
        dlg = AddConnectionDialog(id, list(self.connections.keys()), groups(self.connections), types(self.connections), self.connections[alias])
        dlg.run()
        if dlg.response == QMessageBox.AcceptRole:
            cx = dlg.new_connection
            del self.connections[alias]
            self.connections[cx.alias] = cx
            self.draw_tree()

    def events(self):
        events = {
            'on_main_mcm_destroy': self.quit_event,
            'on_connect_button_clicked': self.connect_event,
            'on_arrow_button_clicked': self.hide_unhide_tree,
            # Menu Items
            'on_mb_about_activate': self.about_event,
            'on_mb_help_activate': self.help_event,
            'on_mb_feedback_activate': self.feedback_event,
            'on_mb_preferences_activate': self.preferences_event,
            'on_mb_save_activate': self.save_event,
            'on_mb_import_activate': self.import_csv_event,
            'on_mb_export_html_activate': self.export_html_event,
            'on_mb_export_csv_activate': self.export_csv_event,
            'on_mb_quit_activate': self.quit_event,
            'on_mb_add_activate': self.add_event,
            'on_mb_delete_activate': self.delete_event,
            'on_mb_connect_activate': self.connect_event,
            'on_mb_cluster_toggled': self.hide_unhide_cluster_box,
            'on_mb_view_tree_toggled': self.hide_unhide_tree,
            'on_mb_tips_toggled': self.hide_unhide_tips,
            'on_mb_update_tips_activate': self.update_tips,
            #'on_mb_http_server_activate': self.http_server,
            'on_mb_edit_activate': self.edit_event,
            # Status Icon Items
            'on_sib_quit_activate': self.quit_event,
            'on_sib_preferences_activate': self.preferences_event,
            'on_sib_add_activate': self.add_event,
            'on_sib_quit_activate': self.quit_event,
            'on_status_icon_menu_deactivate': self.on_status_icon_deactivate,
            'on_sib_home_activate': self.do_localhost,
            # Tree signals
            'on_connections_tree_row_activated': self.connect_event,
            'on_home_button_clicked': self.do_localhost,
            'on_connections_tree_cursor_changed': self.on_tree_item_clicked,
            'on_connections_tree_button_press_event': self.tree_submenu_event,
            # Entries Signales
            'on_user_entry_activate': self.update_connection,
            'on_user_entry_changed': self.entry_changed_event,
            'on_host_entry_activate': self.update_connection,
            'on_host_entry_changed': self.entry_changed_event,
            'on_port_entry_activate': self.update_connection,
            'on_port_entry_changed': self.entry_changed_event,
            'on_options_entry_activate': self.update_connection,
            'on_options_entry_changed': self.entry_changed_event,
            'on_description_entry_activate': self.update_connection,
            'on_description_entry_changed': self.entry_changed_event,
            'on_pwd_entry_activate': self.update_connection,
            'on_pwd_entry_changed': self.entry_changed_event,
            #Cluster Signals
            'on_cluster_entry_changed': self.cluster_event,
            'on_cluster_entry_activate': self.cluster_intro_event,
            'on_cluster_entry_backspace': self.cluster_backspace,
            # Notebook Signals
            #'on_terminals_change_current_page': self.switch_tab_event,
            #'on_terminals_select_page': self.switch_tab_event,
            'on_terminals_switch_page': self.switch_tab_event}
        return events

    def export_csv_event(self, widget):
        dlg = FileSelectDialog(FileSelectDialog.CSV)
        dlg.run()
        if dlg.response == QMessageBox.AcceptRole:
            _csv = ExportCsv(dlg.get_filename(), self.connections)
            idlg = UtilityDialogs()
            idlg.show_info_dialog(constants.export_csv, constants.saved_file % dlg.get_filename())

    def export_html_event(self, widget):
        dlg = FileSelectDialog(FileSelectDialog.HTML)
        dlg.run()
        if dlg.response == QMessageBox.AcceptRole:
            _html = Html(dlg.get_filename(), constants.version, self.connections)
            _html.export()
            idlg = UtilityDialogs()
            idlg.show_info_dialog(constants.export_html, constants.saved_file % dlg.get_filename())

    def f10_event(self, accel_group, window=None, keyval=None, modifier=None):
        return False

    def get_last_id(self):
        return get_last_id(self.connections)

    def get_tree_selection(self, tree=None):
        '''Gets the alias of the connection currently selected on the tree'''
        if tree == None:
            tree = self.widgets['cx_tree']
        cursor = tree.get_selection()
        model = tree.get_model()
        (model, iter) = cursor.get_selected()
        if iter == None:
            return None
        alias = model.get_value(iter, 0)
        return alias

    def feedback_event(self, widget):
        webbrowser.open_new_tab(constants.google_feedback_form_url)

    def help_event(self, widget):
        webbrowser.open_new_tab(constants.mcm_help_url)

    def hide_unhide_cluster_box(self, widget):
        cl_box = self.widgets['cluster_entry']
        if widget.active:
            cl_box.show_all()
        else:
            cl_box.hide()

    def hide_unhide_tips(self, widget):
        tips_bar = self.widgets['tips_hbox']
        if widget.active:
            tips_bar.show_all()
        else:
            tips_bar.hide()

    def hide_unhide_tree(self, widget, window=None, key_val=None, modifier=None):
        # I have to define those parameters so the callbacks from the key bindings work
        vbox = self.widgets['vbox3']
        mb = self.widgets['mb_view_tree']
        if vbox.props.visible:
            mb.set_active(False)
            vbox.hide()
        else:
            mb.set_active(True)
            vbox.show_all()
        return True

    def import_csv_event(self, widget):
        dlg = FileSelectDialog(FileSelectDialog.CSV)
        dlg.run()
        cxs = None
        if dlg.response == QMessageBox.AcceptRole:
            _csv = Csv(dlg.uri)
            cxs = _csv.do_import()
            dlg = ImportProgressDialog(cxs, self.connections)
            dlg.run()
            self.connections = dlg.connections
            self.draw_tree()

    def tree_submenu_event(self, widget, event):
        '''Draw a Menu ready to be inserted in tree'''
        if event.button == 1:
            return False
        elif event.button == 3:
            menu = self.widgets['menu2']
            menu.show_all()
            menu.popup(None, None, None, 3, event.time)
            return True
        else:
            return False

    def update_connection(self, widget):
        alias = self.get_tree_selection()
        connection = self.connections[alias]
        wid_name = widget.get_name()
        property = widget.get_text()
        if wid_name == "user_entry":
            connection.user = property
        elif wid_name == "host_entry":
            connection.host = property
        elif wid_name == "port_entry":
            connection.port = property
        elif wid_name == "options_entry":
            connection.options = property
        elif wid_name == "description_entry":
            connection.description = property
        elif wid_name == "pwd_entry":
            connection.password = property
        self.connections[alias] = connection
        self.draw_connection_widgets(self.get_tree_selection())

    def x_event(self, x=None, y=None):
        self.quit_event(x)
        return True

if __name__ == '__main__':
    # Start the logging stuff
    # log_format = "%(asctime)s %(levelname)s: %(message)s"
    # logging.basicConfig(level=logging.INFO, format = log_format)

    app = QApplication(sys.argv)
    mccmqt = Mccmqt()
    mccmqt.show()
    app.exec_()

