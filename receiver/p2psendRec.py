import sys, traceback, Ice
from Receiver_ui_demo import *
sys.path.append("..")
import data
class sendfileI(data.sendfile):	#This is the interface object
	def __init__(self,UiObject):#WE are passing the qtext also to display the status
		self.UiObject=UiObject
	def sendstringfile(self,data,filename,current=None):##
		self.UiObject.string=data
		self.UiObject.filename=filename
		self.UiObject.Status.append("File "+filename+ "Receieved")

		#print data
		#self.qtext.append("File "+filename+" Receieved")

class window(Ui_MainWindow):
	def setupUi(self,QMainWindow):
		Ui_MainWindow.setupUi(self,QMainWindow)
		self.SetUserNameButton.clicked.connect(self.setUserName)
		self.SaveFile.clicked.connect(self.saveFile)
		self.UserNameString=" "
		self.setUpConnection()
	def setUpConnection(self):
		self.Connetionstatus = 0
		self.ic = None
		self.string=" "
		self.filename=" "
		if self.UserNameString!=" ":
			try:
			    self.ic = Ice.initialize(sys.argv)
			    self.adapter = self.ic.createObjectAdapterWithEndpoints(self.UserNameString+"Adapter", "default -p 10000")
			    self.object = sendfileI(self)
			    self.adapter.add(self.object,self.ic.stringToIdentity(self.UserNameString))
			    self.adapter.activate()
			    #self.ic.waitForShutdown() 	
			except:
			    traceback.print_exc()
			    status = 1
		else:
			self.Status.append("Set The UserName first")
 	def saveFile(self):
 		print self.string
 		if self.string!=" " and self.filename!=" ":
 			self.SavingPosition=QtGui.QFileDialog.getSaveFileName(None,"Save File","/home/")
 			fileObject=open(self.SavingPosition,'w')
 			fileObject.write(self.string)
 			fileObject.close()
 		else:
 			self.Status.append("No file received")
	def setUserName(self):
		self.UserNameString=str(self.UserName.text())
		self.Status.append("New UserName:: "+self.UserNameString)
		self.setUpConnection()


if __name__=='__main__': 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
