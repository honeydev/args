from .ArgumentMarshaler import ArgumentMarshaler

class BooleanArgumentMarshaler(ArgumentMarshaler):
        
    booleanValue = False

    def set(self, argIterator):
        self.booleanValue = True

    def get(self) -> bool:
        return self.booleanValue
