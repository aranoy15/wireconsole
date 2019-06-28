# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aranoy15/projects/raspprojects/logic/wireconsole/widgets/ui/drawwidget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DrawWidget(object):
    def setupUi(self, DrawWidget):
        DrawWidget.setObjectName("DrawWidget")
        DrawWidget.resize(543, 664)
        self.verticalLayout = QtWidgets.QVBoxLayout(DrawWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.verticalLayout.addLayout(self.mainLayout)

        self.retranslateUi(DrawWidget)
        QtCore.QMetaObject.connectSlotsByName(DrawWidget)

    def retranslateUi(self, DrawWidget):
        _translate = QtCore.QCoreApplication.translate
        DrawWidget.setWindowTitle(_translate("DrawWidget", "Form"))


import template_rc
