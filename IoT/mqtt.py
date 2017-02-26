import random
import sys
import time
from Adafruit_IO import MQTTClient
import requests

ADAFRUIT_IO_KEY      = 'c71578bc27d14943ad226e958d3bf25b'
ADAFRUIT_IO_USERNAME = 'homeero'

def connected(client):
    print 'Conectado al servidor!'
    client.subscribe('status')
    client.subscribe('location')

def disconnected(client):
    print 'Desconectado'
    sys.exit(1)

def message(client, feed_id, payload):
    print 'Feed {0} recieved a new value: {1}'.format(feed_id, payload)


client = MQTTClient('homeero','c71578bc27d14943ad226e958d3bf25b')
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.connect()
client.loop_blocking()

