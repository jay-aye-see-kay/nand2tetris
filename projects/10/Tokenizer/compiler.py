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
        return '<' + self.TokenType() + '> ' + self.token + ' </' + self.TokenType() + '>\n' 

    def hasMoreTokens(self):
        if self.index < len(self.string):
            return True
        return False

    def advance(self):
        newToken = ''; char = '' 
        # push past and starting white space
        while self.string[self.index] == " ":
            self.index += 1
        
        # if symbol
        if self.isSymbol(self.string[self.index]):
            self.token = self.string[self.index]
            self.symbol()
            self.tokenType = 'SYMBOL'
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
            self.tokenType = 'STRING_CONST'
        # if number/integer constant
        elif self.string[self.index].isdigit():
            while self.string[self.index].isdigit():
                char = self.string[self.index]
                newToken += char
                self.index += 1
            self.token = newToken
            self.tokenType = 'INT_CONST'
        # if keyword or identifier
        elif self.string[self.index].isalpha() or self.string[self.index] == "_":
            while self.string[self.index].isdigit() or self.string[self.index].isalpha() or self.string[self.index] == "_":
                char = self.string[self.index]
                newToken += char
                self.index += 1
            self.token = newToken
            if self.isKeyword(newToken): self.tokenType = 'KEYWORD'
            else: self.tokenType = 'IDENTIFIER'
        # uncaught error I guess.. don't have a plan here yet
        else:
            self.token = "Error"
            self.tokenType = 'ERROR'
            self.index += 1

    def TokenType(self):
        # return current token type (KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, or STRING_CONST)
        if self.tokenType == "STRING_CONST": return "stringConstant"
        if self.tokenType == "INT_CONST": return "integerConstant"
        return self.tokenType.lower()
    
    def keyword(self):
        # returns the current token's keyword, only called when tokenType = KEYWORD
        # (CLASS, METHOD, FUNCTION, CONSTRUCTOR, INT, BOOLEAN, CHAR, VOID, VAR, STATIC,
        # FIELD, LET, DO, IF, ELSE, WHILE, RETURN, TRUE, FALSE, NULL, or THIS)
        return self.token.upper()

    def symbol(self):
        # returns character of the current token
        if self.token == '<': self.token = '&lt;'
        if self.token == '>': self.token = '&gt;'
        if self.token == '&': self.token = '&amp;'
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
        if testChar == '{' \
            or testChar == '}' \
            or testChar == '(' \
            or testChar == ')' \
            or testChar == '[' \
            or testChar == ']' \
            or testChar == '.' \
            or testChar == ',' \
            or testChar == ';' \
            or testChar == '+' \
            or testChar == '-' \
            or testChar == '*' \
            or testChar == '/' \
            or testChar == '&' \
            or testChar == '|' \
            or testChar == '<' \
            or testChar == '>' \
            or testChar == '=' \
            or testChar == '~':
            return True
        else:
            return False

    def isKeyword(self, testWord):

        # reutrns if the testWord is one of 21 jack keywords
        if testWord == 'class' \
            or testWord == 'constructor' \
            or testWord == 'function' \
            or testWord == 'method' \
            or testWord == 'field' \
            or testWord == 'static' \
            or testWord == 'var' \
            or testWord == 'int' \
            or testWord == 'char' \
            or testWord == 'boolean' \
            or testWord == 'void' \
            or testWord == 'true' \
            or testWord == 'false' \
            or testWord == 'null' \
            or testWord == 'this' \
            or testWord == 'let' \
            or testWord == 'do' \
            or testWord == 'if' \
            or testWord == 'else' \
            or testWord == 'while' \
            or testWord == 'return':
            return True
        else:
            return False

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
