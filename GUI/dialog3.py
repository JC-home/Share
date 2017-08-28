# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(619, 300)
        self.widget = QtWidgets.QWidget(Dialog2)
        self.widget.setGeometry(QtCore.QRect(20, 20, 581, 230))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 0, 1, 1)

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Ext Client"))
        self.checkBox.setText(_translate("Dialog2", "VW (VW, Audi, Porsche)"))
        self.checkBox_2.setText(_translate("Dialog2", "BMW (BMW)"))
        self.checkBox_3.setText(_translate("Dialog2", "Others (Daimler, Fiat, GM, Evobus, PSA, Honda, OEMs)"))
        self.checkBox_4.setText(_translate("Dialog2", "Not Relevant (Hella, Franki Grundbau, internal developement)"))
        self.label.setText(_translate("Dialog2", "Question"))
        self.comboBox.setItemText(0, _translate("Dialog2", " "))
        self.comboBox.setItemText(1, _translate("Dialog2", "Entwicklungszeit"))
        self.comboBox.setItemText(2, _translate("Dialog2", "Schnittstelle"))
        self.comboBox.setItemText(3, _translate("Dialog2", "Planung"))
        self.comboBox.setItemText(4, _translate("Dialog2", "Feature release"))
        self.comboBox.setItemText(5, _translate("Dialog2", "Aenderungen"))
        self.comboBox.setItemText(6, _translate("Dialog2", "Ist/Soll"))
        self.comboBox.setItemText(7, _translate("Dialog2", "Projektkunden"))
        self.pushButton.setText(_translate("Dialog2", "Plot"))
        self.pushButton_2.setText(_translate("Dialog2", "Back"))

