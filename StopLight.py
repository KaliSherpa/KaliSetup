#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

def g(LEDPin, value):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPin, GPIO.OUT)
    GPIO.output(LEDPin, bool(value))
    
value = True
g(20, 1)
    
def go():
    global value
    if not value == True:
        value = True
        g(22, 0)
        g(21, 1)
        sleep(1)
        g(21, 0)
        g(20, 1)

def stop():
    global value
    if not value == False:
        value = False
        g(20, 0)
        g(21, 1)
        sleep(1)
        g(21, 0)
        g(22, 1)

def wild():
    global value
    g(20, 0)
    g(21, 0)
    g(22, 0)
    for i in range(10):
        g(20, 1)
        sleep(0.05)
        g(20, 0)
        g(21, 1)
        sleep(0.05)
        g(21, 0)
        g(22, 1)
        sleep(0.05)
        g(22, 0)
    if value == True:
        g(20, 1)
    else:
        g(22, 1)
         
try:
    while True:
        x = input('Action: ')
        x = ''.join([i.lower() for i in str(x)])
        if x == 'go':
            go()
        elif x == 'stop':
            stop()
        else:
            wild()
except:
    GPIO.cleanup()
