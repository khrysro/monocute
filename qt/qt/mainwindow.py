# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Dec 23 19:43:03 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 443)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 221, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 219, 149))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.treeView = QtWidgets.QTreeView(self.scrollAreaWidgetContents_3)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 221, 141))
        self.treeView.setObjectName("treeView")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.user_entry = QtWidgets.QLineEdit(self.groupBox_2)
        self.user_entry.setObjectName("user_entry")
        self.gridLayout.addWidget(self.user_entry, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.connect_button = QtWidgets.QPushButton(self.groupBox_2)
        self.connect_button.setObjectName("connect_button")
        self.gridLayout.addWidget(self.connect_button, 0, 1, 1, 1)
        self.description_entry = QtWidgets.QLineEdit(self.groupBox_2)
        self.description_entry.setObjectName("description_entry")
        self.gridLayout.addWidget(self.description_entry, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.options_entry = QtWidgets.QLineEdit(self.groupBox_2)
        self.options_entry.setObjectName("options_entry")
        self.gridLayout.addWidget(self.options_entry, 4, 1, 1, 1)
        self.host_entry = QtWidgets.QLineEdit(self.groupBox_2)
        self.host_entry.setObjectName("host_entry")
        self.gridLayout.addWidget(self.host_entry, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.port_entry = QtWidgets.QLineEdit(self.groupBox_2)
        self.port_entry.setObjectName("port_entry")
        self.gridLayout.addWidget(self.port_entry, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.pwd_entry = QtWidgets.QLineEdit(self.groupBox_2)
        self.pwd_entry.setObjectName("pwd_entry")
        self.gridLayout.addWidget(self.pwd_entry, 6, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tabWidget.addTab(self.tab_16, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.cluster_entry = QtWidgets.QLineEdit(self.centralWidget)
        self.cluster_entry.setObjectName("cluster_entry")
        self.verticalLayout_2.addWidget(self.cluster_entry)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 481, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuConnections = QtWidgets.QMenu(self.menuBar)
        self.menuConnections.setObjectName("menuConnections")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionFeedbask = QtWidgets.QAction(MainWindow)
        self.actionFeedbask.setWhatsThis("")
        self.actionFeedbask.setObjectName("actionFeedbask")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPreference = QtWidgets.QAction(MainWindow)
        self.actionPreference.setObjectName("actionPreference")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport_Html = QtWidgets.QAction(MainWindow)
        self.actionExport_Html.setObjectName("actionExport_Html")
        self.actionExport_CSV = QtWidgets.QAction(MainWindow)
        self.actionExport_CSV.setObjectName("actionExport_CSV")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionConnections = QtWidgets.QAction(MainWindow)
        self.actionConnections.setCheckable(True)
        self.actionConnections.setObjectName("actionConnections")
        self.actionCluster = QtWidgets.QAction(MainWindow)
        self.actionCluster.setCheckable(True)
        self.actionCluster.setObjectName("actionCluster")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionHTTP_Server = QtWidgets.QAction(MainWindow)
        self.actionHTTP_Server.setObjectName("actionHTTP_Server")
        self.menuFile.addAction(self.actionPreference)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport_Html)
        self.menuFile.addAction(self.actionExport_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionConnections)
        self.menuView.addAction(self.actionCluster)
        self.menuConnections.addAction(self.actionConnect)
        self.menuConnections.addAction(self.actionAdd)
        self.menuConnections.addAction(self.actionDelete)
        self.menuConnections.addAction(self.actionEdit)
        self.menuTools.addAction(self.actionHome)
        self.menuTools.addAction(self.actionHTTP_Server)
        self.menuHelp.addAction(self.actionFeedbask)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuConnections.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Connections"))
        self.groupBox_2.setTitle(_translate("MainWindow", "SERVER"))
        self.label_4.setText(_translate("MainWindow", "Options"))
        self.label_2.setText(_translate("MainWindow", "Hostname/IP Address"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.label_5.setText(_translate("MainWindow", "Description"))
        self.label_3.setText(_translate("MainWindow", "Port"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuConnections.setTitle(_translate("MainWindow", "Connections"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionFeedbask.setText(_translate("MainWindow", "Feedback"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPreference.setText(_translate("MainWindow", "Preference"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport_Html.setText(_translate("MainWindow", "Export HTML"))
        self.actionExport_CSV.setText(_translate("MainWindow", "Export CSV"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionConnections.setText(_translate("MainWindow", "Connections"))
        self.actionCluster.setText(_translate("MainWindow", "Cluster"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionHTTP_Server.setText(_translate("MainWindow", "HTTP Server"))

