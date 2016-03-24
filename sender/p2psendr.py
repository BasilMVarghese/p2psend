
import sys
from transmitter_ui_demo import *
class  window(Ui_MainWindow):
	def setupUi(self,QMainWindow):
		self.filelist=[]	##Will contain the list of file names to send
		self
		Ui_MainWindow.setupUi(self,QMainWindow)
		self.SelectFileButton.clicked.connect(self.getFile)	
		self.SetUserNameButton.clicked.connect(self.setUserName)
		#self.StatusDisplay.setAlignment(Qt.AlignLeft)
		self.Configfilepath="config"
	def getFile(self):
		filname=QtGui.QFileDialog.getOpenFileName(None,'Open file', '/home/',"Image files(*.jpg *.gif)")
		#print "read"
		self.filelist.append(filname)
		self.FileName.setText(filname)
	def setUserName(self): 
		# This will get the username and will save it into a filename.
		self.StatusDisplay.setText("UsernameSaved::"+str(self.UserName.text()))
		
		fil =open(self.Configfilepath,'w')
		fil.write("Usename#"+str(self.UserName.text()))
		fil.close()
	def varifyBuddyName(self):
	def sendFile(self):




if __name__=='__main__': 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
