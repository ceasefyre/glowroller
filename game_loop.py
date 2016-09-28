#!/ usr/bin/python

# main loop to control the game

import RPi.GPIO as GPIO
import time
import effects_controller as fx

GPIO.setmode(GPIO.BCM)

#Assign the buttons to GPIO pins
#NOTE: do NOT duplicate pins across buttons
btn1 = 17
btn2 = 18

#set the callbacks for the interrupts
options = {
    btn1 : 
}

running = True;

GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def tst_callback(channel):
    print "Button Press (Falling Switch) detected on channel " + str(channel)


GPIO.add_event_detect(btn1, GPIO.FALLING, callback=tst_callback, bouncetime=300)
GPIO.add_event_detect(btn2, GPIO.FALLING, callback=tst_callback, bouncetime=300)

try:
    while(running):
        #main loop hapenning here, with event interrupts defined above
        time.sleep(.01)

except KeyboardInterrupt:
    GPIO.cleanup()  #Cleaning up when Ctrl-C
GPIO.cleanup()      #GPIO cleanup on normal exit