from ArgumentMarshaler import ArgumentMarshaler

class BooleanArgumentMarshaler(ArgumentMarshaler):
        
    booleanValue = False

    def set(s: str):
        self.booleanValue = True

    def get() -> bool:
        self.booleanValue

