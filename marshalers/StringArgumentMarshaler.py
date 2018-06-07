from .ArgumentMarshaler import ArgumentMarshaler

class StringArgumentMarshaler(ArgumentMarshaler):

    stringValue = ""

    def set(self, arg: str) -> None:
        self.stringValue = arg

    def get(self, ) -> None:
        return self.stringValue