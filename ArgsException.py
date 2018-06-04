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
        errorArgumentId: str,
        errorParameter: str,
        ) -> None:
        super().__init__()
        self.errorCode = errorCode
        self.errorParameter = errorParameter
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
            return "Argument -{} unexpected.".format(self.errorArgumentId)
        elif (self.errorCode == ErrorCode.MISSING_STRING):
            return "Could not find string parameter for -{}.".format(self.errorArgumentId)
        elif (self.errorCode == ErrorCode.INVALID_INTEGER):
            return "Argument -{} expects an integer but was '{}'.".format(self.errorArgumentId, self.errorParameter)
        elif (self.errorCode == ErrorCode.MISSING_INTEGER):
            return "Could not find integer parameter for -{}.".format(self.errorArgumentId)
        elif (self.errorCode == ErrorCode.INVALID_DOUBLE):
            return "Argument -{} expects a double but was '{}'.".format(self.errorArgumentId, self.errorParameter)
        elif (self.errorCode == ErrorCode.MISSING_DOUBLE):
            return "Could not find double parameter for -{}.".format(self.errorArgumentId)
        else:
            return ""
