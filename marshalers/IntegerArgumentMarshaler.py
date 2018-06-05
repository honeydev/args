from .ArgumentMarshaler import ArgumentMarshaler
from ..ArgsException import ArgsException

class IntegerArgumentMarshaler(ArgumentMarshaler):

    intValue = 0

    def set(currentArgument: str):
        try:
            self.intValue = int(currentArgument)
        except ValueError as e:
            raise ArgsException()

    def get() -> int:
        return intValue
