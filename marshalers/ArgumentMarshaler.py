from abc import ABCMeta, abstractmethod

class ArgumentMarshaler:
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, argIterator) -> None: pass

    @abstractmethod
    def get(self): pass