from PyQt5 import QtWidgets, QtWidgets, QtGui, QtCore
from logic.wireconsole.widgets.ui_py.Ui_drawwidget import Ui_DrawWidget
from library.wiredata import WireData
import time

class DrawWidget(QtWidgets.QWidget, Ui_DrawWidget):

    @property
    def penWidth(self):
        return 3

    @property
    def normalPen(self):
        return QtGui.QPen(QtCore.Qt.black, self.penWidth)

    @property
    def goodPen(self):
        return QtGui.QPen(QtCore.Qt.green, self.penWidth)
    
    @property
    def errorPen(self):
        return QtGui.QPen(QtCore.Qt.red, self.penWidth)

    @property
    def processPen(self):
        return QtGui.QPen(QtGui.QColor("orange"), self.penWidth)

    @property
    def titleFont(self):
        return QtGui.QFont("Time", 32, 10)

    @property
    def itemFont(self):
        return QtGui.QFont("Time", 12, 4)

    def __init__(self, data: WireData):
        super().__init__()
        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene(-200, -200, 400, 400, self)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.__data = data.data

        self.horizontalLayout.addWidget(self.view)

    def drawTemplate(self, templateName: str):
        self.scene.clear()

        currentTemplateData = next(
            iter([item['wires'] for item in self.__data if item['name'] == templateName]))

        count = max([max([item['out'] for item in currentTemplateData]),
                     max([max(item['ins']) for item in currentTemplateData])])

        self.drawTitle(templateName)

        for item in currentTemplateData:
            print(item)



    def drawTitle(self, title):
        text = f"Шаблон: {title}"
        startX = -(len(text) / 2) * \
            QtGui.QFontMetrics(self.titleFont).width(text) / len(text)

        titleItem = QtWidgets.QGraphicsTextItem()
        titleItem.setPos(startX, -250)
        titleItem.setPlainText(text)
        titleItem.setFont(self.titleFont)
        self.scene.addItem(titleItem)



        """
        pen = QtGui.QPen(QtCore.Qt.red)
        rect = QtCore.QRectF(100.0, 100.0, 10.0, 10.0)

        self.scene.addRect(rect, pen)
        self.scene.addLine(100.0, -200.0, 100.0, 100.0, QtGui.QPen(QtCore.Qt.blue))
        """
