from .ArgumentMarshaler import ArgumentMarshaler
from ArgsException import ArgsException

class IntegerArgumentMarshaler(ArgumentMarshaler):

    def __init__(self):
        self.intValue = 0
    '''
    raise ArgsException
    '''
    def set(self, argIterator) -> None:
        parametr = None
        try:
            parametr = next(argIterator)
            self.intValue = int(parametr)
        except StopIteration:
            raise ArgsException(ArgsException.ErrorCode.MISSING_INTEGER, None, parametr)
        except ValueError:
            raise ArgsException(ArgsException.ErrorCode.INVALID_INTEGER, None, parametr)

    def get(self) -> int:
        return self.intValue
