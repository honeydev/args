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
            self.fail("Expect ArgsException")
        except ArgsException as e:
            self.assertEqual(
                ArgsException.ErrorCode.UNEXPECTED_ARGUMENT,
                e.getErrorCode()
                )
            self.assertEqual("x", e.getErrorArgumentId())

    def testWithNoSchemaButWithMultipleArguments(self):
        try:
            Args("", ["-x"])


if __name__ == '__main__':
    unittest.main()