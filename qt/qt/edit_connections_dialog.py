# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_connections_dialog.ui'
#
# Created: Tue Dec 15 13:22:20 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_edit_connections_dialog(object):
    def setupUi(self, edit_connections_dialog):
        edit_connections_dialog.setObjectName("edit_connections_dialog")
        edit_connections_dialog.resize(400, 300)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(edit_connections_dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.label_Image = QtWidgets.QLabel(edit_connections_dialog)
        self.label_Image.setObjectName("label_Image")
        self.horizontalLayout.addWidget(self.label_Image)
        self.label = QtWidgets.QLabel(edit_connections_dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tree_scroll = QtWidgets.QScrollArea(edit_connections_dialog)
        self.tree_scroll.setWidgetResizable(True)
        self.tree_scroll.setObjectName("tree_scroll")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 380, 82))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tree_scroll.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.tree_scroll)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cancel_button = QtWidgets.QPushButton(edit_connections_dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout_2.addWidget(self.cancel_button, 1, 4, 1, 1)
        self.exp_html_button = QtWidgets.QPushButton(edit_connections_dialog)
        self.exp_html_button.setObjectName("exp_html_button")
        self.gridLayout_2.addWidget(self.exp_html_button, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.exp_csv_button = QtWidgets.QPushButton(edit_connections_dialog)
        self.exp_csv_button.setObjectName("exp_csv_button")
        self.gridLayout_2.addWidget(self.exp_csv_button, 1, 2, 1, 1)
        self.save_button = QtWidgets.QPushButton(edit_connections_dialog)
        self.save_button.setObjectName("save_button")
        self.gridLayout_2.addWidget(self.save_button, 1, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.retranslateUi(edit_connections_dialog)
        self.cancel_button.clicked.connect(edit_connections_dialog.close)
        QtCore.QMetaObject.connectSlotsByName(edit_connections_dialog)

    def retranslateUi(self, edit_connections_dialog):
        _translate = QtCore.QCoreApplication.translate
        edit_connections_dialog.setWindowTitle(_translate("edit_connections_dialog", "Dialog"))
        self.label_Image.setText(_translate("edit_connections_dialog", "<html><head/><body><p><img src=\":/Image/images/Monocute_web.png\"/></p></body></html>"))
        self.label.setText(_translate("edit_connections_dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Monocafe Connections manager</span></p><p> manage you connections</p></body></html>"))
        self.cancel_button.setText(_translate("edit_connections_dialog", "Cancel"))
        self.exp_html_button.setText(_translate("edit_connections_dialog", "HTML"))
        self.exp_csv_button.setText(_translate("edit_connections_dialog", "CSV"))
        self.save_button.setText(_translate("edit_connections_dialog", "Save"))

