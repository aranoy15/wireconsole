import locale
from PyQt5 import QtWidgets

def setting(app, window):
    if not isinstance(app, QtWidgets.QApplication) or not isinstance(app, QtWidgets.QApplication):
        return

    locale.setlocale(locale.LC_ALL, "")
    app.setStyle('Fusion')
    app.aboutToQuit.connect(window.close_window_event)
    window.show()
    app.exec_()