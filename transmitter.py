# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transmitter.ui'
#
# Created: Thu Mar 17 01:26:45 2016
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
        MainWindow.resize(726, 219)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ServerIdentityname = QtGui.QTextEdit(self.centralwidget)
        self.ServerIdentityname.setGeometry(QtCore.QRect(20, 10, 411, 41))
        self.ServerIdentityname.setObjectName(_fromUtf8("ServerIdentityname"))
        self.ServerIdentityEnter = QtGui.QPushButton(self.centralwidget)
        self.ServerIdentityEnter.setGeometry(QtCore.QRect(540, 10, 151, 41))
        self.ServerIdentityEnter.setObjectName(_fromUtf8("ServerIdentityEnter"))
        self.SendButton = QtGui.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(540, 60, 151, 41))
        self.SendButton.setObjectName(_fromUtf8("SendButton"))
        self.FileName = QtGui.QTextEdit(self.centralwidget)
        self.FileName.setGeometry(QtCore.QRect(20, 60, 411, 41))
        self.FileName.setObjectName(_fromUtf8("FileName"))
        self.SendStatus = QtGui.QTextEdit(self.centralwidget)
        self.SendStatus.setGeometry(QtCore.QRect(120, 110, 411, 41))
        self.SendStatus.setObjectName(_fromUtf8("SendStatus"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ServerIdentityEnter.setText(_translate("MainWindow", "Enter", None))
        self.SendButton.setText(_translate("MainWindow", "Send", None))

