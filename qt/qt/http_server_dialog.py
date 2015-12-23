# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'http_server_dialog.ui'
#
# Created: Tue Dec 15 13:22:52 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_http_server_dialog(object):
    def setupUi(self, http_server_dialog):
        http_server_dialog.setObjectName("http_server_dialog")
        http_server_dialog.resize(400, 300)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(http_server_dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_Image_2 = QtWidgets.QLabel(http_server_dialog)
        self.label_Image_2.setObjectName("label_Image_2")
        self.horizontalLayout_2.addWidget(self.label_Image_2)
        self.label_2 = QtWidgets.QLabel(http_server_dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(http_server_dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(http_server_dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.http_server_port = QtWidgets.QSpinBox(http_server_dialog)
        self.http_server_port.setObjectName("http_server_port")
        self.gridLayout.addWidget(self.http_server_port, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(http_server_dialog)
        self.pushButton.setMaximumSize(QtCore.QSize(130, 63))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.http_server_directory = QtWidgets.QLineEdit(http_server_dialog)
        self.http_server_directory.setClearButtonEnabled(False)
        self.http_server_directory.setObjectName("http_server_directory")
        self.gridLayout.addWidget(self.http_server_directory, 0, 2, 1, 1)
        self.open_path_Button = QtWidgets.QToolButton(http_server_dialog)
        self.open_path_Button.setObjectName("open_path_Button")
        self.gridLayout.addWidget(self.open_path_Button, 0, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.retranslateUi(http_server_dialog)
        self.open_path_Button.triggered['QAction*'].connect(self.http_server_directory.paste)
        QtCore.QMetaObject.connectSlotsByName(http_server_dialog)

    def retranslateUi(self, http_server_dialog):
        _translate = QtCore.QCoreApplication.translate
        http_server_dialog.setWindowTitle(_translate("http_server_dialog", "Dialog"))
        self.label_Image_2.setText(_translate("http_server_dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("http_server_dialog", "Monocafe Connections manager\n"
" manage you connections"))
        self.label_3.setText(_translate("http_server_dialog", "Directory"))
        self.label_4.setText(_translate("http_server_dialog", "Port"))
        self.pushButton.setText(_translate("http_server_dialog", "PushButton"))
        self.http_server_directory.setText(_translate("http_server_dialog", "/tmp"))
        self.open_path_Button.setText(_translate("http_server_dialog", "..."))

