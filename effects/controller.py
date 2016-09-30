#!/ usr/bin/python

# from here, we call to the different Effects
# should only need to import controller into the game loop

from abc import ABCMeta, abstractmethod
from threading import Thread
from time import sleep
import opc

class Effect(metaclass=ABCMeta):
    def __init__(self, name, nRepeats)
        self.name = name
        self.nRepeats = nRepeats
        self.client = opc.Client(global.server)
    
    def get_name(self):
        return self.name
    def get_isRepeated(self):
        return self.isRepeated
    
    @abstractmethod
    def do_effect(self): pass
    #this method should be overridden and is the main 'effect loop'

    def start(self):
        #initiate the effect loop in new thread