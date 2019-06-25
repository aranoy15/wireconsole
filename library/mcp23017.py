import enum
from smbus2 import SMBusWrapper
import time
import os

class McpMode(enum.Enum):
    OUTPUT = False
    INPUT = True

class McpState(enum.Enum):
    OFF = False
    ON = True

class McpRegs(enum.Enum):
    IODIRA = 0x00
    IODIRB = 0x01
    IPOLA = 0x02
    IPOLB = 0x03
    GPINTENA = 0x04
    GPINTENB = 0x05
    DEFVALA = 0x06
    DEFVALB = 0x07
    IOCONA = 0x0A
    IOCONB = 0x0B
    GPPUA = 0x0C
    GPPUB = 0x0D
    INTFA = 0x0E
    INTFB = 0x0F
    INTCAPA = 0x10
    INTCAPB = 0x11
    GPIOA = 0x12
    GPIOB = 0x13
    OLATA = 0x14
    OLATB = 0x15

class Mcp23017:
    def __init__(self, address: int):
        if address < 0:
            address = 0
        
        if address > 7:
            address = 7

        self.__baseAddress = 0x20
        self.__baseAddress |= address

        self.writeRegister(McpRegs.IODIRA, 0xFF)
        self.writeRegister(McpRegs.IODIRB, 0xFF)

    def __str__(self) -> str:
        result = os.linesep
        result += 'Mcp23017 info:' + os.linesep
        result += 'address = 0x{:02X}'.format(self.address) + os.linesep
        return result

    @property
    def address(self) -> int:
        return self.__baseAddress

    def bitWrite(self, value: int, pin: int, pinValue: bool):
        if pinValue:
            value |= (1 << pin)
        else:
            value &= ~(1 << pin)

        return value
        

    def bitForPin(self, pin: int) -> int:
        return pin % 8

    def regForPin(self, pin: int, addrA: McpRegs, addrB: McpRegs) -> int:
        return (addrA if pin < 8 else addrB)

    def readRegister(self, reg: McpRegs) -> int:
        result = 0
        try:
            with SMBusWrapper(1) as bus:
                result = bus.read_byte_data(self.address, reg.value)
        except OSError as err:
            print('i2c read error:', str(err))

        print('Read register 0x{2:02X} {1}: {0:08b}'.format(result, reg, self.address))

        return result

    def writeRegister(self, reg: McpRegs, value: int):
        print('Write register 0x{2:02X} {1}: {0:08b}'.format(value, reg, self.address))

        try:
            with SMBusWrapper(1) as bus:
                bus.write_byte_data(self.address, reg.value, value)
        except OSError as err:
            print('i2c write error:', str(err))

    def updateRegisterBit(self, pin: int, value: bool, addrA: McpRegs, addrB: McpRegs):
        regAddr = self.regForPin(pin, addrA, addrB)
        bit = self.bitForPin(pin)
        regValue = self.readRegister(regAddr)

        regValue = self.bitWrite(regValue, bit, value)


        self.writeRegister(regAddr, regValue)

    def pinMode(self, pin: int, mode: McpMode):
        self.updateRegisterBit(pin, mode.value, McpRegs.IODIRA, McpRegs.IODIRB)

    def readGPIOAB(self) -> int:
        regAValue = self.readRegister(McpRegs.GPIOA)
        regBValue = self.readRegister(McpRegs.GPIOB)

        return ((regBValue << 8) | regAValue)

    def readGPIO(self, reg: McpRegs):
        return self.readRegister(reg)

    def writeGPIOAB(self, value: int):
        self.writeRegister(McpRegs.GPIOA, value & 0xFF)
        self.writeRegister(McpRegs.GPIOB, (value >> 8) & 0xFF)

    def digitalWrite(self, pin: int, state: McpState):
        bit = self.bitForPin(pin)

        regAddr = self.regForPin(pin, McpRegs.OLATA, McpRegs.OLATB)
        gpio = self.readRegister(regAddr)

        gpio = self.bitWrite(gpio, bit, state.value)

        regAddr = self.regForPin(pin, McpRegs.GPIOA, McpRegs.GPIOB)
        self.writeRegister(regAddr, gpio)
