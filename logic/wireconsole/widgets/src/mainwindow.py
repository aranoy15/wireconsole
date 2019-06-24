from PyQt5 import QtWidgets, QtCore
from logic.wireconsole.widgets.ui_py.Ui_mainwindow import Ui_MainWindow
from logic.wireconsole.widgets.src.menuwidget import MenuWidget
from logic.wireconsole.widgets.src.drawwidget import DrawWidget

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        #self.showFullScreen()

        self.menu = MenuWidget()
        self.draw = DrawWidget()

        self.mainLayout.addWidget(self.menu)
        self.mainLayout.addWidget(self.draw)

        self.menu.pushButton.clicked.connect(self.test)
    
    def keyPressEvent(self, event):
        #super(MyWidget, self).keyPressEvent(event)

        if event.key() == QtCore.Qt.Key_Backspace:
            print('Backspace pressed')
        print(event.key())
        print('Backspace key:', QtCore.Qt.Key_Backspace)
        #event.ignore()

    def resizeEvent(self, event):
        return super(MainWindow, self).resizeEvent(event)

    def test(self):
        print('Click')

    def resizeWindow(self):
        print('Resize')

    def close_window_event(self): 
        pass
