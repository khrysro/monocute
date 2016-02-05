#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class embeddedTerminal(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self._processes = []
        self.resize(800, 600)
        self.terminal = QWidget(self)
        self.terminal.resize(800, 600)

        layout = QVBoxLayout(self)

        layout.addWidget(self.terminal)

        ID = str(int(self.terminal.winId()))
        print(ID)
        self._start_process(
            'xterm',
            ['-into',  ID,'-s',
             ]
        )
        button = QPushButton('List files')
        layout.addWidget(button)
        button.clicked.connect(self._list_files)

    def _start_process(self, program, kwargs):
        self.child = QProcess()
        self._processes.append(self.child)
        #  self.child.execute(program, options)
        self.child.start(program, kwargs)

    def _list_files(self):
        self._start_process(
            'tee', ['send-keys', '-t', 'my_session:0', 'ls', 'Enter'])

    def closeEvent(self, event):
        self.child.terminate()
        self.child.waitForFinished()
        event.accept()

    def terminate(self):
        program = "tee"
        options = []
        options.extend(["send-keys", "-t", "session1:0"])
        options.extend(["killall tee"])
        options.extend(["Enter"])
        self.start_process(program, options)
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = embeddedTerminal()
    main.show()
    sys.exit(app.exec_())



__author__ = 'khrys'
