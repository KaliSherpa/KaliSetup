#!/usr/bin/python3

import RPi.GPIO as GPIO

def g(Pin, value):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Pin, GPIO.OUT)
    GPIO.output(Pin, bool(value))
    
exitCode = False
while True:
    try:
        while True:
            x = input('GPIO->')
            Pin = int(x.split()[0])
            value = bool(int(x.split()[1]))
            if x == 'cleanup':
                GPIO.cleanup()
            elif x == 'exit':
                exitCode = True
                exit()
            else:
                g(Pin, value)
    except:
        print('[An Error Occured]')
        if exitCode:
            exit()
    finally:
        GPIO.cleanup()
