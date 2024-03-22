# print("Ahoj světe")

import time
from telemetrix import telemetrix
boardESP = telemetrix.Telemetrix(arduino_instance_id=2)
boardSTM = telemetrix.Telemetrix(arduino_instance_id=1)


def makePin(portName, pinNumber):
    return (ord(portName) - ord("A")) * 16 + pinNumber 

pinSTM = makePin("C",7)
pinESP = 23
boardESP.set_pin_mode_digital_output(pinESP)
boardSTM.set_pin_mode_digital_output(pinSTM)
while True:
    boardESP.digital_write(pinESP, 1)
    boardSTM.digital_write(pinSTM, 1)
    time.sleep(1)
    boardESP.digital_write(pinESP, 0)
    boardSTM.digital_write(pinSTM, 0)
    time.sleep(1)