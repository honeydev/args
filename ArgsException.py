
class ArgsException(Exception):
    #why \0 ???
    errorArgumentId = "\0"
    errorParametr = "TILT"
    errorCode = "OK"
    
    def __init__(self, message: str, errors) -> None:
        super().__init__(message)