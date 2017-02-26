import time
from Adafruit_IO import Client
from gpio_96boards import GPIO

GPIO_A = GPIO.gpio_id('GPIO_A')
pins = (
        (GPIO_A, 'out'),
)

def blink(gpio):
    gpio.digital_write(GPIO_A,GPIO.HIGH)
    time.sleep(1)
    gpio.digital_write(GPIO_A,GPIO.LOW)
    time.sleep(1)

ADAFRUIT_IO_KEY = 'c71578bc27d14943ad226e958d3bf25b'

aio = Client(ADAFRUIT_IO_KEY)

data = aio.receive('Status')
print('Alert! {0}'.format(data.value))
if data.value == 'Call for help':
    with GPIO(pins) as gpio:
        blink(gpio)
        blink(gpio)
