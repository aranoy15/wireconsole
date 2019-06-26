
from PyQt5 import QtCore
import template_rc
import json
import enum
import os
import inspect

class WireData:

    def __init__(self):
        self.__path = ':/template.json'
        self.__data = list()
        self.__mutex = QtCore.QMutex()

    @property
    def path(self) -> str:
        return self.__path

    @property
    def data(self) -> list:
        self.__mutex.lock()

        if len(self.__data) == 0:
            self.loadData()

        self.__mutex.unlock()

        return self.__data

    def loadData(self):
        self.__data.clear()
        self.__data = json.loads(self.__getRawData())['data']

    def __getRawData(self):
        f = QtCore.QFile(self.path)

        if f.open(QtCore.QIODevice.ReadOnly):
            text = QtCore.QTextStream(f)

        text.setCodec('UTF-8')
        result = text.readAll()
        f.close()

        return result