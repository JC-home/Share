# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(619, 300)
        self.layoutWidget = QtWidgets.QWidget(Dialog3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 581, 230))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox31 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox31.setObjectName("checkBox31")
        self.gridLayout.addWidget(self.checkBox31, 0, 0, 1, 1)
        self.checkBox32 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox32.setObjectName("checkBox32")
        self.gridLayout.addWidget(self.checkBox32, 1, 0, 1, 1)
        self.checkBox33 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox33.setObjectName("checkBox33")
        self.gridLayout.addWidget(self.checkBox33, 2, 0, 1, 1)
        self.checkBox34 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox34.setObjectName("checkBox34")
        self.gridLayout.addWidget(self.checkBox34, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.comboBox3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.setItemText(0, "")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.gridLayout.addWidget(self.comboBox3, 5, 0, 1, 1)
        self.PlotButton3 = QtWidgets.QPushButton(self.layoutWidget)
        self.PlotButton3.setObjectName("PlotButton3")
        self.gridLayout.addWidget(self.PlotButton3, 6, 0, 1, 1)
        self.backButton3 = QtWidgets.QPushButton(self.layoutWidget)
        self.backButton3.setObjectName("backButton3")
        self.gridLayout.addWidget(self.backButton3, 7, 0, 1, 1)

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "Ext Client"))
        self.checkBox31.setText(_translate("Dialog3", "VW (VW, Audi, Porsche)"))
        self.checkBox32.setText(_translate("Dialog3", "BMW (BMW)"))
        self.checkBox33.setText(_translate("Dialog3", "Others (Daimler, Fiat, GM, Evobus, PSA, Honda, OEMs)"))
        self.checkBox34.setText(_translate("Dialog3", "Not Relevant (Hella, Franki Grundbau, internal developement)"))
        self.label.setText(_translate("Dialog3", "Question"))
        self.comboBox3.setItemText(1, _translate("Dialog3", "Entwicklungszeit"))
        self.comboBox3.setItemText(2, _translate("Dialog3", "Schnittstelle"))
        self.comboBox3.setItemText(3, _translate("Dialog3", "Planung"))
        self.comboBox3.setItemText(4, _translate("Dialog3", "Feature release"))
        self.comboBox3.setItemText(5, _translate("Dialog3", "Aenderungen"))
        self.comboBox3.setItemText(6, _translate("Dialog3", "Ist/Soll"))
        self.comboBox3.setItemText(7, _translate("Dialog3", "ProjektrundenA"))
        self.comboBox3.setItemText(8, _translate("Dialog3", "ProjektrundenB"))
        self.PlotButton3.setText(_translate("Dialog3", "Plot"))
        self.backButton3.setText(_translate("Dialog3", "Back"))

