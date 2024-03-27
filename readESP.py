# print("Ahoj světe")

import sys
import time
from telemetrix import telemetrix
boardESP = telemetrix.Telemetrix(arduino_instance_id=2)
boardSTM = telemetrix.Telemetrix(arduino_instance_id=1)


def makePin(portName, pinNumber):
    return (ord(portName) - ord("A")) * 16 + pinNumber 

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3

pin_value = int(0)

def the_callback(data):
    """
    A callback function to report data changes.
    This will print the pin number, its reported value and
    the date and time when the change occurred

    :param data: [pin, current reported value, pin_mode, timestamp]
    """
    global pin_value
    pin_value = data[CB_VALUE]
    
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[CB_TIME]))
    print(f'Pin Mode: {data[CB_PIN_MODE]} Pin: {data[CB_PIN]} Value: {data[CB_VALUE]} Time Stamp: {date}')


def digital_in(my_board, pin):
    """
     This function establishes the pin as a
     digital input. Any changes on this pin will
     be reported through the call back function.

     :param my_board: a telemetrix instance
     :param pin: Arduino pin number
     """

    # set the pin mode
    my_board.set_pin_mode_digital_input(pin, the_callback)
    #time.sleep(1)
    #my_board.disable_all_reporting()
    # time.sleep(4)
    # my_board.enable_digital_reporting(12)

    #time.sleep(3)
    my_board.enable_digital_reporting(pin)
    #time.sleep(1)

    #print('Enter Control-C to quit.')
    # my_board.enable_digital_reporting(12)


pinSTM = makePin("F",13)
pinESP = 23
boardESP.set_pin_mode_digital_output(pinESP)
#boardSTM.set_pin_mode_digital_input(pinSTM)
while True:
    boardESP.digital_write(pinESP, 0)
    digital_in(boardSTM, pinSTM)
    print(pin_value)
    time.sleep(1)
    boardESP.digital_write(pinESP, 1)
    digital_in(boardSTM, pinSTM)
    print(pin_value)
    time.sleep(1)
    #boardESP.digital_write(pinESP, 0)
    #boardSTM.digital_write(pinSTM, 0)
    #time.sleep(1)