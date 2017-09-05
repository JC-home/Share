import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
#This code just displays one GUI element 



#import the module created in the qtdesigner
from dialog1 import Ui_InitalDialog
from dialog2 import Ui_Dialog2
from dialog3 import Ui_Dialog3

class AppWindow1(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_InitalDialog()
        self.ui.setupUi(self)
        self.show()

class AppWindow2(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        self.show()
class AppWindow3(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        self.show()

#show the window on PC
app = QApplication(sys.argv)
#switch case to define which window shall be opend
w = AppWindow1()
#w = AppWindow2()
#w = AppWindow3()
#End of switch case
w.show()
sys.exit(app.exec_())
#End of showing window on PC