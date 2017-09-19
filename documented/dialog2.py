# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(619, 300)
        self.layoutWidget = QtWidgets.QWidget(Dialog2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 581, 230))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox21 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox21.setObjectName("checkBox21")
        self.gridLayout.addWidget(self.checkBox21, 0, 0, 1, 1)
        self.checkBox22 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox22.setObjectName("checkBox22")
        self.gridLayout.addWidget(self.checkBox22, 1, 0, 1, 1)
        self.checkBox23 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox23.setObjectName("checkBox23")
        self.gridLayout.addWidget(self.checkBox23, 2, 0, 1, 1)
        self.checkBox24 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox24.setObjectName("checkBox24")
        self.gridLayout.addWidget(self.checkBox24, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.comboBox2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.setItemText(0, "")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.gridLayout.addWidget(self.comboBox2, 5, 0, 1, 1)
        self.PlotButton2 = QtWidgets.QPushButton(self.layoutWidget)
        self.PlotButton2.setObjectName("PlotButton2")
        self.gridLayout.addWidget(self.PlotButton2, 6, 0, 1, 1)
        self.backButton2 = QtWidgets.QPushButton(self.layoutWidget)
        self.backButton2.setObjectName("backButton2")
        self.gridLayout.addWidget(self.backButton2, 7, 0, 1, 1)

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "INV Client"))
        self.checkBox21.setText(_translate("Dialog2", "OEM (BMW, Ford)"))
        self.checkBox22.setText(_translate("Dialog2", "Tier 1 (Conti, TRW, Helloa, ZF, Bosch, Webasto, Bombardier, Braexelmaier, Peiker)"))
        self.checkBox23.setText(_translate("Dialog2", "Tier 2 (Renesas, Perei)"))
        self.checkBox24.setText(_translate("Dialog2", "Non Automotive (Bosch ebike, Franki Grundbau, Soehner)"))
        self.label.setText(_translate("Dialog2", "Question"))
        self.comboBox2.setItemText(1, _translate("Dialog2", "Teamgroese"))
        self.comboBox2.setItemText(2, _translate("Dialog2", "PEP"))
        self.comboBox2.setItemText(3, _translate("Dialog2", "Struktur"))
        self.comboBox2.setItemText(4, _translate("Dialog2", "Tools"))
        self.comboBox2.setItemText(5, _translate("Dialog2", "Detailplanung"))
        self.comboBox2.setItemText(6, _translate("Dialog2", "Ressourcenplanung"))
        self.comboBox2.setItemText(7, _translate("Dialog2", "Kostenplanung"))
        self.comboBox2.setItemText(8, _translate("Dialog2", "Aenderungen"))
        self.comboBox2.setItemText(9, _translate("Dialog2", "ProjektrundenA"))
        self.comboBox2.setItemText(10, _translate("Dialog2", "ProjektrundenB"))
        self.comboBox2.setItemText(11, _translate("Dialog2", "Templates"))
        self.comboBox2.setItemText(12, _translate("Dialog2", "Organisationsform"))
        self.comboBox2.setItemText(13, _translate("Dialog2", "PMO"))
        self.PlotButton2.setText(_translate("Dialog2", "Plot"))
        self.backButton2.setText(_translate("Dialog2", "Back"))

