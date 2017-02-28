from JackTokenizer import JackTokenizer

class CompilationEngine(object):
    
    def __init__(self, inStr):
        self.xml = ''
        self.jackFile = JackTokenizer(inStr)
        self.jackFile.advance()

    def compileClass(self):
        # check the first token, return if wrong
        if self.jackFile.token != 'class':
            print("first token needs to be 'class'")
            return ''
        
        self.xml += '<class>'       # open class tag
        self.writeAdv()             # write class keyword   
        self.writeAdv()             # write class name tag
        self.writeAdv()             # write '{'

        # look for variable declarations 
        while (self.jackFile.token == 'static' or self.jackFile.token == 'field') and \
        self.jackFile.tokenType == 'keyword':
            self.compileClassVarDec()

        # look for subroutine declarations 
        while (self.jackFile.token == 'method' or self.jackFile.token == 'function' or \
            self.jackFile.token == 'constructor') and self.jackFile.tokenType == 'keyword':
            self.compileSubroutine()

        # look for '}'
        while not (self.jackFile.token == '}' and self.jackFile.tokenType == 'symbol'):
            self.writeAdv("Expected '}'")
        self.writeAdv()

        # '}' has been hit, end of file. close class tag and return xml string
        if self.jackFile.hasMoreTokens(): print("There is uncompiled code after the class")
        self.xml += '\n</class>'
        return self.xml

    def compileClassVarDec(self):
        self.xml += '\n<classVarDec>'     # open classVarDec tag 
        # loop through until ';' 
        while not (self.jackFile.token == ';' and self.jackFile.tokenType == 'symbol'):
            self.writeAdv()
        self.writeAdv()                 # write ';'
        self.xml += '\n</classVarDec>'    # close classVarDec tag
    
    def compileSubroutine(self):
        self.xml += '\n<subroutineDec>'   # open subroutineDec tag
        self.writeAdv()                 # write sub type
        self.writeAdv()                 # write sub return type
        self.writeAdv()                 # write sub name
        
        self.writeAdv()                 # write '('
        self.xml += '\n<parameterList>'   # open parameterList tag
        self.compileParameterList()     # writes the potentially empty parameter list
        self.xml += '\n</parameterList>'  # close parameterList tag
        self.writeAdv()                 # write ')'

        self.xml += '\n<subroutineBody>'  # open subroutineBody tag
        self.writeAdv()                 # write '{'
        
        # look for variable declarations 
        while (self.jackFile.token == 'var') and self.jackFile.tokenType == 'keyword':
            self.compileVarDec()
        
        # write the sub statements
        self.xml += '\n<statements>'      # open statements tag
        self.compileStatements()        # compile all statements
        self.xml += '\n</statements>'     # close statements tag

        self.writeAdv()                 # write '}' (closing the subroutine body)
        self.xml += '\n</subroutineBody>' # close subroutineBody tag
        self.xml += '\n</subroutineDec>'  # close subroutineDec tag

    def compileParameterList(self):
        # loop through until ')' without writing it  
        while not (self.jackFile.token == ')' and self.jackFile.tokenType == 'symbol'):
            self.writeAdv()
    
    def compileVarDec(self):
        self.xml += '\n<varDec>'     # open varDec tag 
        # loop through until ';' 
        while not (self.jackFile.token == ';' and self.jackFile.tokenType == 'symbol'):
            self.writeAdv()
        self.writeAdv()                 # write ';'
        self.xml += '\n</varDec>'    # close varDec tag

    def compileStatements(self):
        # look for statements
        while not (self.jackFile.token == '}' and self.jackFile.tokenType == 'symbol'):
            if self.jackFile.token == 'let': self.compileLet()
            elif self.jackFile.token == 'if': self.compileIf()
            elif self.jackFile.token == 'while': self.compileWhile()
            elif self.jackFile.token == 'do': self.compileDo()
            elif self.jackFile.token == 'return': self.compileReturn()
            else:
                self.writeAdv('expected statement')
                return
    
    def compileDo(self):
        self.xml += '\n<doStatement>'     # open doStatement tag 
        # loop through until ';' 
        while not (self.jackFile.token == ';' and self.jackFile.tokenType == 'symbol'):
            if self.jackFile.token == '(' and self.jackFile.tokenType == 'symbol':
                self.writeAdv()
                self.compileExpressionList()             
            else:
                self.writeAdv()
        self.writeAdv()                 # write ';'
        self.xml += '\n</doStatement>'    # close doStatement tag

    def compileLet(self):
        # 'let' varName ('[' expression ']')? '=' expression ';'
        self.xml += '\n<letStatement>'     # open letStatement tag 

        self.writeAdv()     # write 'let'
        self.writeAdv()     # write varName
        if self.jackFile.token == '[':
            self.writeAdv()     # write '['
            self.compileExpression()
            self.writeAdv()     # write ']'
        self.writeAdv()     # write '='
        self.compileExpression()
        self.writeAdv()     #write ';'

        self.xml += '\n</letStatement>'    # close letStatement tag
    
    def compileWhile(self):
        # 'while' '(' expression ')' '{' statements '}' 
        self.xml += '\n<whileStatement>'
        self.writeAdv()     # write 'while'
        self.writeAdv()     # write '('
        self.compileExpression()
        self.writeAdv()     # write ')'
        self.writeAdv()     # write '{'
        self.xml += '\n<statements>'      # open statements tag
        self.compileStatements()
        self.xml += '\n</statements>'      # close statements tag
        self.writeAdv()     # write '}'
        self.xml += '\n</whileStatement>'
    
    def compileReturn(self):
        self.xml += '\n<returnStatement>'     
        self.writeAdv()                 # write 'return'
        # loop through until ';' 
        while not (self.jackFile.token == ';' and self.jackFile.tokenType == 'symbol'):
            self.compileExpression()
        self.writeAdv()                 # write ';'
        self.xml += '\n</returnStatement>'
    
    def compileIf(self):
        # 'if' '(' expression ')' '{' statements '}' 
        # ('else' '{' statements '}')?
        #TODO does not handle else statements
        self.xml += '\n<ifStatement>'
        self.writeAdv()     # write 'if'
        self.writeAdv()     # write '('
        self.compileExpression()
        self.writeAdv()     # write ')'
        self.writeAdv()     # write '{'
        self.xml += '\n<statements>'      # open statements tag
        self.compileStatements()
        self.xml += '\n</statements>'      # close statements tag
        self.writeAdv()     # write '}'
        if self.jackFile.token == 'else':
            self.writeAdv()     # write 'else'
            self.writeAdv()     # write '{'
            self.xml += '\n<statements>'      # open statements tag
            self.compileStatements()
            self.xml += '\n</statements>'      # close statements tag
            self.writeAdv()     # write '}' 
        self.xml += '\n</ifStatement>'


    def compileExpressionList(self):
        self.xml += '\n<expressionList>'
        # loop through until ')' without writing it  
        cont = True
        while cont:
            if self.jackFile.token == ')': 
                cont = False
            elif self.jackFile.token == ',':
                self.writeAdv()
            else:
                self.compileExpression()
        self.xml += '\n</expressionList>'

    def compileExpression(self):
        ###  term (op term)*
        # TODO can't handle unary operaters yet ('-' & '~')
        
        self.xml += '\n<expression>' 

        cont = True
        while cont:
            if self.isTerm() or self.isUnaryOp() or self.jackFile.token == '(':
                self.compileTerm()
                if self.isOp(): self.writeAdv()
            else:
                cont = False

        self.xml += '\n</expression>'
    
    def compileTerm(self):
        # this is the hard one that needs to look ahead
        # integerConstant | stringConstant | keywordConstant |
        # varName | varName '[' expression ']' | subroutineCall |
        # '(' expression ')' | unaryOp term
        self.xml += '\n<term>' 
        
        if self.isUnaryOp():            # account for unary operators
            self.writeAdv()         
            self.compileTerm()
        elif self.isTerm() and self.jackFile.peek() == '(':
            self.writeAdv()     # write 'term'
            self.writeAdv()     # write '('
            self.compileExpressionList()
            self.writeAdv()     # write ')'
        elif self.isTerm() and self.jackFile.peek() == '.' and self.jackFile.peek(3) == '(':
            self.writeAdv()     # write 'term'
            self.writeAdv()     # write '.'
            self.writeAdv()     # write 'term'
            self.writeAdv()     # write '('
            self.compileExpressionList()
            self.writeAdv()     # write ')'
        elif self.isTerm() and self.jackFile.peek() == '[':
            self.writeAdv()     # write 'term'
            self.writeAdv()     # write '['
            self.compileExpression()
            self.writeAdv()     # write ']'
        elif self.jackFile.token == '(':
            self.writeAdv()     # write '('
            self.compileExpression()
            self.writeAdv()     # write ')'
        else:
            self.writeAdv()     # write 'term'

        self.xml += '\n</term>' 
    
    def writeAdv(self, *err):
        if err:
            print(err[0])
            self.xml += '\n<error>' + err[0] + '</error>'
            self.jackFile.advance()
        else:
            if self.jackFile.token == '<': self.jackFile.token = '&lt;'
            if self.jackFile.token == '>': self.jackFile.token = '&gt;'
            if self.jackFile.token == '&': self.jackFile.token = '&amp;'
            self.xml += '\n<' + self.jackFile.tokenType + '> ' + self.jackFile.token + ' </' + self.jackFile.tokenType + '>'
            self.jackFile.advance()

    def isOp(self):
        operators = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        return self.jackFile.token in operators
        
    def isUnaryOp(self):
        unaryOperators = ['-', '~']
        return self.jackFile.token in unaryOperators
    
    def isSymbol(self):
        symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
        return self.jackFile.token in symbols

    def isTermEnd(self):
        operators = ['+', '-', '*', '/', '&' '|', '<', '>', '=']
        termFinshers = [' ', ')', ']', ';'] +  operators
        return self.jackFile.token in termFinshers
    
    def isTerm(self):
        terms = ['keyword', 'identifier', 'integerConstant', 'stringConstant']
        return self.jackFile.tokenType in terms


""" NOT TERMINALS:
- class, classVarDec, subroutineDec, parameterList, subroutineBody, varDec;
- statements, whileSatement, ifStatement, returnStatement, letStatement, doStatement;
- expression, term, expressionList. 

"""

    