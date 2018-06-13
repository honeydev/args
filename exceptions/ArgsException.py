from ErrorCode import ErrorCode

class ArgsException(Exception):

    ErrorCode = ErrorCode
    
    def __init__(
        self, 
        errorCode: ErrorCode = ErrorCode.OK,
        errorArgumentId: str = "\0",
        errorParameter: str = "TILT",
        ) -> None:
        super().__init__()
        self.errorCode = errorCode
        self.errorArgumentId = errorArgumentId
        self.errorParameter = errorParameter

    def getErrorArgumentId(self) -> str:
        return self.errorArgumentId

    def setErrorArgumentId(self, errorArgumentId: str) -> None:
        self.errorArgumentId = errorArgumentId

    def getErrorParameter(self) -> str:
        return self.errorParameter

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
