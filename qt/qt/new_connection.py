# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_connection.ui'
#
# Created: Tue Jan 19 18:49:42 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_connection(object):
    def setupUi(self, new_connection):
        new_connection.setObjectName("new_connection")
        new_connection.resize(400, 363)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(new_connection)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_label = QtWidgets.QLabel(new_connection)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.horizontalLayout.addWidget(self.image_label)
        self.label = QtWidgets.QLabel(new_connection)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(new_connection)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.alias_entry1 = QtWidgets.QLineEdit(new_connection)
        self.alias_entry1.setObjectName("alias_entry1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alias_entry1)
        self.label_4 = QtWidgets.QLabel(new_connection)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.types_combobox = QtWidgets.QComboBox(new_connection)
        self.types_combobox.setObjectName("types_combobox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.types_combobox)
        self.label_5 = QtWidgets.QLabel(new_connection)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.port_entry1 = QtWidgets.QLineEdit(new_connection)
        self.port_entry1.setObjectName("port_entry1")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.port_entry1)
        self.user_entry1 = QtWidgets.QLineEdit(new_connection)
        self.user_entry1.setObjectName("user_entry1")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.user_entry1)
        self.group_combobox = QtWidgets.QComboBox(new_connection)
        self.group_combobox.setEditable(True)
        self.group_combobox.setObjectName("group_combobox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.group_combobox)
        self.label_7 = QtWidgets.QLabel(new_connection)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.host_entry1 = QtWidgets.QLineEdit(new_connection)
        self.host_entry1.setObjectName("host_entry1")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.host_entry1)
        self.label_6 = QtWidgets.QLabel(new_connection)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_9 = QtWidgets.QLabel(new_connection)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_8 = QtWidgets.QLabel(new_connection)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.options_entry1 = QtWidgets.QLineEdit(new_connection)
        self.options_entry1.setObjectName("options_entry1")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.options_entry1)
        self.label_10 = QtWidgets.QLabel(new_connection)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(new_connection)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.description_entry1 = QtWidgets.QLineEdit(new_connection)
        self.description_entry1.setObjectName("description_entry1")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.description_entry1)
        self.password_entry1 = QtWidgets.QLineEdit(new_connection)
        self.password_entry1.setObjectName("password_entry1")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.password_entry1)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(new_connection)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(new_connection)
        QtCore.QMetaObject.connectSlotsByName(new_connection)

    def retranslateUi(self, new_connection):
        _translate = QtCore.QCoreApplication.translate
        new_connection.setWindowTitle(_translate("new_connection", "Dialog"))
        self.label.setText(_translate("new_connection", "<html><head/><body><p><span style=\" font-weight:600;\">Monocafe Connections manager</span></p><p>Add/Edit Connections</p></body></html>"))
        self.label_3.setText(_translate("new_connection", "Alias"))
        self.label_4.setText(_translate("new_connection", "type"))
        self.label_5.setText(_translate("new_connection", "Group"))
        self.label_7.setText(_translate("new_connection", "Username"))
        self.label_6.setText(_translate("new_connection", "Host/IP Address"))
        self.label_9.setText(_translate("new_connection", "Port"))
        self.label_8.setText(_translate("new_connection", "Options"))
        self.label_10.setText(_translate("new_connection", "Description"))
        self.label_11.setText(_translate("new_connection", "Password"))

