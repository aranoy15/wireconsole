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
        self.horizontalLayout = QtWidgets.QHBoxLayout(DrawWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(1, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)

        self.retranslateUi(DrawWidget)
        QtCore.QMetaObject.connectSlotsByName(DrawWidget)

    def retranslateUi(self, DrawWidget):
        _translate = QtCore.QCoreApplication.translate
        DrawWidget.setWindowTitle(_translate("DrawWidget", "Form"))


import  template_rc
