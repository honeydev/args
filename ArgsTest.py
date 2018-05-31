import unittest
from Args import Args

class ArgsTest(unittest.TestCase):

    def testCreateWithNoSchemaOrArguments(self):
        args = Args("", "")
        print(args.cardinality())
        self.assertEqual(args.cardinality(), 0);


if __name__ == '__main__':
    unittest.main()