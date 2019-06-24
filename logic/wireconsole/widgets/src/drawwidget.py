from PyQt5 import QtWidgets, QtWidgets, QtGui, QtCore
from logic.wireconsole.widgets.ui_py.Ui_drawwidget import Ui_DrawWidget

class DrawWidget(QtWidgets.QWidget, Ui_DrawWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.view = QtWidgets.QGraphicsView(self.scene)

        self.horizontalLayout.addWidget(self.view)

        pen = QtGui.QPen(QtCore.Qt.red)
        rect = QtCore.QRectF(100.0, 100.0, 10.0, 10.0)

        self.scene.addRect(rect, pen)
        self.scene.addLine(100.0, -200.0, 100.0, 100.0, QtGui.QPen(QtCore.Qt.blue))
