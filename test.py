import time
from library.mcp23017 import Mcp23017, McpMode, McpState, McpRegs

def main():
    print('Start application')

    mcpOut = Mcp23017(0)
    mcpIn = Mcp23017(4)

    print(mcpOut)
    print(mcpIn)

    for i in range(8):
        mcpOut.pinMode(i, McpMode.OUTPUT)

    mcpOut.digitalWrite(0, McpState.ON)

    c = 0
    while True:
        print('c:', c) 
        c += 1

        print('IO A:', '{0:08b}'.format(mcpIn.readRegister(McpRegs.IODIRA)))
        print('IO B:', '{0:08b}'.format(mcpIn.readRegister(McpRegs.IODIRB)))

        state = mcpIn.readGPIOAB()
        print('States: {0:016b}'.format(state))
        print('')

        time.sleep(0.5)


if __name__ == '__main__':
    main()
