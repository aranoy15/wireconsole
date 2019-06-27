from PyQt5 import QtWidgets, QtWidgets, QtGui, QtCore
from logic.wireconsole.widgets.ui_py.Ui_drawwidget import Ui_DrawWidget
from library.wiredata import WireData, WireStatus
import time

class DrawWidget(QtWidgets.QWidget, Ui_DrawWidget):

    @property
    def penWidth(self):
        return 2

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

    @property
    def miniTitleFont(self):
        return QtGui.QFont("Time", 8, 4)

    @property
    def sceneSize(self):
        return 600

    @property 
    def maxIndexScale(self):
        return self.sceneSize / 2

    """
    @property
    def wirkingPlace(self):
        return self.maxIndexScale - self.__currentY
    """

    def __init__(self, data: WireData):
        super().__init__()
        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene(-(self.sceneSize / 2), -(self.sceneSize / 2), self.sceneSize, self.sceneSize, self)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.__data = data.data
        self.__currentY = -self.maxIndexScale

        self.horizontalLayout.addWidget(self.view)

    def getPen(self, status: WireStatus) -> QtGui.QPen:
        if status == WireStatus.OK:
            return self.goodPen
        elif status == WireStatus.ERROR:
            return self.errorPen
        elif status == WireStatus.PROCESS:
            return self.processPen
        else:
            return self.normalPen

    def drawTemplate(self, templateName: str):
        self.scene.clear()

        currentTemplateData = next(
            iter([item for item in self.__data if item['name'] == templateName]))

        self.drawTitle(templateName)
        self.drawItems(currentTemplateData)

    def drawTitle(self, title):
        text = f"Шаблон: {title}"
        startX = -(len(text) / 2) * \
            QtGui.QFontMetrics(self.titleFont).width(text) / len(text)

        self.__currentY += QtGui.QFontMetrics(self.titleFont).height()
        self.__currentY += 50
        

        titleItem = QtWidgets.QGraphicsTextItem()
        titleItem.setPos(startX, -(self.sceneSize / 2))
        titleItem.setPlainText(text)
        titleItem.setFont(self.titleFont)
        self.scene.addItem(titleItem)

    def drawItems(self, templateData: dict):

        self.printOuts(templateData)
        self.printIns(templateData)
        self.drawWires(templateData)

        

    def printOuts(self, templateData: dict):
        items = templateData['wires']
        workingPlace = self.maxIndexScale - self.__currentY

        outs = list(set([item['out'] for item in items]))

        currentY = self.__currentY
        outsHeight = workingPlace / len(outs)

        for i in range(len(outs)):

            startX = -self.maxIndexScale
            startY = currentY + (outsHeight / 2)

            templateData['outsY'].update({outs[i]: startY + (QtGui.QFontMetrics(self.itemFont).height() / 2)})

            startY -= QtGui.QFontMetrics(self.itemFont).height() / 4

            title = "O{0}".format(outs[i] + 1)

            titleWidth = QtGui.QFontMetrics(self.itemFont).width(title)
            startX -= titleWidth + titleWidth / 4

            titleItem = QtWidgets.QGraphicsTextItem() 
            titleItem.setPos(startX, startY)
            titleItem.setPlainText(title)
            titleItem.setFont(self.itemFont)
            self.scene.addItem(titleItem)

            currentY += outsHeight

    def printIns(self, templateData: dict):
        items = templateData['wires']
        workingPlace = self.maxIndexScale - self.__currentY

        ins = []
        for item in items:
            ins.extend(item['ins'])
        inputs = list(set(ins))

        currentY = self.__currentY
        insHeight = workingPlace / len(inputs)
        
        for i in range(len(inputs)):
            startX = self.maxIndexScale
            startY = currentY + (insHeight / 2)

            templateData['insY'].update({ins[i]: startY + (QtGui.QFontMetrics(self.itemFont).height() / 2)})

            charHeight = QtGui.QFontMetrics(self.itemFont).height()
            startY -= charHeight / 4

            titleItem = QtWidgets.QGraphicsTextItem()
            titleItem.setPos(startX, startY)
            titleItem.setPlainText(f"I{inputs[i] + 1}")
            titleItem.setFont(self.itemFont)
            self.scene.addItem(titleItem)

            currentY += insHeight


    def drawWires(self, templateData:dict):
        wires = templateData['wires']

        for wire in wires:
            outY = templateData['outsY'][wire['out']]
            self.scene.addLine(-self.maxIndexScale, outY, 0, outY, self.getPen(wire['status']))

            for inp in wire['ins']:
                inpY = templateData['insY'][inp]
                self.scene.addLine(0, outY, 0, inpY, self.getPen(wire['status']))
                self.scene.addLine(0, inpY, self.maxIndexScale, inpY, self.getPen(wire['status']))

                text = f"O{wire['out']}"
                titleItem = QtWidgets.QGraphicsTextItem()
                textY = inpY - (QtGui.QFontMetrics(self.miniTitleFont).height() + 5)
                textX = self.maxIndexScale - (QtGui.QFontMetrics(self.miniTitleFont).width(text) * 2)
                titleItem.setPos(textX, textY)
                titleItem.setPlainText(text)
                titleItem.setFont(self.miniTitleFont)
                self.scene.addItem(titleItem)
                #self.scene.addLine(0, outY, 0, templateData['outsY'][inp], self.getPen(wire['status']))