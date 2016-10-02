#!/ usr/bin/python

# from here, we call to the different Effects
# should only need to import controller into the game loop

from abc import ABCMeta, abstractmethod
from threading import Thread
from time import sleep
import utils.opc

class effect(object):
    __metaclass__ = ABCMeta
    
    def threadLoop(self):
        self.do_effect(self.__iterations)
    
    def __init__(self, **kwargs):
        kwargs.setdefault('server', '127.0.0.1:7890')
        kwargs.setdefault('name', 'unnamedEffect')
        kwargs.setdefault('iterations', 0) #0 being infinite
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])
        self.__thread = Thread(name=self.name, target=threadLoop)
    
    @abstractmethod
    def do_effect(self, iterations): pass
    #this method should be overridden and is the main 'effect loop'
    #connecting to the host and thread control is taken care of by the rest of the class

    def start(self):
        #initiate the effect loop in new thread
        self.__running = True
        self.__thread.start

    def stop(self):
        self.__running = False
    
    def connectOPC(self):
        self.__client = opc.Client(self.__server)
        while not self.__client.can_connect():
            pass
