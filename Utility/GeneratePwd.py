import re
import random

# -------------------------------------------------------------
#               class:      LetterCase
# -------------------------------------------------------------
# For Range objcets. If range is like '[a-Z]' or '[A-z]'
class LetterCase:
    def __init__(self, start, end):
        self.start = ord(start)
        self.end = ord(end)
        self.bothCase = False
        self.__initalize(start, end)

    def __initalize(self, start, end):
        if start.isupper() != end.isupper():
            self.start = ord(start.lower())
            self.end = ord(end.lower())
            self.bothCase = True

# -------------------------------------------------------------
#               class:      BaseCharSet
# -------------------------------------------------------------
class BaseCharSet:

    def __init__(self, definition):
        self.amount = None
        self.charset = None
        self.definition = definition

    def hasAmount(self):
        if not self.amount:
            return False
        return True

    # Get randomly the defined amount of character from the charset.
    # Returns a list of character (string).
    def randomCharset(self):
        charset = []
        random.seed(None, 2)
        for i in range(0, self.amount):
            rnd = random.randrange(0, len(self.charset))
            charset.append(self.charset[rnd])
        return charset

    def toString(self):
        print('-----------------------------------------------------')
        print('Klasse: ' + str(type(self)))
        print('Definition: ' + self.definition)
        print('Anzahl: ' + str(self.amount))
        print('Zeichen: ' + self.charset)

# -------------------------------------------------------------
#               class:      Range
# -------------------------------------------------------------
class Range(BaseCharSet):

    def __init__(self, definition):
        super().__init__(definition)
        self.__parseDefinition(definition)

    # Parse definition string and initialize this object.
    def __parseDefinition(self, definition):
        pos = definition.find('[')
        if not definition.startswith('*'):
            self.amount = int(definition[:pos])
        start = definition[pos+1]
        end = definition[pos+3]
        letterCase = LetterCase(start, end)
        self.charset = self.rangeString(letterCase.start, letterCase.end)
        if letterCase.bothCase:
            self.charset += self.charset.upper()

    # Build a string with characters from start to end.
    def rangeString(self, start, end):
        charset = str()
        if start < end:
            for c in range(start, end+1):
                charset += chr(c)
        else:
            raise Exception("The start value '" + chr(start) + "' of Range object is greater then the end value '" + chr(end) + ".")

        return charset

    # Return a triple with ord(start), ord(end) and True or False.
    # If definition has a upper case and a lower case letter then
    # the range should contain uppser and lower case letters.
    def letterCase(self, start, end):
        if start.isupper() == end.isupper():
            return (ord(start.lower()), ord(end.lower()), True)
        return (ord(start), ord(end), False)

# -------------------------------------------------------------
#               class:      Set
# -------------------------------------------------------------
class Set(BaseCharSet):

    def __init__(self, definition):
        super().__init__(definition)
        self.__parseDefinition(definition)

    # Parse the definition string and initialize the object.
    def __parseDefinition(self, definition):
        pos = definition.find('{')
        if not definition.startswith('*'):
            self.amount = int(definition[:pos])
        end = len(definition) - 1
        self.charset = definition[pos+1:end]

# -------------------------------------------------------------
#               class:      Generator
# -------------------------------------------------------------
class Generator:

    patternSet = '([0-9]+|\*)\{.*?\}'       #   5{+#*-_.:,;()<>=?}  or  *{<>.:-#_*+=?()}
    patternRange = '([0-9]+|\*)\[.-.\]'     #   9[a-z]  or  *[a-z]

    def __init__(self, definition='*[a-Z]*[0-9]*{+#-_<>()*.:=}', length=12):
        self.definition = definition
        self.lengthPwd = length
        self.lengthDefined = 0
        self.objectsWithoutLenght = 0
        self.definitionList = []

    # Parse definition string.
    def parseDefinition(self):
        definition = self.definition
        self.__parsePattern(self.patternRange, True)
        self.__parsePattern(self.patternSet)
        if len(self.definition) > 0:
            raise Exception("The part '" + definition + "' of definition is not valid.")
        self.__fixAmount()
        self.definition = definition

    # Parse the definition string for a pattern.
    # Build range objects and append them to the list.
    def __parsePattern(self, pattern, isRange=False):
        while(True):
            match = re.search(pattern, self.definition)
            if not match:
                break
            obj = None
            if isRange:
                obj = Range(match.group())
            else:
                obj = Set(match.group())
            self.definitionList.append(obj)
            if obj.hasAmount():
                self.lengthDefined += obj.amount
            else:
                self.objectsWithoutLenght += 1
            before = self.definition[:match.span()[0]]
            after = self.definition[match.span()[1]:]
            self.definition = before + after

    # If there are some object without a fix length value then
    # they will get one here.
    def __fixAmount(self):
        if self.objectsWithoutLenght < 1:
            return
        amount = int((self.lengthPwd - self.lengthDefined) / self.objectsWithoutLenght)
        if amount <= 0:
            raise Exception('There are more characters defined ({0}) then the password length ({1}).'.format(self.lengthDefined, self.lengthPwd))
        rest = (self.lengthPwd - self.lengthDefined) % self.objectsWithoutLenght
        for obj in self.definitionList:
            if not obj.hasAmount():
                obj.amount = amount
                if rest > 0:
                    obj.amount += 1
                    rest -= 1

    # Get a random password from definition.
    def randomPassword(self):
        charset = []
        for obj in self.definitionList:
            charset += obj.randomCharset()
        random.seed(None, 2)
        password = str()
        while(len(charset) > 0):
            rnd = random.randrange(0, len(charset))
            password += charset[rnd]
            del charset[rnd]

        return password

    # Object to string
    def toString(self):
        print('Definition: ' + self.definition)
        print('Passwortlänge: ' + str(self.lengthPwd))
        for obj in self.definitionList:
            obj.toString()
