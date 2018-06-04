import ArgsException
from marshalers.BooleanArgumentMarshaler import BooleanArgumentMarshaler

class Args:

    schema = ""
    args = []
    """
    dictonary
    :key - string, schema symbol
    :value - ArgumentMarshaler instance
    """
    marshalers = {}
    """
    set contain founded arguments
    """
    argsFound = {}

    def __init__(self, schema: str, args: list) -> None:
        self.schema = schema
        self.args = args
        self.__parse()
    '''
    raise ArgsException
    '''
    def __parse(self) -> None:
        self.__parseSchema()
        #self.__parseArguments()

    def __parseSchema(self) -> bool:
        for element in self.schema.split(","):
            if len(element) > 0:
                self.__parseSchemaElement(self, element.strip())

        return True

    def __parseSchemaElement(self, element: str):
        elementId = element[0]
        elementTail = element[1:]
        self.__validateSchemaElementId(elementId)

        if (len(elementTail) == 0):
            self.marshalers[elementId] = BooleanArgumentMarshaler()
        elif (elementTail == "*"):
            self.marshalers[elementId] = StringArgumentMarshaler()
        elif (elementTail == "#"):
            self.marshalers[elementId] = IntegerArgumentMarshaler()
        elif (elementTail == "##"):
            self.marshalers[elementId] = DoubleArgumentMarshaler()
        else:
            raise ArgsException(ArgsException.ErrorCode.INVALID_FORMAT, elementId, elementTail)
    '''
    raise ArgsException
    '''
    def __validateSchemaElementId(self, elementId: str) -> None:
        if (not elementId.isAlpha() or len(elementId) != 1):
            raise ArgsException(ArgsException.ErrorCode.INVALID_ARGUMENT_NAME, elementId, None)

    def __parseArguments(self):
        pass

    def cardinality(self) -> int:
        return len(self.argsFound)
