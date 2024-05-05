import time
from telemetrix import telemetrix
boardESP = telemetrix.Telemetrix(arduino_instance_id=2)
boardSTM = telemetrix.Telemetrix(arduino_instance_id=1)

def makePin(portName, pinNumber):
    return (ord(portName) - ord("A")) * 16 + pinNumber 

list_stm_read_esp = [] # stm pin, coresponding esp pin, read value
global_value = 0

list_stm_read_esp.append([makePin('G', 2), 1, 0])
list_stm_read_esp.append([makePin('G', 3), 2, 0])
list_stm_read_esp.append([makePin('B', 3), 4, 0])
list_stm_read_esp.append([makePin('B', 4), 5, 0])
list_stm_read_esp.append([makePin('B', 5), 6, 0])
list_stm_read_esp.append([makePin('B', 6), 7, 0])
list_stm_read_esp.append([makePin('B', 11), 8, 0])
list_stm_read_esp.append([makePin('B', 14), 9, 0])
list_stm_read_esp.append([makePin('B', 15), 10, 0])
list_stm_read_esp.append([makePin('C', 0), 11, 0])
list_stm_read_esp.append([makePin('C', 1), 12, 0])
list_stm_read_esp.append([makePin('C', 2), 13, 0])
list_stm_read_esp.append([makePin('C', 3), 14, 0])
list_stm_read_esp.append([makePin('F', 0), 21, 0])
list_stm_read_esp.append([makePin('G', 11), 35, 0])
list_stm_read_esp.append([makePin('G', 10), 36, 0])
list_stm_read_esp.append([makePin('G', 9), 37, 0])
list_stm_read_esp.append([makePin('G', 8), 38, 0])
list_stm_read_esp.append([makePin('G', 7), 39, 0])
list_stm_read_esp.append([makePin('G', 6), 40, 0])
list_stm_read_esp.append([makePin('G', 5), 41, 0])
list_stm_read_esp.append([makePin('G', 4), 42, 0])
list_stm_read_esp.append([makePin('G', 15), 47, 0])
list_stm_read_esp.append([makePin('G', 14), 48, 0])



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


#START  
boardSTM.disable_all_reporting()
boardESP.disable_all_reporting()
'''
#read stm pins by ESP
for esp_read_stm in list_stm_read_esp:
    boardSTM.set_pin_mode_digital_output(esp_read_stm[0])
    digital_in(boardESP, esp_read_stm[1])
    boardSTM.digital_write(esp_read_stm[0], 1)
    time.sleep(0.1)
    boardSTM.digital_write(esp_read_stm[0], 0)
    time.sleep(0.1)
    print('existuju')
'''    

boardSTM.disable_all_reporting()
boardESP.disable_all_reporting()

#read EPS pins by STM
for stm_read_esp in list_stm_read_esp:
    boardESP.set_pin_mode_digital_output(stm_read_esp[1])
    digital_in(boardSTM, stm_read_esp[0])
    boardESP.digital_write(stm_read_esp[1], 1)
    time.sleep(0.1)
    stm_read_esp[2] = global_value
    boardESP.digital_write(stm_read_esp[1], 0)
    time.sleep(0.1)
    print(stm_read_esp)

for stm_read_esp in list_stm_read_esp:
    print(stm_read_esp)