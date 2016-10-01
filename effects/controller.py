#!/ usr/bin/python

# from here, we call to the different Effects
# should only need to import controller into the game loop

from abc import ABCMeta, abstractmethod
from threading import Thread
from time import sleep
import opc

class Effect(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        if global.server is None:
            kwargs.setdefault('server', '127.0.0.1:7890')
        else:
            kwargs.setdefault('server', global.server)
        kwargs.setdefault('name', 'unnamedEffect')
        kwargs.setdefault('runcount', 0)
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])
    
    #name getter/setter
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    #server geter/setter
    @property
    def server(self):
        if global.server is None:
            return self.__server
        else:
            return global.server
    @server.setter
    def server(self, server):
        self.__server = server
    
    #runcount getter/setter
    @property
    def runcount(self):
        return self.__runcount
    @runcount.setter
    def runcount(self, runcount):
        self.__runcount = runcount

    @abstractmethod
    def do_effect(self): pass
    #this method should be overridden and is the main 'effect loop'

    def start(self):
        #initiate the effect loop in new thread