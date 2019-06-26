from PyQt5 import QtWidgets, QtCore
from logic.wireconsole.widgets.ui_py.Ui_mainwindow import Ui_MainWindow
from logic.wireconsole.widgets.src.menuwidget import MenuWidget
from logic.wireconsole.widgets.src.drawwidget import DrawWidget
from library.wiredata import WireData

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        #self.showFullScreen()

        self.wireData = WireData()
        self.menu = MenuWidget(self.wireData)
        self.draw = DrawWidget(self.wireData)

        self.mainLayout.addWidget(self.menu)
        self.mainLayout.addWidget(self.draw)

        self.menu.cmbWireType.currentIndexChanged.connect(self.wireTypeChanged)
        #self.installEventFilter(self)

        self.draw.drawTemplate(self.menu.cmbWireType.currentText())

    @QtCore.pyqtSlot()
    def wireTypeChanged(self):
        self.draw.drawTemplate(self.menu.cmbWireType.currentText())
        print("Wire type changed")

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
