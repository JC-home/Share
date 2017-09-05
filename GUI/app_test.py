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
flag2 = [0] * 5
flag3 = [0] * 5


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
        #Question
        text_flag2 = str(self.ui.comboBox2.currentText())
        print text_flag2

        #get flags if checked self.ui.checkBox31.isChecked() = True
        #starts with a zero [0 x x x x]
        if self.ui.checkBox21.isChecked():
            flag2[1] = 1
        else:
            flag2[1] = 0
        if self.ui.checkBox22.isChecked():
            flag2[2] = 1
        else:
            flag2[2] = 0
        if self.ui.checkBox23.isChecked():
            flag2[3] = 1  
        else:
            flag2[3] = 0         
        if self.ui.checkBox24.isChecked():
            flag2[4] = 1
        else:
            flag2[4] = 0
        print flag2

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

        #Question
        text_flag3 = str(self.ui.comboBox3.currentText())
        print text_flag3

        #get flags if checked self.ui.checkBox31.isChecked() = True
        #starts with a zero [0 x x x x]
        if self.ui.checkBox31.isChecked():
            flag3[1] = 1
        else:
            flag3[1] = 0
        if self.ui.checkBox32.isChecked():
            flag3[2] = 1
        else:
            flag3[2] = 0
        if self.ui.checkBox33.isChecked():
            flag3[3] = 1  
        else:
            flag3[3] = 0         
        if self.ui.checkBox34.isChecked():
            flag3[4] = 1
        else:
            flag3[4] = 0
        print flag3

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