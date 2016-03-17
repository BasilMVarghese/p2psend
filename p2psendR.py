import sys
from PyQt4	import	QtCore, QtGui
from Receiver import Ui_MainWindow

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.SaveButton,QtCore.SIGNAL("clicked()"), self.savefile)
    def savefile :
    # This will varify the conditions and save the file into a user input directory
    	if transfer_status=True	#True if file is recieved
    		try:
    		 	UserInSaveName=self.ui.SaveDirectory.getText() #The directory and name to which the file should be saved 
    			OutputFile=open(savename,'w')	
    			OutputFile.write(TransferedFile)
    			OutputFile.close()
    			self.ui.Receivedstatus.setText("File Saved")
    		 except:
    		 	Print "There is no such directory \n"
    	else 
    		print "No file Recieved"
    	