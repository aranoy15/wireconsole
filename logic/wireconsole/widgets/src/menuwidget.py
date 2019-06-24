from logic.wireconsole.widgets.ui_py.Ui_menuwidget import Ui_MenuWidget
from PyQt5 import QtWidgets

class MenuWidget(QtWidgets.QWidget, Ui_MenuWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)