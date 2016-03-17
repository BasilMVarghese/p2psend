import sys
from PyQt4	import	QtCore, QtGui
from Receiver import Ui_MainWindow

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.ServerIdentityEnter,QtCore.SIGNAL("clicked()"), self.SeverNameSave)
        QtCore.QObject.connect(self.ui.SendButton,QtCore.SIGNAL("clicked()"), self.SendFile)
    def ServerName:	
  	#This will help user enter the server name(Name of  computer to which the file have to be send)
  	def SendFile :
  	#This will initialise the object proxy and all other stuffs and send the file
  	def SetSendStatus :
  	#This will put the send status to the text field
app = QtGui.QApplication(sys.argv)
myapp = StartQT4()
myapp.show()
sys.exit(app.exec_())

