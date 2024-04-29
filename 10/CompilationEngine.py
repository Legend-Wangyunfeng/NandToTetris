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

    def compileVarDec(self):
        
    def compileStatements(self):
        
    def compileLet(self):
        
    def compileIf(self):
        
    def compileWhile(self):
        
    def compileDo(self):
        
    def compileReturn(self):
        
    def compileExpression(self):
        
    def compileTerm(self):
        
    def compileExpressionList(self):

    def process(self, string):
        if (self.tokenizer.token == string):
            self.printXMLToken(self.tokenizer.type, string)
        else:
            print("syntax error")
        self.tokenizer.advance()

    def printXMLToken(self, tokenType, string):
        self.output_file.write(f'<{tokenType}> {string} </{tokenType}>\n')