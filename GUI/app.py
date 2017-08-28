import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from dialog1 import Ui_InitalDialog

class App(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_InitalDialog()
            self.ui.setupUI(self)
            self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())