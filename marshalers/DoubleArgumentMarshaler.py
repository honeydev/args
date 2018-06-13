from .ArgumentMarshaler import ArgumentMarshaler
from ArgsException import ArgsException

class DoubleArgumentMarshaler(ArgumentMarshaler):
    
    def __init__(self):
        self.doubleValue = 0

    def set(self, argIterator) -> None:
        parametr = None
        try:
            parametr = next(argIterator)
            self.doubleValue = float(parametr)
        except StopIteration:
            raise ArgsException(ArgsException.ErrorCode.MISSING_DOUBLE, None, parametr)
        except ValueError:
            raise ArgsException(ArgsException.ErrorCode.INVALID_DOUBLE, None, parametr)

    def get(self) -> int:
        return self.doubleValue
