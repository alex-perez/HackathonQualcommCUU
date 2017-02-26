import random
import sys
import time
from Adafruit_IO import *

ADAFRUIT_IO_KEY      = 'c71578bc27d14943ad226e958d3bf25b'
ADAFRUIT_IO_USERNAME = 'homeero'

aio = Client(ADAFRUIT_IO_KEY)
feed = aio.feeds('status')
print(feed)
print feed.last_value
