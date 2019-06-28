from library.utils import Stoppable, Clearable
from PyQt5 import QtCore
from library.wiredata import WireData, WireStatus
import time
from library.mcp23017 import Mcp23017

class TestThread(QtCore.QThread, Stoppable, Clearable):

    completeTest = QtCore.pyqtSignal(object)
    updateWireStatus = QtCore.pyqtSignal(object)

    def __init__(self, data: WireData):
        super().__init__()

        self.__data = data.data
        self.__templateName = ''
        self.__mutex = QtCore.QMutex()

    template = property()
    
    @template.getter
    def template(self):
        return self.__templateName

    @template.setter
    def template(self, value):
        if value:
            self.__templateName = value

    def run(self):
        QtCore.QMutexLocker(self.__mutex)
        
        self.clearFlags()
        currentTemplateData = next(
            iter([item for item in self.__data if item['name'] == self.__templateName]))

        testResult = True

        for wire in currentTemplateData['wires']:
            if self.needStop:
                testResult = False
                break

            if not self.needStop:
                time.sleep(1)
                wire['status'] = int(WireStatus.OK)
                print(wire)
                self.updateWireStatus.emit(wire)

        self.completeTest.emit(testResult)


