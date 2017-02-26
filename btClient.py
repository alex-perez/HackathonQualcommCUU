
from bluetooth import *
import sys
import time
from gpio_96boards import GPIO
GPIO_A = GPIO.gpio_id('GPIO_A')
pins = ((GPIO_A, 'out'),)

def blink(gpio):
    gpio.digital_write(GPIO_A, GPIO.HIGH)
    time.sleep(1)
    gpio.digital_write(GPIO_A, GPIO.LOW)

if sys.version < '3':
    input = raw_input

addr = None

if len(sys.argv) < 2:
    print("no device specified.  Searching all nearby bluetooth devices for")
    print("the SampleServer service")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on %s" % addr)

# search for the SampleServer service
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

print("connected.  type stuff")
while True:
    data = input()
    if len(data) == 0: break
    sock.send(data)
    data = sock.recv(1024)
    print "received [%s]" % data
    if data  == "69":
        with GPIO(pins) as gpio:
            blink(gpio)
    
    

sock.close()
