from logic.wireconsole.widgets.ui_py.Ui_menuwidget import Ui_MenuWidget
from PyQt5 import QtWidgets, QtCore
from library.wiredata import WireData
from enum import Enum

class StatusType(Enum):
    GOOD = 0
    ERROR = 1
    INFO = 2

class MenuWidget(QtWidgets.QWidget, Ui_MenuWidget):
    startTestSignal = QtCore.pyqtSignal(object)
    cancelTestSignal = QtCore.pyqtSignal()

    @property
    def startButtonText(self):
        return "Старт"
    
    @property
    def cancelButtonText(self):
        return "Завершить"

    def __init__(self, data: WireData):
        super().__init__()
        self.setupUi(self)

        self.__data = data.data
        self.updateWireTypeList()

        self.btnStart.clicked.connect(self.btnStartClicked)

    def updateWireTypeList(self):
        self.cmbWireType.clear()
        self.cmbWireType.addItems([item['name'] for item in self.__data])

    @QtCore.pyqtSlot(object)
    def updateStatus(self, status: str):
        self.lblStatus.setText(status)

    @QtCore.pyqtSlot()
    def btnStartClicked(self):
        self.btnStart.setEnabled(False)

        if self.btnStart.text() == self.startButtonText:
            self.startTest()
        else:
            self.cancelTest()

        self.btnStart.setEnabled(True)

    def startTest(self):
        self.btnStart.setText(self.cancelButtonText)
        self.startTestSignal.emit(self.cmbWireType.currentText())

    def cancelTest(self):
        self.btnStart.setText(self.startButtonText)
        self.cancelTestSignal.emit()

    def completeTest(self):
        self.btnStart.setEnabled(False)
        self.btnStart.setText(self.startButtonText)
        self.btnStart.setEnabled(True)