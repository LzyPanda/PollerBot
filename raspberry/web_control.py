__author__ = 'CroMarmot-OSX'
#20140413
#TODO: left-forward e.g. 25/25 or 50/50

import RPi.GPIO as GPIO
import signal
import sys

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

def forward():
    first.start(50)
    second.start(0)
    third.start(0)
    fourth.start(50)
    print "Geradeaus vorwaerts"
    return

def reverse():
    first.start(0)
    second.start(50)
    third.start(50)
    fourth.start(0)
    print "Geradeaus rueckwaerts"
    return

def left():
    first.start(0)
    second.start(50)
    third.start(0)
    fourth.start(50)
    print "Drehung nach Links"
    return

def right():
    first.start(50)
    second.start(0)
    third.start(50)
    fourth.start(0)
    print "Drehung nach rechts"
    return

def stop():
    first.start(0)
    second.start(0)
    third.start(0)
    fourth.start(0)
    print "Stop"
    return

controlarg = sys.argv[0]

if controlarg == 'forward':
    forward()
elif controlarg == 'reverse':
    reverse()
elif controlarg == 'left':
    left()
elif controlarg == 'right':
    right()
elif controlarg == 'stop':
    stop()
