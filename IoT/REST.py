import time
from Adafruit_IO import Client
from gpio_96boards import GPIO
from time import gmtime, strftime

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

while True:
    try:
        data = aio.receive_next('Status')
        ts = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print ts, ' ','Alert! {0}'.format(data.value)
        if data.value == 'Call for help':
            with GPIO(pins) as gpio:
                blink(gpio)
                blink(gpio)
    except Exception as e:
        pass

    time.sleep(10)
