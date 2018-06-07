from ArgsException import ArgsException
from marshalers.BooleanArgumentMarshaler import BooleanArgumentMarshaler
from marshalers.StringArgumentMarshaler import StringArgumentMarshaler

class Args:

    def __init__(self, schema: str, args: list) -> None:
        self.schema = ""
        self.args = []
        self.marshalers = {}
        self.argsFound = set({})
        self.currentArgument = None
        self.schema = schema
        self.args = args
        self.__parse()

    '''
    raise ArgsException
    '''
    def __parse(self) -> None:
        self.__parseSchema()
        self.__parseArguments()

    def __parseSchema(self) -> bool:
        for element in self.schema.split(","):
            if len(element) > 0:
                self.__parseSchemaElement(element.strip())

        return True
    '''
    raise ArgsException
    '''
    def __parseSchemaElement(self, element: str):
        print('setMarshaler')
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
        if (not elementId.isalpha() or len(elementId) != 1):
            raise ArgsException(ArgsException.ErrorCode.INVALID_ARGUMENT_NAME, elementId, None)
    '''
    raise ArgsException
    '''
    def __parseArguments(self) -> None:
        print('arguments', self.args)
        for self.currentArgument in self.args:
            print('current', self.currentArgument)
            self.__parseArgument(self.currentArgument)
    '''
    raise ArgsException
    '''
    def __parseArgument(self, arg: str) -> None:
        if (arg.startswith("-")):
            self.__parseElements(arg)
    '''
    raise ArgsException
    '''
    def __parseElements(self, arg: str) -> None:
        counter = 1
        while (counter < len(arg)):
            self.__parseElement(arg[counter])
            counter += 1
    '''
    raise ArgsException
    '''
    def __parseElement(self, argChar: str) -> None:
        print('schema', self.schema, 'marshalers', self.marshalers)
        if (self.__setArgument(argChar)):
            self.argsFound.update(argChar)
        else:
            raise ArgsException(ArgsException.ErrorCode.UNEXPECTED_ARGUMENT, argChar, None)
    '''
    raise ArgsException
    '''
    def __setArgument(self, argChar: str) -> bool:
        if (argChar in self.marshalers):
            argumentMarshaler = self.marshalers[argChar]
        else:
            return False

        try:
            argumentMarshaler.set(self.currentArgument)
            return True
        except ArgsException as e:
            e.setErrorArgumentId(argChar)
            raise e

    def cardinality(self) -> int:
        return len(self.argsFound)

    def getBoolean(self, arg: str) -> bool:
        argumentMarshaler = self.marshalers.get(arg)
        boolean = False

        try:
            boolean = argumentMarshaler != None and argumentMarshaler.get()
        except:
            boolean = False

        return boolean

    def getString(self, arg: str) -> str:
        print(self.marshalers)
        argumentMarshaler = self.marshalers.get(arg)
        print('argumentMarshaler', argumentMarshaler)
        print('stringAM', self.marshalers.get('x').get())
        return argumentMarshaler.get()

        # try:
        #     return "" if argumentMarshaler == None else argumentMarshaler.get()
        # except Exception:
        #     return ""

    def has(self, arg: str) -> bool:
        return arg in self.argsFound;
