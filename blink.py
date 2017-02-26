#!/usr/bin/python
import time

from gpio_96boards import GPIO

GPIO_A = GPIO.gpio_id('GPIO_A')
pins = (
    (GPIO_A, 'out'),
)
GPIO_B = GPIO.gpio_id('GPIO_B')
pins = (
    (GPIO_B, 'in'),
)


def blink(gpio):
    gpio.digital_write(GPIO_A, GPIO.HIGH)
    time.sleep(1)
    gpio.digital_write(GPIO_A, GPIO.LOW)
    time.sleep(1)
    alto = gpio.digital_read(GPIO_B)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Blink LED on GPIO A (pin 23)')
    args = parser.parse_args()

    with GPIO(pins) as gpio:
        blink(gpio)
