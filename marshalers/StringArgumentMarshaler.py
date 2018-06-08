from .ArgumentMarshaler import ArgumentMarshaler
from ..ArgsException import ArgsException


class StringArgumentMarshaler(ArgumentMarshaler):

    stringValue = ""

    def set(self, argIterator) -> None:
        self.stringValue = next(argIterator)

    def get(self) -> None:
        return self.stringValue