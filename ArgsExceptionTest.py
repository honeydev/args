import unittest
from ArgsException import ArgsException

class ArgsExceptionTest(unittest.TestCase):
    '''
    raise Exception
    '''
    def testUnexpectedMessage(self):
        argsException = ArgsException(ArgsException.ErrorCode.UNEXPECTED_ARGUMENT, "x", None)
        self.assertEqual("Argument -x unexpected ". argsException.errorMessage())

if __name__ == '__main__':
    unittest.main()