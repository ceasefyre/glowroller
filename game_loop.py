#!/ usr/bin/python

# main loop to control the game

import RPi.GPIO as GPIO
import time
import effects_controller as fx

GPIO.setmode(GPIO.BCM)

#Assign the buttons to GPIO pins
#NOTE: do NOT duplicate pins across buttons
btn_pins = dict(
    'btn1' = 17,
    'btn2' = 18,
    'btn3' = 27,
    'btn4' = 23
)

#button bounceback time for callback triggers
btn_bounce = 300

#
running = True

def cb_test(channel):
    print "Button Press (Falling Switch) detected on channel " + str(channel)

def cb_cease_polling(channel):
    tst_callback(channel)
    running = False

#set the callbacks for the interrupts
btn_cb = {
    btn_pins['btn1'].value : cb_test,
    btn_pins['btn2'].value : cb_test,
    btn_pins['btn3'].value : cb_test,
    btn_pins['btn4'].value : cb_cease_polling
}

#iterate the pins dict and set them up with their callbacks
for button in btn_pins
    GPIO.setup(btn_pins[button], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_even_detect(btn_pins[button], GPIO.FALLING, callback=btn_cb[btn_pins[button]], bouncetime=btn_bounce)

try:
    while(running):
        #main loop hapenning here, with event interrupts defined above
        time.sleep(.01)

except KeyboardInterrupt:
    GPIO.cleanup()  #Cleaning up when Ctrl-C
GPIO.cleanup()      #GPIO cleanup on normal exit