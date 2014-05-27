#!/usr/bin/env python

__author__ = 'CroMarmot-OSX'
#20140512
#TODO: left-forward e.g. 25/25 or 50/50

import tornado.web
import tornado.websocket
import tornado.ioloop

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

def forwards():
    first.start(0)
    second.start(50)
    third.start(50)
    fourth.start(0)
    return "forwards"

def reverse():
    first.start(50)
    second.start(0)
    third.start(0)
    fourth.start(50)
    return "reverse"

def left():
    first.start(0)
    second.start(50)
    third.start(0)
    fourth.start(50)
    return "left"

def right():
    first.start(50)
    second.start(0)
    third.start(50)
    fourth.start(0)
    return "right"

def stop():
    first.start(0)
    second.start(0)
    third.start(0)
    fourth.start(0)
    return "stop"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class JQueryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("jquery-2.1.0.min.js")

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.message = message
        if self.message == 'forwards':
            action = forwards()
        elif self.message == 'reverse':
            action = reverse()
        elif self.message == 'left':
            action = left()
        elif self.message == 'right':
            action = right()
        elif self.message == 'stop':
            action = stop()

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/jquery", JQueryHandler),
    (r"/websocket", WebSocketHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
