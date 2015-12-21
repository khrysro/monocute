# - coding: utf-8 -
#
#
# This file is part of the monocute Connection Manager
#
# monocute Connection Manager is free software: you can redistribute
# it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 2 of the
# License, or (at your option) any later version.
#
# monocute Connection Manager is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with the monocute Connection Manager. If not, see
# <http://www.gnu.org/licenses/>.
#
import sys
#import PyQt5
#import PyQt5.QtGui

from PyQt5.QtWidgets import * #QApplication, QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import self as self

class UtilityDialogs(QDialog):
     def __init__(self, *args, **kwargs):
            super(UtilityDialogs, self).__init__(*args, **kwargs)
            QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.buttonBox)
            self.setLayout(self.layout)

        #self.ui.comboBox_conn_type.activated['QString'].connect(self.connetion_type)

     def show_question_dialog(self, title, message):
        """Display a Warning Dialog and return the response to the caller"""
        dialog = QMessageBox.question(self,QDialog,QMessageBox_StandardButtons_buttons=) #(None, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_OK_CANCEL, title)

        dialog.setText(message) # format_secondary_text(message)
        dialog.addButton(QPushButton('Accept'), QMessageBox.YesRole)
        dialog.addButton(QPushButton('Cancel'), QMessageBox.RejectRole)
        response = dialog.exec_() #dialog.run()

        dialog.destroy()
        return response


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):

        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My app")
        label = QLabel("etiqueta")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        toolbar = QToolBar("my toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("boton dialogo", self)
        button_action.triggered.connect(self.onMyToolbarClick)
        toolbar.addAction(button_action)

    def onMyToolbarClick(self, s):
        print("click", s)
        dlg = UtilityDialogs.show_question_dialog(self, "pregunta","quieres una pregunta?")

        #dlg.exec_()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

