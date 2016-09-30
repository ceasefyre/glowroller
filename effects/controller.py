#!/ usr/bin/python

# from here, we call to the different Effects
# should only need to import controller into the game loop

from abc import ABCMeta, abstractmethod
import opc

class Effect(metaclass=ABCMeta):
    self.name = name
    self.isRepeated = isRepeated
    self.client = opc.Client(global.server)
    
    def get_name(self):
        return self.name
    def get_isRepeated(self):
        return self.isRepeated
    
    @abstractmethod
    def do_effect(self): pass
    #this method should be overridden and is the main 'effect loop'

