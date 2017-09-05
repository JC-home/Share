import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog
from dialog1 import Ui_InitalDialog

class InitalDialog(QDialog):
    def __init__(self):
        super(InitalDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui1 = Ui_InitalDialog()
        self.ui1.setupUi(self)

        # Connect up the buttons.
        self.ui1.pushButton.clicked()
        # Get dropdown menu text.
        self.ui1.comboBox1.curretText()
#show window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InitalDialog()
    sys.exit(app.exec_())

####Simple "show window"
#.app = QApplication(sys.argv)
#window = QDialog()
#ui = Ui_InitalDialog()
#ui.setupUi(window)

#window.show()
#sys.exit(app.exec_())

###New windows from clicked push button
#https://stackoverflow.com/questions/33924369/how-to-open-a-window-with-a-click-of-a-button-from-another-window-using-pyqt