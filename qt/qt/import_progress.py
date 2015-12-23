# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_progress.ui'
#
# Created: Tue Dec 15 13:23:12 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_import_progress(object):
    def setupUi(self, import_progress):
        import_progress.setObjectName("import_progress")
        import_progress.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(import_progress)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Image = QtWidgets.QLabel(import_progress)
        self.label_Image.setObjectName("label_Image")
        self.horizontalLayout.addWidget(self.label_Image)
        self.label = QtWidgets.QLabel(import_progress)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(import_progress)
        self.groupBox.setObjectName("groupBox")
        self.tree_scroll = QtWidgets.QScrollArea(self.groupBox)
        self.tree_scroll.setGeometry(QtCore.QRect(0, 0, 382, 105))
        self.tree_scroll.setMinimumSize(QtCore.QSize(382, 105))
        self.tree_scroll.setWidgetResizable(True)
        self.tree_scroll.setObjectName("tree_scroll")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 388, 103))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.import_result = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.import_result.setMinimumSize(QtCore.QSize(370, 85))
        self.import_result.setObjectName("import_result")
        self.horizontalLayout_3.addWidget(self.import_result)
        self.tree_scroll.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ok_button6 = QtWidgets.QPushButton(import_progress)
        self.ok_button6.setObjectName("ok_button6")
        self.horizontalLayout_2.addWidget(self.ok_button6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(import_progress)
        self.ok_button6.clicked.connect(import_progress.accept)
        QtCore.QMetaObject.connectSlotsByName(import_progress)

    def retranslateUi(self, import_progress):
        _translate = QtCore.QCoreApplication.translate
        import_progress.setWindowTitle(_translate("import_progress", "Dialog"))
        self.label_Image.setText(_translate("import_progress", "<html><head/><body><p><img src=\":/Image/images/Monocute_web.png\"/></p></body></html>"))
        self.label.setText(_translate("import_progress", "<html><head/><body><p><span style=\" font-weight:600;\">Monocafe Connections manager</span></p><p>Importing Connections</p></body></html>"))
        self.groupBox.setTitle(_translate("import_progress", "Importing"))
        self.ok_button6.setText(_translate("import_progress", "Aceptar"))

