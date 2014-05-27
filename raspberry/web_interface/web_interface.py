#!/usr/bin/env python

__author__ = 'Simon Buttke'
__copyright__ = 'Copyright 2014, Studienarbeit "Pollerbot"'
__credits__ = ["Sebastian Barz", "Simon Buttke", "Ferdinand Frank", "Sebastian Hantelmann", "Yusuf Peker"]
__version__ = '1.0'
__date__ =  '2014-05-26'
__email__ = 's110263@student.dhbw-mannheim.de'
__status__ = 'Production'

#import some python stuff
import signal
import multiprocessing
import time
#import webservice tornado
import tornado.web
import tornado.websocket
import tornado.ioloop
#import GPIO lib for gap and servo
import RPi.GPIO as GPIO
#import PWM control for servo
from pizypwm import *

def endProcess(signalnum = None, handler = None):
    first.stop()
    second.stop()
    third.stop()
    fourth.stop()

    GPIO.cleanup()
    exit(0)
	
GPIO.setwarnings(False)

signal.signal(signal.SIGTERM, endProcess)
signal.signal(signal.SIGINT, endProcess)

first = PiZyPwm(20000, 19, GPIO.BOARD)
second = PiZyPwm(20000, 21, GPIO.BOARD)
third = PiZyPwm(20000, 23, GPIO.BOARD)
fourth = PiZyPwm(20000, 24, GPIO.BOARD)
TRIGGER = 14
ECHO = 15
running = False

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

def ControlAPairOfPins(FirstPin,FirstState,SecondPin,SecondState):
    if FirstState == "1":
        GPIO.output(int(FirstPin),True)
    else:
        GPIO.output(int(FirstPin),False)

    if SecondState == "1":
        GPIO.output(int(SecondPin),True)
    else:
        GPIO.output(int(SecondPin),False)
    return

def autonomy(autoproc_pipe):
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIGGER,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)

        GPIO.output(TRIGGER, False)

        time.sleep(0.5)

        GPIO.output(TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, False)

        while GPIO.input(ECHO)==0:
            pass

        start_time = time.time()

        while GPIO.input(ECHO)==1:
            pass

        stop_time = time.time()
        elapsed = stop_time-start_time
        distance = elapsed * 17000

        if distance < 20:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(19,GPIO.OUT)
            GPIO.setup(21,GPIO.OUT)
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            ControlAPairOfPins("19","0","21","0")
            ControlAPairOfPins("23","0","24","0")
            print "Stop"
            time.sleep(1)

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(19,GPIO.OUT)
            GPIO.setup(21,GPIO.OUT)
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            ControlAPairOfPins("19","1","21","0")
            ControlAPairOfPins("23","1","24","0")
            time.sleep(1)
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(19,GPIO.OUT)
            GPIO.setup(21,GPIO.OUT)
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            ControlAPairOfPins("19","1","21","0")
            ControlAPairOfPins("23","0","24","1")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class JQueryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("jquery-2.1.0.min.js")

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.message = message
        if self.message == 'autonomy':
            if running == False:
                autoproc = multiprocessing.Process(target=autonomy,)
                autoproc.start()
                global running
                running = True
        elif self.message == 'control':
            if running == True:
                autoproc.terminate()
                global running
                running = False
        elif self.message == 'forwards':
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