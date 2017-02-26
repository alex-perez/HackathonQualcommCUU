#! /usr/bin/python

import serial
from time import sleep
bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)

count = None
while count == None:
    try:
        count = raw_input("please enter the number of times to blink the ")
    except:
        pass
        bluetoothSerial.write(str(count))
        print bluetoothSerial.readline()
