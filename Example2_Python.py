import serial
import time

#define serial port
arduino = serial.Serial('COM4', 115200, timeout=.1)

def ledSwitch():
    print("To turn on/off an led:")
    print(" Type 1 to turn on")
    print(" Type 0 to turn off")
    userInput = input("Please enter a number: ")

    #check if user chose on(1)/off(0)
    if userInput == "1":
        print ("you type ",userInput)
        print ("The LED light is on")
        arduino.write('1'.encode())
    elif userInput == '0':
        print ("you type ",userInput)
        print ("The LED light is off")
        arduino.write('0'.encode())
    else:
        print("Please try again")
        
    print("=================================")
    ledSwitch()

time.sleep(1)

ledSwitch()
