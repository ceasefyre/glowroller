#!/ usr/bin/python

# main loop to control the game

import RPi.GPIO as GPIO
import time
import effects.controller
import effects.lib1 as fx

GPIO.setmode(GPIO.BCM)

#Assign the buttons to GPIO pins
#NOTE: do NOT duplicate pins across buttons
btn_pins = {
    'btn1': 17,
    'btn2': 22,
    'btn3': 27,
    'btn4': 4,
    'btn5': 21
}

#button bounceback time for callback triggers
btn_bounce = 300
#Global variable for the client
server = 'da3-lightpi.local:7890'

#Flag to indicate keep main loop going
running = True

def cb_test(channel):
    print "Button Press (Falling Switch) detected on channel "+str(channel)

def cb_testChase(channel):
    print "Creating class of chase"
    fx_chase = fx.chase(iterations=2, server=server, name="chase")
    print "Starting loop"
    fx_chase.start()


def cb_cease_polling(channel):
    cb_test(channel)
    print "Ceasing main loop."
    global running
    running = False

#set the callbacks for the interrupts
btn_cb = {
    btn_pins['btn1']: cb_test,
    btn_pins['btn2']: cb_test,
    btn_pins['btn3']: cb_test,
    btn_pins['btn4']: cb_test,
    btn_pins['btn5']: cb_cease_polling
}

#iterate the pins dict and set them up with their callbacks
for btn in btn_pins:
    GPIO.setup(btn_pins[btn], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(btn_pins[btn], GPIO.FALLING, callback=btn_cb[btn_pins[btn]], bouncetime=btn_bounce)

try:
    while(running):
        #main loop hapenning here, with event interrupts defined above
        time.sleep(.01)

except KeyboardInterrupt:
    GPIO.cleanup()  #Cleaning up when Ctrl-C
GPIO.cleanup()      #GPIO cleanup on normal exit