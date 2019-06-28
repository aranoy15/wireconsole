from PyQt5 import QtWidgets, QtCore
from logic.wireconsole.widgets.ui_py.Ui_mainwindow import Ui_MainWindow
from logic.wireconsole.widgets.src.menuwidget import MenuWidget
from logic.wireconsole.widgets.src.drawwidget import DrawWidget
from library.wiredata import WireData
from library.testthread import TestThread

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        #self.showFullScreen()

        self.wireData = WireData()
        self.menu = MenuWidget(self.wireData)
        self.draw = DrawWidget(self.wireData)
        self.testThread = TestThread(self.wireData)

        self.mainLayout.addWidget(self.menu)
        self.mainLayout.addWidget(self.draw)

        self.menu.cmbWireType.currentIndexChanged.connect(self.wireTypeChanged)

        self.menu.startTestSignal.connect(self.startTest)
        self.menu.cancelTestSignal.connect(self.cancelTest)
        self.testThread.completeTest.connect(self.completeTest)
        self.testThread.updateWireStatus.connect(self.updateWireStatus)
        #self.installEventFilter(self)

        self.draw.drawTemplate(self.menu.cmbWireType.currentText())

    @QtCore.pyqtSlot()
    def wireTypeChanged(self):
        self.draw.drawTemplate(self.menu.cmbWireType.currentText())
        print("Wire type changed")

    @QtCore.pyqtSlot(object)
    def startTest(self, templateName: str):
        self.draw.clearStatus()
        self.testThread.template = templateName
        self.testThread.start()
        print('Start test:', templateName)

    @QtCore.pyqtSlot()
    def cancelTest(self):
        print('Cancel test')
        self.testThread.stop()

    @QtCore.pyqtSlot(object)
    def updateWireStatus(self, wire: dict):
        self.draw.updateStatus(wire)

    @QtCore.pyqtSlot(object)
    def completeTest(self, result: bool):
        self.menu.completeTest()

    def keyPressEvent(self, event):
        #super(MyWidget, self).keyPressEvent(event)

        if event.key() == QtCore.Qt.Key_D and event.modifiers() == QtCore.Qt.ControlModifier:
            if self.isFullScreen():
                    self.showNormal()
            else:
                self.showFullScreen()

    def resizeEvent(self, event):
        return super(MainWindow, self).resizeEvent(event)

    def close_window_event(self): 
        pass
