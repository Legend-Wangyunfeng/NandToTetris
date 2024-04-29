import consts

class CompilationEngine:

    def __init__(self, tokenizer, output_file):
        self.tokenizer = tokenizer
        self.output_file = output_file


    def compileClass(self):
        self.output_file.write('<class>\n')
        self.process("class")
        self.process(self.tokenizer.token)
        self.process("{")
        while (self.tokenizer.token == "static" or self.tokenizer.token == "field"):
            self.compileClassVarDec()
        while (self.tokenizer.token == "constructor" or self.tokenizer.token == "function" or self.tokenizer.token == "method"):
            self.compileSubroutine()
            
        self.process("}")
        self.output_file.write('</class>\n')

    def compileClassVarDec(self):
        self.output_file.write('<classVarDec>\n')
        self.process(self.tokenizer.token)
        self.process(self.tokenizer.token)
        self.process(self.tokenizer.token)
        while (self.tokenizer.token != ";"):
            self.process(",")
            self.process(self.tokenizer.token)
        self.process(";")
        self.output_file.write('</classVarDec>\n')
        
    def compileSubroutine(self):
        self.output_file.write('<subroutineDec>\n')
        self.process(self.tokenizer.token)
        self.process(self.tokenizer.token)
        self.process(self.tokenizer.token)
        self.process("(")
        self.compileParameterList()
        self.process(")")
        self.compileSubroutineBody()
        self.output_file.write('</subroutineDec>\n')

    def compileParameterList(self):
        self.output_file.write('<parameterList>\n')
        if (self.tokenizer.token != ")"):
            self.process(self.tokenizer.token)
            self.process(self.tokenizer.token)
            while (self.tokenizer.token != ")"):
                self.process(",")
                self.process(self.tokenizer.token)
                self.process(self.tokenizer.token)               
        self.output_file.write('</parameterList>\n')

    def compileSubroutineBody(self):
        self.output_file.write('<subroutineBody>\n')
        self.process("{")
        while (self.tokenizer.token == "var"):
            self.compileVarDec()
            
        self.compileStatements()
        self.process("}")
        self.output_file.write('</subroutineBody>\n')

    def compileVarDec(self):
        self.output_file.write('<varDec>\n')
        self.process(self.tokenizer.token)
        self.process(self.tokenizer.token)
        while (self.tokenizer.token != ";"):
            self.process(",")
            self.process(self.tokenizer.token)
        self.process(";")
        self.output_file.write('</varDec>\n')
        
    def compileStatements(self):
        self.output_file.write('<statements>\n')
        while (self.tokenizer.token in consts.STATEMENT_KEYWORDS):
            if (self.tokenizer.token == "let"):
                self.compileLet()
            elif (self.tokenizer.token == "if"):
                self.compileIf()
                
            elif (self.tokenizer.token == "while"):
                self.compileWhile()
                
            elif (self.tokenizer.token == "do"):
                self.compileDo()
                
            elif (self.tokenizer.token == "return"):
                self.compileReturn()
                
        self.output_file.write('</statements>\n')
        
    def compileLet(self):
        self.output_file.write('<letStatement>\n')
        self.process(self.tokenizer.token)
        self.process(self.tokenizer.token)
        if (self.tokenizer.token == "["):
            self.process("[")
            self.compileExpression()
            self.process("]")
            
        self.process(self.tokenizer.token)
        self.compileExpression()
        self.process(";")
        
    def compileIf(self):
        self.output_file.write('<ifStatement>\n')
        self.process(self.tokenizer.token)
        self.process("(")
        self.compileExpression()
        self.process(")")
        self.process("{")
        self.compileStatements()
        self.process("}")
        if (self.tokenizer.token == "else"):
            self.process("else")
            self.process("{")
            self.compileStatements()
            self.process("}")

        self.output_file.write('</ifStatement>\n')
        
    def compileWhile(self):
        self.output_file.write('<whileStatement>\n')
        self.process(self.tokenizer.token)
        self.process("(")
        self.compileExpression()
        self.process(")")
        self.process("{")
        self.compileStatements()
        self.process("}")
        self.output_file.write('</whileStatement>\n')
        
    def compileDo(self):
        self.output_file.write('<doStatement>\n')
        self.process(self.tokenizer.token)
        while (self.tokenizer.token == "."):
            self.process(".")
            self.process(self.tokenizer.token)
            
        self.process("(")
        self.compileExpressionList()
        self.process(")")
        self.process(";")
        self.output_file.write('</doStatement>\n')
        
    def compileReturn(self):
        self.output_file.write('<returnStatement>\n')
        self.process(self.tokenizer.token)
        if (self.tokenizer.token != ";"):
            self.compileExpression()
        self.process(";")
        self.output_file.write('</returnStatement>\n')
        
    def compileExpression(self):
        self.output_file.write('<expression>\n')
        self.compileTerm()
        while (self.tokenizer.token in consts.OPERATORS):
            if (self.tokenizer.token in consts.OPERATORS_MAP):
                self.process(consts.OPERATORS_MAP(self.tokenizer.token))
            else:
                self.process(self.tokenizer.token)
            self.compileTerm()
        self.output_file.write('</expression>\n')

        
    def compileTerm(self):

        
    def compileExpressionList(self):
        self.output_file.write('<expressionList>\n')
        if (self.tokenizer.token != ")"):
            self.compileExpression()
            while (self.tokenizer.token == ","):
                self.process(",")
                self.compileExpression()
        self.output_file.write('</expressionList>\n')

    def process(self, string):
        if (self.tokenizer.token == string):
            self.printXMLToken(self.tokenizer.type, string)
        else:
            print("syntax error")
        self.tokenizer.advance()

    def printXMLToken(self, tokenType, string):
        self.output_file.write(f'<{tokenType}> {string} </{tokenType}>\n')