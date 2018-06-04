from abc import ABCMeta, abstractmethod

class ArgumentMarshaler:
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def set(currentArgument) -> None: pass

    @abstractmethod
    def get(): pass