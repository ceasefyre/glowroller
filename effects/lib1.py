import controller
import time

class chase(controller.effect):
    def __init__(self, **kwargs):
        super(chase,self).__init__(**kwargs)

    def do_effect(self, iterations):
        i = iterations
        over = False
        numLEDs = 64
        while self.running and not over:
            while i>0:
                i -= 1
                print "running effect " + self.name + " for iteration# " + str(i)
                for n in range(numLEDs):
                    pixels = [ (0,0,0) ] * numLEDs
                    pixels[n] = (255, 255, 255)
                    self.client.put_pixels(pixels)
                    time.sleep(0.01)
                pixels[numLEDs - 1] = (0,0,0)
                self.client.put_pixels(pixels)
                if not self.running:
                    return
                if i < 0:
                    i = 0
            over = True #non-release once finished needed an escape