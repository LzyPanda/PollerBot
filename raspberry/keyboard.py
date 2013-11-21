__author__ = 'CroMarmot'

#These are the keyboard mappings
#w = Go forward
#s = Go back
#a= Go left
#d = Go right
#Space = Stop going forward or back

#Get the GPIO module
import RPi.GPIO as GPIO

#Get the time module
import time

#A routine to control a pair of pins
def ControlAPairOfPins(FirstPin,FirstState,SecondPin,SecondState):
    print "Controlling them pins"
    if FirstState == "1":
        GPIO.output(int(FirstPin),True)
    else:
        GPIO.output(int(FirstPin),False)

    if SecondState == "1":
        GPIO.output(int(SecondPin),True)
    else:
        GPIO.output(int(SecondPin),False)
    #Just return
    return

####Main body of code

#Get rid of warnings
GPIO.setwarnings(False)

#Set the GPIO mode
GPIO.setmode(GPIO.BOARD)
#Set the pins to be outputs
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

try:
    print "Controls are w, a, s, d and Space!\n"
    while True:
        MyChar = raw_input("Press a character:")
        print "You pressed: " + MyChar
        if MyChar == "w":
            ControlAPairOfPins("19","1","21","0")
            ControlAPairOfPins("23","0","24","1")
            print "Forward"
        elif MyChar == "s":
            ControlAPairOfPins("19","0","21","1")
            ControlAPairOfPins("23","1","24","0")
            print ("Back")
        elif MyChar == "a":
            ControlAPairOfPins("19","0","21","1")
            ControlAPairOfPins("23","0","24","1")
            print "Left"
        elif MyChar == "d":
            ControlAPairOfPins("19","1","21","0")
            ControlAPairOfPins("23","1","24","0")
            print "Right"
        elif MyChar == " ":
            ControlAPairOfPins("19","0","21","0")
            ControlAPairOfPins("23","0","24","0")
            print "Stop"
        else:
            print "Not a command"
except:
    print "Error"
    #Fill Keyboardinterrupt here!