from enum import Enum

class TokenType(Enum):
    KEYWORD = 1
    SYMBOL = 2
    IDENTIFIER = 3
    INT_CONST = 4
    STRING_CONST = 5

class JackTokenizer:
    def __init__(self, file_name):
        self.file_name = file_name
        
        self.keywords = ['class', 'constructor', 'function', 'method', 'field', 'static',
                          'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null',
                          'this', 'let', 'do', 'if', 'else', 'while', 'return']
        self.symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
        self.tokenType = None
      
        self.input_file = open(file_name, 'r')
        self.name = file_name.split(".jack")[0]

        self.current_command = self.input_file.readline()
        self.current_token = None
        self.token_list = []

    def advanceCommands(self):
        # Reads the next command from the input and makes it the current command.
        # Should be called only if has_more_commands() is true.
        # Initially there is no current command.
        self.current_command = self.input_file.readline()

    def hasMoreCommands(self):
        if self.current_command:
            # 处理掉注释
            # 单行注释以 // 开头
            # 多行注释以 /* 开头，以 */ 结尾
            self.current_command = self.current_command.strip()

            if self.current_command.startswith("/**"):
                while not self.current_command.endswith("*/"):
                    self.advanceCommands()
                    self.current_command = self.current_command.strip()
                    
                self.advanceCommands()
                return self.hasMoreCommands()
            else:
                self.current_command = self.current_command.split("//")[0]
                self.token_list = self.current_command.split()
                # self.current_token = self.token_list[0] if len(self.token_list) > 0 else None
                return True

        else:
            return False
        
    def hasMoreTokens(self):
        # Returns true if there are more tokens to read, false otherwise.
        if len(self.token_list) > 0:
            return True
        else:
            return False

    def advanceTokens(self):
        # Reads the next token from the current command and makes it the current token.
        # Should be called only if has_more_tokens() is true.
        # Initially there is no current token.
        if self.hasMoreTokens():
            self.current_token = self.token_list.pop(0)
            #如果self.current_token末尾字符为“,”，则去掉这个“,”
            if self.current_token.endswith(","):
                self.current_token = self.current_token[:-1]
            #如果self.current_token末尾字符为“;”，则将这个“;”作为单独的一个token
            elif self.current_token.endswith(";") and self.current_token != ";":
                self.current_token = self.current_token[:-1]
                self.token_list.append(";")



if __name__ == "__main__":
    # Test the JackTokenizer
    file_name = "./Square/Main.jack"
    tokenizer = JackTokenizer(file_name)
    while tokenizer.hasMoreCommands():
        while tokenizer.hasMoreTokens():
            print(tokenizer.current_token)
            tokenizer.advanceTokens()

        tokenizer.advanceCommands()
            


