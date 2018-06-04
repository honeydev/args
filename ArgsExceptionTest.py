import unittest
from ArgsException import ArgsException

class ArgsExceptionTest(unittest.TestCase):
    '''
    raise Exception
    '''
    def testUnexpectedMessage(self):
        argsException = ArgsException(ArgsException.ErrorCode.UNEXPECTED_ARGUMENT, "x", None)
        self.assertEqual("Argument -x unexpected.", argsException.errorMessage())
    '''
    raise Exception
    '''
    def testMissingStringMessage(self):
        argsException = ArgsException(ArgsException.ErrorCode.MISSING_STRING, "x", None)
        self.assertEquals("Could not find string parameter for -x.", argsException.errorMessage())
    '''
    raise Exception
    '''
    def testInvalidIntegerMessage(self):
        argsException = ArgsException(ArgsException.ErrorCode.INVALID_INTEGER, "x", "Forty two")
        self.assertEquals("Argument -x expects an integer but was 'Forty two'.", argsException.errorMessage())
    '''
    raise Exception
    '''
    def testMissingIntegerMessage(self):
        argsException = ArgsException(ArgsException.ErrorCode.MISSING_INTEGER, "x", None)
        self.assertEquals("Could not find integer parameter for -x.", argsException.errorMessage())
    '''
    raise Exception
    '''
    def testInvalidDoubleMessage(self):
        argsException = ArgsException(ArgsException.ErrorCode.INVALID_DOUBLE, "x", 'Forty two')
        self.assertEquals("Argument -x expects a double but was 'Forty two'.", argsException.errorMessage())    
    '''
    raise Exception
    '''
    def testMissingDoubleMessage(self):
        argsException = ArgsException(ArgsException.ErrorCode.MISSING_DOUBLE, "x", 'None')
        self.assertEquals("Could not find double parameter for -x.", argsException.errorMessage())


if __name__ == '__main__':
    unittest.main()