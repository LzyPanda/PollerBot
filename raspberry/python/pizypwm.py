__author__ = 'CroMarmot'

import RPi.GPIO as GPIO
import threading
import time
 
class PiZyPwm(threading.Thread):
    def __init__(self, frequency, gpioPin, gpioScheme):
        self.baseTime = 1.0 / frequency
        self.maxCycle = 100.0
        self.sliceTime = self.baseTime / self.maxCycle
        self.gpioPin = gpioPin
        self.terminated = False
        self.toTerminate = False
        GPIO.setmode(gpioScheme)

    def start(self, dutyCycle):
        self.dutyCycle = dutyCycle
        GPIO.setup(self.gpioPin, GPIO.OUT)
        self.thread = threading.Thread(None, self.run, None, (), {})
        self.thread.start()

    def run(self):
        while self.toTerminate == False:
            if self.dutyCycle > 0:			
                GPIO.output(self.gpioPin, GPIO.HIGH)
                time.sleep(self.dutyCycle * self.sliceTime)
      
            if self.dutyCycle < self.maxCycle:
                GPIO.output(self.gpioPin, GPIO.LOW)
                time.sleep((self.maxCycle - self.dutyCycle) * self.sliceTime)

        self.terminated = True

    def changeDutyCycle(self, dutyCycle):
        self.dutyCycle = dutyCycle

    def changeFrequency(self, frequency):
        self.baseTime = 1.0 / frequency
        self.sliceTime = self.baseTime / self.maxCycle

    def stop(self):
        self.toTerminate = True
        while self.terminated == False:
            time.sleep(0.01)
  
        GPIO.output(self.gpioPin, GPIO.LOW)
        GPIO.setup(self.gpioPin, GPIO.IN)