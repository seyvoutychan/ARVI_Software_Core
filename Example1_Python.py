import serial
import time

arduino = serial.Serial('COM4', 115200, timeout=.1)

def stringFunction():
    data = arduino.readline().decode('ascii')
    if data:
        print(data)

while True:
    stringFunction()
    time.sleep(1)


