import unittest
from Args import Args
from ArgsException import ArgsException

class ArgsTest(unittest.TestCase):

    def testCreateWithNoSchemaOrArguments(self):
        args = Args("", "")
        self.assertEqual(args.cardinality(), 0);
    '''
    raise Exception
    '''
    def testWithNoSchemaButWithOneArgument(self):
        try:
            Args("", ["-x"])
            self.fail("Expect ArgsException in testWithNoSchemaButWithOneArgument")
        except ArgsException as e:
            self.assertEqual(
                ArgsException.ErrorCode.UNEXPECTED_ARGUMENT,
                e.getErrorCode()
                )
            self.assertEqual("x", e.getErrorArgumentId())
    '''
    raise Exception
    '''
    def testWithNoSchemaButWithMultipleArguments(self):
        try:
            Args("", ["-x", "-y"])
            self.fail("Expect ArgsException in testWithNoSchemaButWithMultipleArguments")
        except ArgsException as e:
            self.assertEqual(
                ArgsException.ErrorCode.UNEXPECTED_ARGUMENT,
                e.getErrorCode()
                )
            self.assertEqual("x", e.getErrorArgumentId())
    '''
    raise Exception
    '''
    def testNonLetterSchema(self):
        try:
            Args("*", [])
            self.fail("Args constructor should have thrown exception")
        except ArgsException as e:
            self.assertEqual(
                ArgsException.ErrorCode.INVALID_ARGUMENT_NAME,
                e.getErrorCode()
                )
            self.assertEqual("*", e.getErrorArgumentId())

    '''
    raise Exception
    '''
    def testInvalidArgumentFormat(self):
        try:
            Args("f~", [])
            self.fail("Args constructor should have thrown exception")
        except ArgsException as e:
            self.assertEqual(
                ArgsException.ErrorCode.INVALID_FORMAT,
                e.getErrorCode()
                )
            self.assertEqual("f", e.getErrorArgumentId())

    def testSimpleBooleanPresent(self):
        args = Args("x", ["-x"])
        self.assertEqual(1, args.cardinality())
        self.assertEqual(True, args.getBoolean("x"))


if __name__ == '__main__':
    unittest.main()