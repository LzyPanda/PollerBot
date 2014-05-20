#!/usr/bin/python2

__author__ = 'CroMarmot-OSX'
#20140512
#TODO: left-forward e.g. 25/25 or 50/50

import tornado.web
import tornado.websocket
import tornado.ioloop

import RPi.GPIO as GPIO
import signal
import time
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

def forwards():
    first.start(0)
    second.start(100)
    third.start(100)
    fourth.start(0)
    return "reverse"

def reverse():
    first.start(100)
    second.start(0)
    third.start(0)
    fourth.start(100)
    return "forwards"

def left():
    first.start(0)
    second.start(100)
    third.start(0)
    fourth.start(100)
    return "left"

def right():
    first.start(100)
    second.start(0)
    third.start(100)
    fourth.start(0)
    return "right"

def stop():
    first.start(0)
    second.start(0)
    third.start(0)
    fourth.start(0)
    return "stop"

def drive(message):
    if message == 'forwards':
        forwards()
    elif message == 'reverse':
        reverse()
    elif message == 'left':
        left()
    elif message == 'right':
        right()
    elif message == 'stop':
        stop()
    elif True:
        print "Wrong Signal"
        endProcess()

while True:
    signal = sys.argv[1]
    print signal
    drive(signal)
    time.sleep(float(sys.argv[2]))
    endProcess()
