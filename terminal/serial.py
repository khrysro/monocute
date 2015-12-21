import sys
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QAction, qApp, QPushButton

from PyQt5.QtGui import QIcon
import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 2

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.workerThread = SerialRead()
        self.workerThread.mySignal.connect(self.on_change)
        #self.connect(self.workerThread, QtCore.SIGNAL("mysignal(QString)"),self.on_change, QtCore.Qt.QueuedConnection)

    def initUI(self):
        btn1 = QPushButton('Open Serial', self)
        btn1.clicked.connect(self.openSerial)
        btn1.resize(btn1.sizeHint())
        btn1.move(50,50)

        btn2 = QPushButton('Close Serial', self)
        btn2.clicked.connect(self.closeSerial)
        btn2.resize(btn2.sizeHint())
        btn2.move(50,100)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Alt+F4')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.closeEvent)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Motor Driver')

        self.show()

    def openSerial(self):
        ser.open()
        self.workerThread.start()

    def closeSerial(self):
        ser.close()
        self.workerThread.terminate()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class SerialRead(QThread):
    mySignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.data = []

        def run(self):
            while True:
                x = ser.readline()
                # if x != b'\n':
                #   self.data.append(str(x))
                #  else:
                self.mySignal.emit(("mysignal(Qstring)"), (x.decode("utf-8")))
                    # self.data = []



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainUI()
    sys.exit(app.exec_())