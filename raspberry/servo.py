__author__ = 'CroMarmot'

import RPi.GPIO as GPIO

import time
import signal

from pizypwm import *

def endProcess(signalnum = None, handler = None):
    first.stop()
    second.stop()
    third.stop()
    fourth.stop()

    GPIO.cleanup()
    exit(0)

signal.signal(signal.SIGTERM, endProcess)
signal.signal(signal.SIGINT, endProcess)

first = PiZyPwm(20000, 19, GPIO.BOARD)
second = PiZyPwm(20000, 21, GPIO.BOARD)
third = PiZyPwm(20000, 23, GPIO.BOARD)
fourth = PiZyPwm(20000, 24, GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

while True:
    
    first.start(50)
    second.start(0)
    third.start(50)
    fourth.start(0)
    print "Drehung nach rechts"
    time.sleep(1)

    first.start(0)
    second.start(0)
    third.start(0)
    fourth.start(0)
    print "Stop"
    time.sleep(1)
    
    first.start(0)
    second.start(50)
    third.start(0)
    fourth.start(50)
    print "Drehung nach Links"
    time.sleep(1)

    first.start(0)
    second.start(0)
    third.start(0)
    fourth.start(0)
    print "Stop"
    time.sleep(1)

    first.start(50)
    second.start(0)
    third.start(0)
    fourth.start(50)
    print "Geradeaus vorwaerts"
    time.sleep(1)
    
    first.start(0)
    second.start(0)
    third.start(0)
    fourth.start(0)
    print "Stop"
    time.sleep(1)

    first.start(0)
    second.start(50)
    third.start(50)
    fourth.start(0)
    print "Geradeaus rueckwaerts"
    time.sleep(1)

    first.start(0)
    second.start(0)
    third.start(0)
    fourth.start(0)
    print "Stop"
    time.sleep(1)