
#! /usr/bin/python
import sys
from transmitter_ui_demo import *
import sys, traceback, Ice
sys.path.append("..")	#This is to add the main application path to search path as the Ice interface object is described there

import data
class  window(Ui_MainWindow):# The Ui_Main Window is a model of userinterface which is imported by above command..
	def setupUi(self,QMainWindow):
		self.filelist=[]
		self.BuddyNameString=" "
		Ui_MainWindow.setupUi(self,QMainWindow)
		self.SelectFileButton.clicked.connect(self.getFile)	
		self.SetUserNameButton.clicked.connect(self.setUserName)
		self.SendButton.clicked.connect(self.sendFile)
		self.VerfiyBuddyButton.clicked.connect(self.varifyBuddyName)
		self.StatusDisplay.setTextColor(QtGui.QColor(255,0,0))
		self.StatusDisplay.append("Welcome to p2psend")
		self.Configfilepath="config"
		self.setupConnection()
	def setupConnection(self):#This will setup the connection with the receiver.Current the reciever have to be started before the sender for working.
		self.ConnectionStatus = 0
		self.ic = None
		if self.BuddyNameString != " ":
			try:
			    self.ac = Ice.initialize(sys.argv)
			    self.base =self.ac.stringToProxy(self.BuddyNameString+":default -p 10000")
			    self.SendObject= data.sendfilePrx.checkedCast(self.base)
			    self.StatusDisplay.append("Connected to the Buddy")
			    if not self.SendObject:

			    	raise RuntimeError("Invalid proxy")

			except:
				self.StatusDisplay.append("Wrong Buddy Name or Buddy is not up")
				traceback.print_exc()
				self.ConnectionStatus = 1
		else :
			self.StatusDisplay.append("Enter your Buddy Name")

	def getFile(self):	 # This will get the file to send 
		filname=QtGui.QFileDialog.getOpenFileName(None,'Open file', '/home/')
		self.filelist.append(filname)
		self.FileName.setText(filname)
	def setUserName(self): # This will get the username and will save it into a filenameself.
		self.StatusDisplay.setTextColor(QtGui.QColor(0,255,0))
		self.StatusDisplay.append("UsernameSaved::"+str(self.UserName.text()))
		fil =open(self.Configfilepath,'w')
		fil.write("Usename#"+str(self.UserName.text()))
		fil.close()
	def varifyBuddyName(self):
		self.BuddyNameString=str(self.BuddyName.text())
		self.setupConnection()

	def sendFile(self):
		file=open(self.filelist[-1],'r')
		data=file.read()
		self.SendObject.sendstringfile(str(data),"hello")
if  __name__=='__main__': 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
