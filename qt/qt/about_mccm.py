# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_mccm.ui'
#
# Created: Tue Dec 15 13:21:15 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_about_mccm(object):
    def setupUi(self, about_mccm):
        about_mccm.setObjectName("about_mccm")
        about_mccm.resize(392, 284)
        about_mccm.setMinimumSize(QtCore.QSize(392, 284))
        about_mccm.setMaximumSize(QtCore.QSize(392, 284))
        self.gridLayout_2 = QtWidgets.QGridLayout(about_mccm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_imagen = QtWidgets.QLabel(about_mccm)
        self.label_imagen.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imagen.setObjectName("label_imagen")
        self.gridLayout.addWidget(self.label_imagen, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(about_mccm)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(about_mccm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(about_mccm)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(about_mccm)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(about_mccm)
        QtCore.QMetaObject.connectSlotsByName(about_mccm)

    def retranslateUi(self, about_mccm):
        _translate = QtCore.QCoreApplication.translate
        about_mccm.setWindowTitle(_translate("about_mccm", "Dialog"))
        self.label_imagen.setText(_translate("about_mccm", "<html><head/><body><p><img src=\":/Image/images/Monocute_web.png\"/></p></body></html>"))
        self.label_3.setText(_translate("about_mccm", "Este programa viene SIN NINGUNA GARANTIA"))
        self.label.setText(_translate("about_mccm", "Monocute Connections Manager"))
        self.label_2.setText(_translate("about_mccm", "port a Qt de monocaffe connection manager"))
        self.label_4.setText(_translate("about_mccm", "Version 0.0.1"))

