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

    def testSimpleStringPresent(self):
        args = Args("x*", ["-x", "param"])
        self.assertEqual(1, args.cardinality())
        self.assertTrue(args.has('x'))
        self.assertEqual("param", args.getString("x"))
    '''
    raise Exception
    '''
    def testMissingStringArgument(self):
        try:
            args = Args("x*", ["-x"])
            self.fail("Args constructor should have thrown exception")
        except ArgsException as e:
            self.assertEqual(ArgsException.ErrorCode.MISSING_STRING, e.getErrorCode())
            self.assertEqual("x", e.getErrorArgumentId())

    def testSpacesInFormat(self):
        args = Args("x, y", ["-xy"])
        self.assertEqual(2, args.cardinality())
        self.assertTrue(args.has("x"))
        self.assertTrue(args.has("y"))

    def testSimpeIntPresent(self):
        args = Args("x#", ["-x", 42])
        self.assertEqual(1, args.cardinality())
        self.assertTrue(args.has('x'))
        self.assertEqual(42, args.getInt('x'))
    '''
    raise Exception
    '''
    def testInvalidInteger(self):
        try:
            Args("x#", ["-x", "Forty two"])
            self.fail("Args constructor should have thrown exception")
        except ArgsException as e:
            self.assertEqual(ArgsException.ErrorCode.INVALID_INTEGER, e.getErrorCode())
            self.assertEqual("x", e.getErrorArgumentId())
            self.assertEqual("Forty two", e.getErrorParameter())
    '''
    raise Exception
    '''
    def testMissingInteger(self):
        try:
            Args("x#", ["-x"])
            self.fail("Args constructor should have thrown exception")
        except ArgsException as e:
            self.assertEqual(ArgsException.ErrorCode.MISSING_INTEGER, e.getErrorCode())
            self.assertEqual("x", e.getErrorArgumentId())

    def testSimpleDoublePresent(self):
        args = Args("x##", ["-x", "42.3"])
        self.assertEqual(1, args.cardinality())
        self.assertTrue(args.has('x'))
        self.assertEqual(42.3, args.getDouble("x"))
    '''
    raise Exception
    '''
    def testInvalidDouble(self):
        try:
            Args("x##", ["-x", "Forty two"])
            self.fail("Args constructor should have thrown exception")
        except ArgsException as e:
            self.assertEqual(ArgsException.ErrorCode.INVALID_DOUBLE, e.getErrorCode())
    '''
    raise Exception
    '''
    def testMissingDouble(self):
        try:
            Args("x##", ["-x"])
            self.fail("Args constructor should have thrown exception")
        except ArgsException as e:
            self.assertEqual(ArgsException.ErrorCode.MISSING_DOUBLE, e.getErrorCode())
            self.assertEqual("x", e.getErrorArgumentId())


if __name__ == '__main__':
    unittest.main()