# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_preferences.ui'
#
# Created: Tue Dec 15 13:21:50 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_preferences(object):
    def setupUi(self, dialog_preferences):
        dialog_preferences.setObjectName("dialog_preferences")
        dialog_preferences.resize(427, 527)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dialog_preferences)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Imagen = QtWidgets.QLabel(dialog_preferences)
        self.label_Imagen.setProperty("pix", QtGui.QPixmap("images/Monocute_web.png"))
        self.label_Imagen.setObjectName("label_Imagen")
        self.horizontalLayout_3.addWidget(self.label_Imagen)
        self.label = QtWidgets.QLabel(dialog_preferences)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabs = QtWidgets.QTabWidget(dialog_preferences)
        self.tabs.setObjectName("tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider)
        self.fontComboBox = QtWidgets.QFontComboBox(self.groupBox)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fontComboBox)
        self.font_colorbutton = QtWidgets.QPushButton(self.groupBox)
        self.font_colorbutton.setText("")
        self.font_colorbutton.setObjectName("font_colorbutton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.font_colorbutton)
        self.horizontalLayout_5.addLayout(self.formLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.bg_colorbutton = QtWidgets.QPushButton(self.groupBox_2)
        self.bg_colorbutton.setText("")
        self.bg_colorbutton.setObjectName("bg_colorbutton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bg_colorbutton)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_2)
        self.bgimage_filechooserbutton = QtWidgets.QLineEdit(self.groupBox_2)
        self.bgimage_filechooserbutton.setAutoFillBackground(False)
        self.bgimage_filechooserbutton.setDragEnabled(False)
        self.bgimage_filechooserbutton.setClearButtonEnabled(True)
        self.bgimage_filechooserbutton.setObjectName("bgimage_filechooserbutton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bgimage_filechooserbutton)
        self.toolButton_11 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_11.setObjectName("toolButton_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toolButton_11)
        self.horizontalLayout_6.addLayout(self.formLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.tabs.addTab(self.tab, "")
        self.tab_SSH = QtWidgets.QWidget()
        self.tab_SSH.setObjectName("tab_SSH")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_SSH)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_SSH)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.ssh_client_entry = QtWidgets.QLineEdit(self.groupBox_6)
        self.ssh_client_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.ssh_client_entry.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.ssh_client_entry.setObjectName("ssh_client_entry")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ssh_client_entry)
        self.toolButton = QtWidgets.QToolButton(self.groupBox_6)
        self.toolButton.setObjectName("toolButton")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton)
        self.horizontalLayout_9.addLayout(self.formLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_SSH)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.ssh_default_options_entry = QtWidgets.QLineEdit(self.groupBox_5)
        self.ssh_default_options_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.ssh_default_options_entry.setObjectName("ssh_default_options_entry")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ssh_default_options_entry)
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_2.setObjectName("toolButton_2")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_2)
        self.horizontalLayout_10.addLayout(self.formLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tabs.addTab(self.tab_SSH, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.ftp_client_entry = QtWidgets.QLineEdit(self.groupBox_7)
        self.ftp_client_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.ftp_client_entry.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.ftp_client_entry.setObjectName("ftp_client_entry")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ftp_client_entry)
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton_3.setObjectName("toolButton_3")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_3)
        self.horizontalLayout_11.addLayout(self.formLayout_7)
        self.verticalLayout_7.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.ftp_default_options_entry = QtWidgets.QLineEdit(self.groupBox_8)
        self.ftp_default_options_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.ftp_default_options_entry.setObjectName("ftp_default_options_entry")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ftp_default_options_entry)
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox_8)
        self.toolButton_4.setObjectName("toolButton_4")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_4)
        self.horizontalLayout_12.addLayout(self.formLayout_8)
        self.verticalLayout_7.addWidget(self.groupBox_8)
        self.horizontalLayout_13.addLayout(self.verticalLayout_7)
        self.tabs.addTab(self.tab_6, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.telnet_client_entry = QtWidgets.QLineEdit(self.groupBox_9)
        self.telnet_client_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.telnet_client_entry.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.telnet_client_entry.setObjectName("telnet_client_entry")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.telnet_client_entry)
        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox_9)
        self.toolButton_5.setObjectName("toolButton_5")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_5)
        self.horizontalLayout_14.addLayout(self.formLayout_9)
        self.verticalLayout_8.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.telnet_default_options_entry = QtWidgets.QLineEdit(self.groupBox_10)
        self.telnet_default_options_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.telnet_default_options_entry.setObjectName("telnet_default_options_entry")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.telnet_default_options_entry)
        self.toolButton_6 = QtWidgets.QToolButton(self.groupBox_10)
        self.toolButton_6.setObjectName("toolButton_6")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_6)
        self.horizontalLayout_15.addLayout(self.formLayout_10)
        self.verticalLayout_8.addWidget(self.groupBox_10)
        self.horizontalLayout_16.addLayout(self.verticalLayout_8)
        self.tabs.addTab(self.tab_4, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.formLayout_11 = QtWidgets.QFormLayout()
        self.formLayout_11.setObjectName("formLayout_11")
        self.rdp_client_entry = QtWidgets.QLineEdit(self.groupBox_11)
        self.rdp_client_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.rdp_client_entry.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.rdp_client_entry.setObjectName("rdp_client_entry")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rdp_client_entry)
        self.toolButton_7 = QtWidgets.QToolButton(self.groupBox_11)
        self.toolButton_7.setObjectName("toolButton_7")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_7)
        self.horizontalLayout_17.addLayout(self.formLayout_11)
        self.verticalLayout_9.addWidget(self.groupBox_11)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.formLayout_12 = QtWidgets.QFormLayout()
        self.formLayout_12.setObjectName("formLayout_12")
        self.rdp_default_options_entry = QtWidgets.QLineEdit(self.groupBox_12)
        self.rdp_default_options_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.rdp_default_options_entry.setObjectName("rdp_default_options_entry")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rdp_default_options_entry)
        self.toolButton_8 = QtWidgets.QToolButton(self.groupBox_12)
        self.toolButton_8.setObjectName("toolButton_8")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_8)
        self.horizontalLayout_18.addLayout(self.formLayout_12)
        self.verticalLayout_9.addWidget(self.groupBox_12)
        self.horizontalLayout_19.addLayout(self.verticalLayout_9)
        self.tabs.addTab(self.tab_7, "")
        self.VNC = QtWidgets.QWidget()
        self.VNC.setObjectName("VNC")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.VNC)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox_13 = QtWidgets.QGroupBox(self.VNC)
        self.groupBox_13.setObjectName("groupBox_13")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.formLayout_13 = QtWidgets.QFormLayout()
        self.formLayout_13.setObjectName("formLayout_13")
        self.vnc_client_entry = QtWidgets.QLineEdit(self.groupBox_13)
        self.vnc_client_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.vnc_client_entry.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.vnc_client_entry.setObjectName("vnc_client_entry")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vnc_client_entry)
        self.toolButton_9 = QtWidgets.QToolButton(self.groupBox_13)
        self.toolButton_9.setObjectName("toolButton_9")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_9)
        self.horizontalLayout_20.addLayout(self.formLayout_13)
        self.verticalLayout_10.addWidget(self.groupBox_13)
        self.groupBox_14 = QtWidgets.QGroupBox(self.VNC)
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.formLayout_14 = QtWidgets.QFormLayout()
        self.formLayout_14.setObjectName("formLayout_14")
        self.vnc_default_options_entry = QtWidgets.QLineEdit(self.groupBox_14)
        self.vnc_default_options_entry.setMinimumSize(QtCore.QSize(250, 0))
        self.vnc_default_options_entry.setObjectName("vnc_default_options_entry")
        self.formLayout_14.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vnc_default_options_entry)
        self.toolButton_10 = QtWidgets.QToolButton(self.groupBox_14)
        self.toolButton_10.setObjectName("toolButton_10")
        self.formLayout_14.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton_10)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout_14.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.horizontalLayout_21.addLayout(self.formLayout_14)
        self.verticalLayout_10.addWidget(self.groupBox_14)
        self.horizontalLayout_22.addLayout(self.verticalLayout_10)
        self.tabs.addTab(self.VNC, "")
        self.verticalLayout.addWidget(self.tabs)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(dialog_preferences)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dialog_preferences)

    def retranslateUi(self, dialog_preferences):
        _translate = QtCore.QCoreApplication.translate
        dialog_preferences.setWindowTitle(_translate("dialog_preferences", "Dialog"))
        self.label_Imagen.setText(_translate("dialog_preferences", "<html><head/><body><p><img src=\":/Image/images/Monocute_web.png\"/></p></body></html>"))
        self.label.setText(_translate("dialog_preferences", "<html><head/><body><p><span style=\" font-weight:600;\">Monocute Connections Manager</span></p><p>Preferences</p></body></html>"))
        self.groupBox.setTitle(_translate("dialog_preferences", "Console"))
        self.label_2.setText(_translate("dialog_preferences", "Font Style"))
        self.label_4.setText(_translate("dialog_preferences", "Font Color"))
        self.label_5.setText(_translate("dialog_preferences", "Buffer Size                         "))
        self.groupBox_2.setTitle(_translate("dialog_preferences", "Background"))
        self.label_3.setText(_translate("dialog_preferences", "Color"))
        self.label_6.setText(_translate("dialog_preferences", "Image"))
        self.label_7.setText(_translate("dialog_preferences", "Desaturation:"))
        self.label_8.setText(_translate("dialog_preferences", "Background Transparent"))
        self.label_9.setText(_translate("dialog_preferences", "Select-by-word Characters"))
        self.toolButton_11.setText(_translate("dialog_preferences", "..."))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("dialog_preferences", "General"))
        self.groupBox_6.setTitle(_translate("dialog_preferences", "Client"))
        self.toolButton.setText(_translate("dialog_preferences", "..."))
        self.groupBox_5.setTitle(_translate("dialog_preferences", "Default Options"))
        self.toolButton_2.setText(_translate("dialog_preferences", "..."))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_SSH), _translate("dialog_preferences", "SSH"))
        self.groupBox_7.setTitle(_translate("dialog_preferences", "Client"))
        self.toolButton_3.setText(_translate("dialog_preferences", "..."))
        self.groupBox_8.setTitle(_translate("dialog_preferences", "Default Options"))
        self.toolButton_4.setText(_translate("dialog_preferences", "..."))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_6), _translate("dialog_preferences", "FTP"))
        self.groupBox_9.setTitle(_translate("dialog_preferences", "Client"))
        self.toolButton_5.setText(_translate("dialog_preferences", "..."))
        self.groupBox_10.setTitle(_translate("dialog_preferences", "Default Options"))
        self.toolButton_6.setText(_translate("dialog_preferences", "..."))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_4), _translate("dialog_preferences", "Telnet"))
        self.groupBox_11.setTitle(_translate("dialog_preferences", "Client"))
        self.toolButton_7.setText(_translate("dialog_preferences", "..."))
        self.groupBox_12.setTitle(_translate("dialog_preferences", "Default Options"))
        self.toolButton_8.setText(_translate("dialog_preferences", "..."))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_7), _translate("dialog_preferences", "RDP"))
        self.groupBox_13.setTitle(_translate("dialog_preferences", "Client"))
        self.toolButton_9.setText(_translate("dialog_preferences", "..."))
        self.groupBox_14.setTitle(_translate("dialog_preferences", "Default Options"))
        self.toolButton_10.setText(_translate("dialog_preferences", "..."))
        self.checkBox_3.setText(_translate("dialog_preferences", "Embedded"))
        self.tabs.setTabText(self.tabs.indexOf(self.VNC), _translate("dialog_preferences", "VNC"))
