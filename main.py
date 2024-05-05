import sys
import time
from telemetrix import telemetrix
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter import simpledialog
import os
import subprocess
import subprocess
import serial.tools.list_ports

boardESP = telemetrix.Telemetrix(arduino_instance_id=2)
boardSTM = telemetrix.Telemetrix(arduino_instance_id=1)

    #makes a stm pin number
def makePin(portName, pinNumber):
    return (ord(portName) - ord("A")) * 16 + pinNumber 

    #pins for stm to read from esp
list_esp_pins = [] # stm pin, coresponding esp pin, read value

#GND
list_esp_pins.append([makePin('F', 13), 23, 0, (374, 98)])
list_esp_pins.append([makePin('F', 14), 22, 0, (374, 119)])
#list_esp_pins.append([makePin('F', 15), 1, 0, (374, 140)])
#list_esp_pins.append([makePin('E', 0), 3, 0, (374, 161)])
list_esp_pins.append([makePin('E', 1), 21, 0, (374, 182)])
#GND                                                     203
list_esp_pins.append([makePin('E', 2), 19, 0, (374, 224)])
list_esp_pins.append([makePin('E', 3), 18, 0, (374, 245)])
list_esp_pins.append([makePin('E', 4), 5, 0, (374, 266)])
list_esp_pins.append([makePin('E', 5), 17, 0, (374, 287)])
list_esp_pins.append([makePin('E', 6), 16, 0, (374, 308)])
list_esp_pins.append([makePin('E', 7), 4, 0, (374, 329)])
list_esp_pins.append([makePin('E', 8), 0, 0, (374, 350)])
list_esp_pins.append([makePin('E', 9), 2, 0, (374, 371)])
list_esp_pins.append([makePin('E', 10), 15, 0, (374, 392)])
#list_esp_pins.append([makePin('E', 11), 8, 0]) pin shared with the flash memory
#list_esp_pins.append([makePin('E', 12), 7, 0])
#list_esp_pins.append([makePin('E', 13), 6, 0])

#3v3
#EN
#list_esp_pins.append([makePin('C', 10), 36, 0]) these 4 input only
#list_esp_pins.append([makePin('C', 11), 39, 0])
#list_esp_pins.append([makePin('C', 12), 34, 0])
#list_esp_pins.append([makePin('C', 13), 35, 0])
list_esp_pins.append([makePin('C', 14), 32, 0, (105, 200)])
list_esp_pins.append([makePin('C', 15), 33, 0, (105, 221)])
list_esp_pins.append([makePin('D', 0), 25, 0, (105, 242)])
list_esp_pins.append([makePin('D', 1), 26, 0, (105, 263)])
list_esp_pins.append([makePin('D', 2), 27, 0, (105, 284)])
list_esp_pins.append([makePin('D', 3), 14, 0, (105, 305)])
list_esp_pins.append([makePin('D', 4), 12, 0, (105, 326)])
#GND
list_esp_pins.append([makePin('D', 5), 13, 0, (105, 368)])
#list_esp_pins.append([makePin('D', 6), 9, 0]) pin shared with the flash memory
#list_esp_pins.append([makePin('D', 7), 10, 0])
#list_esp_pins.append([makePin('D', 8), 11, 0])

#####################################################################
list_esp_s3_pins = [] # stm pin, coresponding esp pin, read value

#3v3
#3v3
#RST
list_esp_s3_pins.append([makePin('B', 3), 4, 0,   (120, 165)]) # o 26
list_esp_s3_pins.append([makePin('B', 4), 5, 0,   (120, 190)])
list_esp_s3_pins.append([makePin('B', 5), 6, 0,   (120, 215)])
list_esp_s3_pins.append([makePin('B', 6), 7, 0,   (120, 240)])
# 4 Serial pins
#
#
#
list_esp_s3_pins.append([makePin('B', 11), 8, 0,  (120, 365)])
# 2 strapping pins
#
list_esp_s3_pins.append([makePin('B', 14), 9, 0,  (120, 440)])
list_esp_s3_pins.append([makePin('B', 15), 10, 0, (120, 465)])
list_esp_s3_pins.append([makePin('C', 0), 11, 0,  (120, 490)])
list_esp_s3_pins.append([makePin('C', 1), 12, 0,  (120, 515)])
list_esp_s3_pins.append([makePin('C', 2), 13, 0,  (120, 540)])
list_esp_s3_pins.append([makePin('C', 3), 14, 0,  (120, 565)])
#5V0
#GND

