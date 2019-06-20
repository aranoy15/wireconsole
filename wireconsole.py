import sys

from PyQt5 import QtWidgets
from logic.wireconsole.widgets.src.mainwindow import MainWindow
import mainsetting
import locale

def main(argv):
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    mainsetting.setting(app, window)

if __name__ == '__main__':
    main(sys.argv)