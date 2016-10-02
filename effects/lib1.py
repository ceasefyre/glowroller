import controller
import time

class chase(controller.effect):
    def __init__(self, **kwargs):
        super(chase,self).__init__(**kwargs)

    def do_effect(self, iterations):
        i = iterations
        
        i += 1
        
        numLEDs = 64
        while super(chase, self).running:
            while i>0:
                i -= 1
                print "running effect " + self.name + " for iteration# " + i
                for n in range(numLEDs):
                    pixels = [ (0,0,0) ] * numLEDs
                    pixels[n] = (255, 255, 255)
                    super(chase, self).client.put_pixels(pixels)
                    time.sleep(0.01)