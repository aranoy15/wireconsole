# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aranoy15/projects/raspprojects/logic/wireconsole/widgets/ui/menuwidget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWidget(object):
    def setupUi(self, MenuWidget):
        MenuWidget.setObjectName("MenuWidget")
        MenuWidget.resize(679, 50)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MenuWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(MenuWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lblStatus = QtWidgets.QLabel(MenuWidget)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.horizontalLayout.addWidget(self.lblStatus)
        spacerItem = QtWidgets.QSpacerItem(473, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmbWireType = QtWidgets.QComboBox(MenuWidget)
        self.cmbWireType.setMinimumSize(QtCore.QSize(200, 0))
        self.cmbWireType.setObjectName("cmbWireType")
        self.horizontalLayout.addWidget(self.cmbWireType)
        self.btnStart = QtWidgets.QPushButton(MenuWidget)
        self.btnStart.setMinimumSize(QtCore.QSize(100, 0))
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)

        self.retranslateUi(MenuWidget)
        QtCore.QMetaObject.connectSlotsByName(MenuWidget)

    def retranslateUi(self, MenuWidget):
        _translate = QtCore.QCoreApplication.translate
        MenuWidget.setWindowTitle(_translate("MenuWidget", "Form"))
        self.label.setText(_translate("MenuWidget", "Статус:"))
        self.btnStart.setText(_translate("MenuWidget", "Старт"))


