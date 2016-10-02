import controller
import time

class chase(controller.effect):
    def __init__(self, **kwargs):
        super(self).__init__(kwargs)

    def do_effect(self, iterations):
        i = iterations
        i += 1

        numLEDs = 64
        while super(chase, self).__isRunning:
            while i>0:
                for n in range(numLEDs):
                    pixels = [ (0,0,0) ] * numLEDs
                    pixels[n] = (255, 255, 255)
                    super(chase, self).__client.put_pixels(pixels)
                    time.sleep(0.01)