#GND
# 2 Serial pins
#
list_esp_s3_pins.append([makePin('G', 2), 1, 0,   (390, 165)])
list_esp_s3_pins.append([makePin('G', 3), 2, 0,   (390, 190)])
list_esp_s3_pins.append([makePin('G', 4), 42, 0,  (390, 215)])
list_esp_s3_pins.append([makePin('G', 5), 41, 0,  (390, 240)])
list_esp_s3_pins.append([makePin('G', 6), 40, 0,  (390, 265)])
list_esp_s3_pins.append([makePin('G', 7), 39, 0,  (390, 290)])
list_esp_s3_pins.append([makePin('G', 8), 38, 0,  (390, 315)])
list_esp_s3_pins.append([makePin('G', 9), 37, 0,  (390, 340)])
list_esp_s3_pins.append([makePin('G', 10), 36, 0, (390, 365)])
list_esp_s3_pins.append([makePin('G', 11), 35, 0, (390, 390)])
# 2 strapping pins
#
list_esp_s3_pins.append([makePin('G', 14), 48, 0, (390, 465)])
list_esp_s3_pins.append([makePin('G', 15), 47, 0, (390, 490)])
list_esp_s3_pins.append([makePin('F', 0), 21, 0,  (390, 515)])
# USB
# USB
# GND
# GND

global_value = 0

 # Initialize selected_board variable
selected_board = None

def ask_which_board():
    # Function to handle button clicks
    def button_click(board_name):
        global selected_board
        selected_board = board_name
        root.destroy()  # Close the pop-up window
        
    # Create the main window
    root = tk.Tk()

    # Set window title and size
    root.title("Board Selection")
    root.geometry("300x100")

    # Create buttons for each board
    button_board1 = tk.Button(root, text="ESP32-devkit", command=lambda: button_click("ESP32-devkit"))
    button_board1.pack(side=tk.LEFT, padx=10)

    button_board2 = tk.Button(root, text="ESP32-S3", command=lambda: button_click("ESP32-S3"))
    button_board2.pack(side=tk.LEFT, padx=10)


    # Display the window
    root.mainloop()

    print('selected board:', selected_board)

def graphic_output(board):
        # Load the image of the board
    if board == list_esp_pins:
        board_image = Image.open('esp.png')
    else:
        board_image = Image.open('esp-s3.png')
        # Create a figure and axis for plotting
    fig, ax = plt.subplots()

        # Display the board image
    ax.imshow(board_image)
        # Plot the tested pins on the image
    for pin in board:
        if pin[2] == 1:
            ax.text(pin[3][0], pin[3][1], pin[1], color='lime', fontsize=12, ha='center', va='center')
        else:
            ax.text(pin[3][0], pin[3][1], f'pin: {pin[1]} is broken', color='red', fontsize=12, ha='center', va='center')
            

    # Hide the axis
    ax.axis('off')

    # Show the plot
    plt.show()


# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3

def the_callback(data):
    global global_value
    global_value = data[CB_VALUE]
    
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[CB_TIME]))
    print(f'Pin Mode: {data[CB_PIN_MODE]} Pin: {data[CB_PIN]} Value: {data[CB_VALUE]} Time Stamp: {date}')


def digital_in(my_board, pin):
    # set the pin mode
    my_board.enable_digital_reporting(pin)
    my_board.set_pin_mode_digital_input(pin, the_callback)
    
    
######################################################################################
#               START
######################################################################################

ask_which_board()

boardSTM.disable_all_reporting()
boardESP.disable_all_reporting()

if selected_board == "ESP32-devkit":
    for items in list_esp_pins:
        boardESP.set_pin_mode_digital_output(items[1])
        digital_in(boardSTM, items[0])
        boardESP.digital_write(items[1], 1)
        time.sleep(0.1)
        items[2] = global_value
        boardESP.digital_write(items[1], 0)
        time.sleep(0.1)
        print(items)
    graphic_output(list_esp_pins)
if selected_board == "ESP32-S3":
    for items in list_esp_s3_pins:
        boardESP.set_pin_mode_digital_output(items[1])
        digital_in(boardSTM, items[0])
        boardESP.digital_write(items[1], 1)
        time.sleep(0.1)
        items[2] = global_value
        boardESP.digital_write(items[1], 0)
        time.sleep(0.1)
        print(items)
    graphic_output(list_esp_s3_pins)
