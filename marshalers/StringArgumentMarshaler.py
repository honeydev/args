from .ArgumentMarshaler import ArgumentMarshaler

class StringArgumentMarshaler(ArgumentMarshaler):

    stringValue = ""

    def set(arg: str) -> None:
        self.stringValue = arg

    def get() -> None:
        return self.stringValue