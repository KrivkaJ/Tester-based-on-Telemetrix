import time
from telemetrix import telemetrix
#boardESP = telemetrix.Telemetrix(arduino_instance_id=2)
boardSTM = telemetrix.Telemetrix(arduino_instance_id=1)

def makePin(portName, pinNumber):
    return (ord(portName) - ord("A")) * 16 + pinNumber 

global_value = 0

list_esp_read_stm = [] # stm pin, coresponding esp pin, read value
#pins for esp to read from stm
list_esp_read_stm.append([makePin('F', 13), 23, 0])
list_esp_read_stm.append([makePin('F', 14), 22, 0])
list_esp_read_stm.append([makePin('C', 10), 36, 0]) #these 4 input only on stm
list_esp_read_stm.append([makePin('C', 11), 39, 0])
list_esp_read_stm.append([makePin('C', 12), 34, 0])
list_esp_read_stm.append([makePin('C', 13), 35, 0])
list_esp_read_stm.append([makePin('E', 1), 21, 0])
list_esp_read_stm.append([makePin('E', 2), 19, 0])
list_esp_read_stm.append([makePin('E', 3), 18, 0])
list_esp_read_stm.append([makePin('E', 4), 5, 0])
list_esp_read_stm.append([makePin('E', 5), 17, 0])
list_esp_read_stm.append([makePin('E', 6), 16, 0])
list_esp_read_stm.append([makePin('E', 7), 4, 0])
list_esp_read_stm.append([makePin('E', 8), 0, 0])
list_esp_read_stm.append([makePin('E', 9), 2, 0])
list_esp_read_stm.append([makePin('E', 10), 15, 0])
list_esp_read_stm.append([makePin('C', 14), 32, 0])
list_esp_read_stm.append([makePin('C', 15), 33, 0])
list_esp_read_stm.append([makePin('D', 0), 25, 0])
list_esp_read_stm.append([makePin('D', 1), 26, 0])
list_esp_read_stm.append([makePin('D', 2), 27, 0])
list_esp_read_stm.append([makePin('D', 3), 14, 0])
list_esp_read_stm.append([makePin('D', 4), 12, 0])
list_esp_read_stm.append([makePin('D', 5), 13, 0])

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3

def the_callback(data):
    """
    A callback function to report data changes.
    This will print the pin number, its reported value and
    the date and time when the change occurred

    :param data: [pin, current reported value, pin_mode, timestamp]
    """
    global global_value
    global_value = data[CB_VALUE]
    
    
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
    my_board.enable_digital_reporting(pin)
    my_board.set_pin_mode_digital_input(pin, the_callback)
    #time.sleep(1)
    #my_board.disable_all_reporting()
    # time.sleep(4)
    # my_board.enable_digital_reporting(12)

    #time.sleep(3)
    #time.sleep(1)

    #print('Enter Control-C to quit.')
    # my_board.enable_digital_reporting(12)


#pinSTM = makePin("F",13)
#pinESP = 23
#boardESP.set_pin_mode_digital_output(pinESP)
#boardSTM.set_pin_mode_digital_input(pinSTM)

boardSTM.disable_all_reporting()

#for esp_read_stm in list_esp_read_stm:
 #   digital_in(boardSTM, esp_read_stm[0])

digital_in(boardSTM, makePin('G', 3))
while True:
    time.sleep(1)