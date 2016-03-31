# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transmitter_UI.ui'
#
# Created: Thu Mar 24 22:44:40 2016
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
        MainWindow.resize(681, 231)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.UserName = QtGui.QLineEdit(self.centralwidget)
        self.UserName.setObjectName(_fromUtf8("UserName"))
        self.horizontalLayout_4.addWidget(self.UserName)
        self.SetUserNameButton = QtGui.QPushButton(self.centralwidget)
        self.SetUserNameButton.setObjectName(_fromUtf8("SetUserNameButton"))
        self.horizontalLayout_4.addWidget(self.SetUserNameButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.BuddyIp = QtGui.QLineEdit(self.centralwidget)
        self.BuddyIp.setObjectName(_fromUtf8("BuddyIp"))
        self.horizontalLayout_3.addWidget(self.BuddyIp)
        self.BuddyName = QtGui.QLineEdit(self.centralwidget)
        self.BuddyName.setObjectName(_fromUtf8("BuddyName"))
        self.horizontalLayout_3.addWidget(self.BuddyName)
        self.VerfiyBuddyButton = QtGui.QPushButton(self.centralwidget)
        self.VerfiyBuddyButton.setObjectName(_fromUtf8("VerfiyBuddyButton"))
        self.horizontalLayout_3.addWidget(self.VerfiyBuddyButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.FileName = QtGui.QLineEdit(self.centralwidget)
        self.FileName.setObjectName(_fromUtf8("FileName"))
        self.horizontalLayout.addWidget(self.FileName)
        self.SelectFileButton = QtGui.QPushButton(self.centralwidget)
        self.SelectFileButton.setObjectName(_fromUtf8("SelectFileButton"))
        self.horizontalLayout.addWidget(self.SelectFileButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.SendButton = QtGui.QPushButton(self.centralwidget)
        self.SendButton.setObjectName(_fromUtf8("SendButton"))
        self.horizontalLayout_5.addWidget(self.SendButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.StatusDisplay = QtGui.QTextEdit(self.centralwidget)
        self.StatusDisplay.setObjectName(_fromUtf8("StatusDisplay"))
        self.horizontalLayout_2.addWidget(self.StatusDisplay)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("P2PSEND Transmitter", "P2PSEND Transmitter", None))
        self.SetUserNameButton.setText(_translate("MainWindow", "Set User Name", None))
        self.VerfiyBuddyButton.setText(_translate("MainWindow", "Verify", None))
        self.SelectFileButton.setText(_translate("MainWindow", "Select File ", None))
        self.SendButton.setText(_translate("MainWindow", "Send ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

