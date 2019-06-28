from library.utils import Stoppable, Clearable
from PyQt5 import QtCore
from library.wiredata import WireData, WireStatus
import time
from library.mcp23017 import Mcp23017, McpRegs, McpState

class TestThread(QtCore.QThread, Stoppable, Clearable):

    completeTest = QtCore.pyqtSignal(object)
    updateWireStatus = QtCore.pyqtSignal(object)

    def __init__(self, data: WireData):
        super().__init__()

        self.__data = data.data
        self.__templateName = ''
        self.__mutex = QtCore.QMutex()

        self.__outputs = [Mcp23017(0), Mcp23017(1), Mcp23017(2)]
        self.__inputs = [Mcp23017(4), Mcp23017(5), Mcp23017(6)]

    template = property()
    
    @template.getter
    def template(self):
        return self.__templateName

    @template.setter
    def template(self, value):
        if value:
            self.__templateName = value

    def init(self):
        for item in self.__outputs:
            item.writeRegister(McpRegs.IODIRA, 0x00)
            item.writeRegister(McpRegs.IODIRB, 0x00)

            item.writeGPIOAB(0)

    def setOutput(self, value: int):
        self.__outputs[0].writeGPIOAB(value & 0xFFFF)
        self.__outputs[1].writeGPIOAB((value >> 16) & 0xFFFF)
        self.__outputs[2].writeGPIOAB((value >> 32) & 0xFFFF)

    def readInput(self) -> int:
        value = 0
        value &= self.__inputs[0].readGPIOAB()
        value &= self.__inputs[1].readGPIOAB() << 16
        value &= self.__inputs[2].readGPIOAB() << 32

        return value

    def run(self):
        QtCore.QMutexLocker(self.__mutex)
        
        self.init()
        self.clearFlags()
        currentTemplateData = next(
            iter([item for item in self.__data if item['name'] == self.__templateName]))

        testResult = True

        for wire in currentTemplateData['wires']:
            if self.needStop:
                testResult = False
                break

            if not self.needStop:
                self.setOutput(wire['outs'])
                time.sleep(1)
                readInputs = self.readInput()

                compareInputs = 0

                for i in wire['ins']:
                    compareInputs &= (1 << i)

                if readInputs == compareInputs:
                    wire['status'] = int(WireStatus.OK)
                else:
                    print('Read inputs: {0: 048b}'.format(readInputs))
                    print('Compare inputs: {0: 048b}'.format(compareInputs))

                    testResult = False
                    wire['status'] = int(WireStatus.ERROR)
                    
                self.updateWireStatus.emit(wire)

        self.completeTest.emit(testResult)


