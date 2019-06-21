from PyQt5 import QtWidgets, QtCore
from logic.wireconsole.widgets.ui_py.Ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def close_window_event(self):
        pass
