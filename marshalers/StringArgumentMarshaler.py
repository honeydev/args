from .ArgumentMarshaler import ArgumentMarshaler
from ArgsException import ArgsException

class StringArgumentMarshaler(ArgumentMarshaler):

    def __init__(self):
        self.stringValue = ""
    '''
    raise ArgsException
    '''
    def set(self, argIterator) -> None:
        try:
            self.stringValue = next(argIterator)
        except StopIteration:
            raise ArgsException(ArgsException.ErrorCode.MISSING_STRING, None, None)
            
    def get(self) -> None:
        return self.stringValue