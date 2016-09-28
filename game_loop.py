# main loop to control the game

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

btn1 = 17
btn2 = 18

GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def tst_callback(channel):
    print "falling edge detected on channel " + str(channel)

GPIO.add_event_detect(btn1, GPIO.FALLING, callback=tst_callback, bouncetime=300)
GPIO.add_event_detect(btn2, GPIO.FALLING, callback=tst_callback, bouncetime=300)

running = true;

try:
    while(running):
        #main loop hapenning here, with event interrupts defined above


except KeyboardInterrupt:
    GPIO.cleanup()  #Cleaning up when Ctrl-C
GPIO.cleanup()      #GPIO cleanup on normal exit