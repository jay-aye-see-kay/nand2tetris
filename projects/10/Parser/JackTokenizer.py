class JackTokenizer(object):
    
    def __init__(self, input_string):
        self.string = self.tidy_up(input_string)
        self.index = 0
        self.token = ''

    def printToken(self):
        self.advance()
        print('<' + self.tokenType + '>' + self.token + ' </' +self.tokenType + '>')
        #print('index: ' + str(self.index) + '. string length: ' + str(len(self.string)))
        #if self.tokenType == "ERROR": print('error')
    
    def writeXML(self):
        return '<' + self.tokenType + '> ' + self.token + ' </' + self.tokenType + '>\n' 

    def hasMoreTokens(self):
        if self.index < len(self.string):
            return True
        return False
    
    def peek(self, *depth):
        if not depth: depth = 1
        else: depth = depth[0]
        # peek returns next token without advancing index
        tempIndex = self.index
        tempToken = self.token
        tempTokenType = self.tokenType
        for i in range(depth):
            self.advance()
        peekedToken = self.token
        self.index = tempIndex
        self.token = tempToken
        self.tokenType = tempTokenType
        return peekedToken

    def advance(self):
        # exit silently if on last token
        if not self.hasMoreTokens(): return
        
        newToken = ''; char = '' 
        # push past and starting white space
        while self.hasMoreTokens() and self.string[self.index] == " ":
            self.index += 1
        
        # if symbol
        if self.isSymbol(self.string[self.index]):
            self.token = self.string[self.index]
            self.symbol()
            self.tokenType = 'symbol'
            self.index += 1
        # if string constant
        elif self.string[self.index] == '"':
            self.index += 1
            while char != '"':
                char = self.string[self.index]
                newToken += char
                self.index += 1
            newToken = newToken[:-1]
            self.token = newToken
            self.tokenType = 'stringConstant'
        # if number/integer constant
        elif self.string[self.index].isdigit():
            while self.string[self.index].isdigit():
                char = self.string[self.index]
                newToken += char
                self.index += 1
            self.token = newToken
            self.tokenType = 'integerConstant'
        # if keyword or identifier
        elif self.string[self.index].isalpha() or self.string[self.index] == "_":
            while self.string[self.index].isdigit() or self.string[self.index].isalpha() or self.string[self.index] == "_":
                char = self.string[self.index]
                newToken += char
                self.index += 1
            self.token = newToken
            if self.isKeyword(newToken): self.tokenType = 'keyword'
            else: self.tokenType = 'identifier'
        # uncaught error I guess.. don't have a plan here yet
        else:
            self.token = "Error"
            self.tokenType = 'ERROR'
            self.index += 1

    def TokenType(self):
        # return current token type (KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, or STRING_CONST)
        return self.tokenType
    
    def keyword(self):
        # returns the current token's keyword, only called when tokenType = KEYWORD
        # (CLASS, METHOD, FUNCTION, CONSTRUCTOR, INT, BOOLEAN, CHAR, VOID, VAR, STATIC,
        # FIELD, LET, DO, IF, ELSE, WHILE, RETURN, TRUE, FALSE, NULL, or THIS)
        return self.token.upper()

    def symbol(self):
        # returns character of the current token
        return self.token

    def identifier(self):
        # returns identifier of current token
        return self.token

    def intVal(self):
        # returns integer value of current token
        return int(self.token)

    def stringVal(self):
        # returns string value of current token (without "")
        return self.token
    
    def isSymbol(self, testChar):
        # returns if testChar is one of the 19 jack symbols
        symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
        return testChar in symbols

    def isKeyword(self, testWord):
        # reutrns if the testWord is one of 21 jack keywords
        keywords = ['class', 'constructor', 'function', 'method', 'field', 'static', 
        'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 
        'let', 'do', 'if', 'else', 'while', 'return']
        return testWord in keywords

    def isStatement(self, testWord):
        # reutrns if the testWord is one of 6 jack statements
        statementTypes = ['let', 'do', 'if', 'else', 'while', 'return']
        return testWord in statementTypes

    def tidy_up(self, str0):
        # initialize str1 for output, set comment flags to false
        str1 = ''; MLC = False; SLC = False
        # loop through string by characters
        for i in range(len(str0)):
            # check if in leaving or entering comment section and change flags as needed
            if str0[i] == '/' and str0[i+1] == '/': SLC = True
            if str0[i] == '\n': SLC = False
            if str0[i] == '/' and str0[i+1] == '*': MLC = True
            if str0[i-2] == '*' and str0[i-1] == '/': MLC = False
            # if character is not in comment or new line, add to output string
            if MLC == False and SLC == False and str0[i] != '\n':
                str1 += str0[i]
        # spilt and re-join output string to remove additional whitespace
        return ' '.join(str1.split())
