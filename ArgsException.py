from ErrorCode import ErrorCode

class ArgsException(Exception):
    #why \0 ???
    errorArgumentId = "\0"
    errorParameter = "TILT"
    errorCode = ErrorCode.OK
    ErrorCode = ErrorCode
    
    def __init__(
        self, 
        errorCode: ErrorCode,
        errorParameter: str,
        errorArgumentId: str
        ) -> None:
        super().__init__()
        self.errorCode = errorCode
        self.errorParametr = errorParameter
        self.errorArgumentId = errorArgumentId

    def getErrorArgumentId(self) -> str:
        return self.errorArgumentId

    def setErrorArgumentId(self, errorArgumentId: str) -> None:
        self.errorArgumentId = errorArgumentId

    def getErrorParameter(self) -> str:
        return errorParameter

    def setErrorParameter(self, errorParameter: str) -> None:
        self.errorParameter = errorParameter

    def getErrorCode(self) -> ErrorCode:
        return self.errorCode

    def setErrorCode(self, errorCode: ErrorCode) -> None:
        self.errorCode = errorCode
    '''
    raise Exception
    '''
    def errorMessage(self) -> str:
        if (self.errorCode == ErrorCode.OK):
            raise Exception("TILT: Should not get here.")
        elif (self.errorCode == ErrorCode.UNEXPECTED_ARGUMENT):
            return "Argument -" + self.errorParameter + " unexpected. " + self.errorArgumentId
        else:
            return ""

