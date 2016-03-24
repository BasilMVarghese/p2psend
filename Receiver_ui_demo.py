# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Receiver_UI.ui'
#
# Created: Thu Mar 24 21:20:22 2016
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
        MainWindow.resize(685, 299)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.UserIp = QtGui.QLabel(self.centralwidget)
        self.UserIp.setObjectName(_fromUtf8("UserIp"))
        self.horizontalLayout_4.addWidget(self.UserIp)
        self.UserName = QtGui.QLineEdit(self.centralwidget)
        self.UserName.setObjectName(_fromUtf8("UserName"))
        self.horizontalLayout_4.addWidget(self.UserName)
        self.SetUserNameButton = QtGui.QPushButton(self.centralwidget)
        self.SetUserNameButton.setObjectName(_fromUtf8("SetUserNameButton"))
        self.horizontalLayout_4.addWidget(self.SetUserNameButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ServerUpRadio = QtGui.QRadioButton(self.centralwidget)
        self.ServerUpRadio.setObjectName(_fromUtf8("ServerUpRadio"))
        self.horizontalLayout_3.addWidget(self.ServerUpRadio)
        self.ServerDownRadio = QtGui.QRadioButton(self.centralwidget)
        self.ServerDownRadio.setObjectName(_fromUtf8("ServerDownRadio"))
        self.horizontalLayout_3.addWidget(self.ServerDownRadio)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Status = QtGui.QTextEdit(self.centralwidget)
        self.Status.setObjectName(_fromUtf8("Status"))
        self.horizontalLayout_2.addWidget(self.Status)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.SaveFile = QtGui.QPushButton(self.centralwidget)
        self.SaveFile.setObjectName(_fromUtf8("SaveFile"))
        self.horizontalLayout.addWidget(self.SaveFile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.UserIp.setText(_translate("MainWindow", "TextLabel", None))
        self.SetUserNameButton.setText(_translate("MainWindow", "Set User Name", None))
        self.ServerUpRadio.setText(_translate("MainWindow", "Server Down", None))
        self.ServerDownRadio.setText(_translate("MainWindow", "Serve Up", None))
        self.SaveFile.setText(_translate("MainWindow", "Save", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

