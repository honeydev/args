from enum import Enum

class ErrorCode(Enum):

    OK = None
    INVALID_FORMAT = None
    UNEXPECTED_ARGUMENT = None
    INVALID_ARGUMENT_NAME = None
    MISSING_STRING = None
    MISSING_INTEGER = None
    INVALID_INTEGER = None
    MISSING_DOUBLE = None
    INVALID_DOUBLE = None