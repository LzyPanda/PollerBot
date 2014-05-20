#!/usr/bin/env python

__author__ = 'CroMarmot-OSX'
#20140413
#TODO: left-forward e.g. 25/25 or 50/50

import RPi.GPIO as GPIO
import signal
#import sys

from flask import Flask, render_template

from pizypwm import *

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('/var/www/index.html')

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

@app.route('/forward/')
def forward():
    first.start(50)
    second.start(0)
    third.start(0)
    fourth.start(50)
#    print "Geradeaus vorwaerts"
    return

@app.route('/reverse/')
def reverse():
    first.start(0)
    second.start(50)
    third.start(50)
    fourth.start(0)
#    print "Geradeaus rueckwaerts"
    return

@app.route('/link/')
def left():
    first.start(0)
    second.start(50)
    third.start(0)
    fourth.start(50)
#    print "Drehung nach Links"
    return

@app.route('/right/')
def right():
    first.start(50)
    second.start(0)
    third.start(50)
    fourth.start(0)
#    print "Drehung nach rechts"
    return

@app.route('/stop/')
def stop():
    first.start(0)
    second.start(0)
    third.start(0)
    fourth.start(0)
    print "Stop"
    return

if __name__ == '__main__':
  app.run()