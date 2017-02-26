 #!/usr/bin/env python

import time
import serial
import os

arduino = serial.Serial('/dev/rfcomm0', 115200)
print "Conecting"
time.sleep(0)
while 1:
    value = arduino.read()
    time.wait(0.5)
    print value
    mensaje = "Que sirva"
    arduino.write(mensaje)
    time.wait(0.5)
    mensaje = "2"
    arduino.write(mensaje)
