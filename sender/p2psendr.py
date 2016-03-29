
import sys
from transmitter_ui_demo import *
import sys, traceback, Ice
sys.path.append("..")	#This is to add the main application path to search path as the Ice interface object is described there

import data
class  window(Ui_MainWindow):# The Ui_Main Window is a model of userinterface which is imported by above command..
	def setupUi(self,QMainWindow):
		self.filelist=[]	##Will contain the list of file names to send
		self
		Ui_MainWindow.setupUi(self,QMainWindow)
		self.SelectFileButton.clicked.connect(self.getFile)	
		self.SetUserNameButton.clicked.connect(self.setUserName)
		self.StatusDisplay.setTextColor(QtGui.QColor(255,0,0))
		self.StatusDisplay.append("Welcome to p2psend")
		#self.StatusDisplay.setAlignment(Qt.AlignLeft)
		self.Configfilepath="config"
		self.setupConnection()
	def setupConnection(self):
		self.ConnectionStatus = 0
		self.ic = None
		try:
		    self.ac = Ice.initialize(sys.argv)
		    self.base =self.ac.stringToProxy("SimplePrinter:default -p 10000")
		    self.SendObject= data.sendfilePrx.checkedCast(self.base)
		    self.SendObject.sendstringfile("hello","motherfuckers")
		    if not self.SendObject:
		        raise RuntimeError("Invalid proxy")
	            
		except: 
		    traceback.print_exc()
		    self.ConnectionStatus = 1
		 
		#if ac:
		#    # Clean up
		#    try:
		#        ac.destroy()
		#    except:
		#        traceback.print_exc()
		#       status = 1	
	def getFile(self):	 
		filname=QtGui.QFileDialog.getOpenFileName(None,'Open file', '/home/',"Image files(*.jpg *.gif)")
		#print "read"
		self.filelist.append(filname)
		self.FileName.setText(filname)
	def setUserName(self): 
		# This will get the username and will save it into a filenameself.
		self.StatusDisplay.setTextColor(QtGui.QColor(0,255,0))
		self.StatusDisplay.append("UsernameSaved::"+str(self.UserName.text()))
		
		fil =open(self.Configfilepath,'w')
		fil.write("Usename#"+str(self.UserName.text()))
		fil.close()
	def varifyBuddyName(self):
		pass
	def sendFile(self):
		pass




if  __name__=='__main__': 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
