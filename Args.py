import ArgsException

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

    def __init__(self, schema: str, args: str) -> None:
        self.schema = schema
        self.args = args.split(' ')
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
    '''
    raise ArgsException
    '''
    def __validateSchemaElementId(self, elementId: str) -> None:
        if (!elementId.isAlpha() or len(elementId) != 1):
            raise ArgsException

    def __parseArguments(self):
        None

    def cardinality(self) -> int:
        return len(self.argsFound)
