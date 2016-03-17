# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Receiver.ui'
#
# Created: Thu Mar 17 15:51:40 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(733, 218)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Receivedstatus = QtGui.QTextEdit(self.centralwidget)
        self.Receivedstatus.setGeometry(QtCore.QRect(10, 10, 711, 41))
        self.Receivedstatus.setObjectName(_fromUtf8("Receivedstatus"))
        self.SaveDirectory = QtGui.QTextEdit(self.centralwidget)
        self.SaveDirectory.setGeometry(QtCore.QRect(10, 70, 471, 51))
        self.SaveDirectory.setObjectName(_fromUtf8("SaveDirectory"))
        self.SaveButton = QtGui.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(520, 70, 181, 51))
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))
        self.ServerStatusOnline = QtGui.QCheckBox(self.centralwidget)
        self.ServerStatusOnline.setGeometry(QtCore.QRect(10, 130, 97, 22))
        self.ServerStatusOnline.setObjectName(_fromUtf8("ServerStatusOnline"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.SaveButton.setText(_translate("MainWindow", "Save", None))
        self.ServerStatusOnline.setText(_translate("MainWindow", "Server Up", None))

