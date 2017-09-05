import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
#import the module created in the qtdesigner
from dialog1 import Ui_InitalDialog
from dialog2 import Ui_Dialog2
from dialog3 import Ui_Dialog3

#Dropdown of AppWindow1
AW11="In welchen Firmen hattest du dein Projekt (Branche/OEM/Tier1,2,3)?"
AW12="Wer ist der Kunde?"
showTrigger = 1 #Show AppWindow1
#Flagcheckbox
flag2 = [0] * 4
print flag2


#Main window
class AppWindow1(QDialog):
    def __init__(self, parent=None):
        super(AppWindow1, self).__init__()
        #Set up interface from designer
        self.ui = Ui_InitalDialog()
        self.ui.setupUi(self)
        #Connect to buttons
        self.ui.PushButton1ok.clicked.connect(self.decision)
        #load GUI
        self.show()
        
    def decision(self):
        text_decision = str(self.ui.comboBox1.currentText())
        if text_decision == AW11:
            self.hide()
            self.QDialog = AppWindow2(self)
        elif text_decision == AW12:
            self.hide()
            self.QDialog = AppWindow3(self)
        else:        
            return 
#Window if the following response is selected by AppWindow1
#In welchen Firmen hattest du dein Projekt (Branche/OEM/Tier1,2,3)?
class AppWindow2(QDialog):
    def __init__(self, parent=None):
        super(AppWindow2, self).__init__()
        #Set up interface from designer
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        #Connect to buttons
        self.ui.PlotButton2.clicked.connect(self.plot2)
        self.ui.backButton2.clicked.connect(self.back2)
        #load GUI
        self.show()

    def plot2(self):
        print "Here comes the plot2"
        #get flags if checked self.ui.checkBox31.isChecked() = True
        if self.ui.checkBox21.isChecked():
               print "checked21"
               if self.ui.checkBox22.isChecked():
                   print "checked22"
                   if self.ui.checkBox23.isChecked():
                       print "checked23"
                       if self.ui.checkBox24.isChecked():
                           print "checked24"
        else:
            return
        #Question
        text_flag2 = str(self.ui.comboBox2.currentText())

    def back2(self):
        self.hide()
        self.QDialog = AppWindow1(self)
    
#Window if the following response is selected by AppWindow1
#Wer ist der Kunde?
class AppWindow3(QDialog):
    def __init__(self, parent=None):
        super(AppWindow3, self).__init__()
        #Set up interface from designer
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        #Connect to buttons
        self.ui.PlotButton3.clicked.connect(self.plot3)
        self.ui.backButton3.clicked.connect(self.back3)
        #load GUI
        self.show()

    def plot3(self):
        print "Here comes the plot3"
        #get flags if checked self.ui.checkBox31.isChecked() = True
         if self.ui.checkBox31.isChecked():
               print "checked31"
               if self.ui.checkBox32.isChecked():
                   print "checked32"
                   if self.ui.checkBox33.isChecked():
                       print "checked33"
                       if self.ui.checkBox34.isChecked():
                           print "checked34"
        else:
            return
        #Question
        text_flag3 = str(self.ui.comboBox3.currentText())

    def back3(self):
        self.hide()
        self.QDialog = AppWindow1(self)

def main():
    app = QApplication(sys.argv)
    main = AppWindow1()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()