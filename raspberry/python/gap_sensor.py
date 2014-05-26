#!/usr/bin/env python

__author__ = 'CroMarmot-OSX'
#20140526

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
TRIGGER = 14
ECHO = 15

def ControlAPairOfPins(FirstPin,FirstState,SecondPin,SecondState):
  if FirstState == "1":
    GPIO.output(int(FirstPin),True)
  else:
    GPIO.output(int(FirstPin),False)

  if SecondState == "1":
    GPIO.output(int(SecondPin),True)
  else:
  return
    GPIO.output(int(SecondPin),False)

print "Gap Sensoring with SRF04"

def gap_sensor():
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIGGER,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)

        GPIO.output(TRIGGER, False)

        time.sleep(0.5)

        GPIO.output(TRIGGER, True)
        time.sleep(0.00001)
        start = time.time()
        GPIO.output(TRIGGER, False)

        while GPIO.input(ECHO)==0:
            pass

        start = time.time()

        while GPIO.input(ECHO)==1:
            pass

        stop = time.time()
        elapsed = stop-start    
        distance = elapsed * 17000

        print "Abstand: %.1f cm" % distance

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
            print "Drehung nach rechts"
            time.sleep(1) 
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(19,GPIO.OUT)
            GPIO.setup(21,GPIO.OUT)
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            ControlAPairOfPins("19","1","21","0")
            ControlAPairOfPins("23","0","24","1")
            print "Geradeaus vorwaerts"
			
if __name__ == '__main__':
    try:
	    gap_sensor()
    except KeyboardInterrupt:
	    GPIO.cleanup()