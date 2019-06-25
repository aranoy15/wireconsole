import time
from library.mcp23017 import Mcp23017, McpMode, McpState

def main():
    print('Start application')

    mcp = Mcp23017(0)
    print(mcp)

    mcp.pinMode(0, McpMode.OUTPUT)
    mcp.digitalWrite(0, McpState.ON)

    while True:
        state = mcp.readGPIOAB()
        print('States: {0:016b}'.format(state))
        print('')

        time.sleep(0.5)


if __name__ == '__main__':
    main()
