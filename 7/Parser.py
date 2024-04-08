from enum import Enum


class CommandType(Enum):
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2

class Parser:
    def __init__(self, input_file):
        # Opens the input file/stream and gets ready to parse it
        self.input_file = open(input_file, 'r')
        self.current_command = self.input_file.readline()
        self.name = input_file.split("/")[-1].split(".vm")[0] + ".asm"

        self.command_type = None

    def has_more_commands(self):
        # Are there more commands in the input?
        if  self.current_command:
            self.current_command = self.current_command.strip().split("//")[0]
            return True
        else:
            
            return False
    
    def advance(self):
        # Reads the next command from the input and makes it the current command.
        # Should be called only if has_more_commands() is true.
        # Initially there is no current command.
        self.current_command = self.input_file.readline()

    def commandType(self):
        if self.current_command.startswith("push"):
            return CommandType.C_PUSH
        elif self.current_command.startswith("pop"):
            return CommandType.C_POP
        else:
            return CommandType.C_ARITHMETIC
        
    def arg1(self):
        if self.command_type == CommandType.C_PUSH:
            return self.current_command.split(" ")[1]
        elif self.command_type == CommandType.C_POP:
            return self.current_command.split(" ")[1]
        else:
            return self.current_command.split(" ")[0]
        
    def arg2(self):
        if self.command_type == CommandType.C_PUSH or self.command_type == CommandType.C_POP:
            return self.current_command.split(" ")[2]
        else:
            return None
        
    def close_file(self):
        self.input_file.close()
        
if __name__ == "__main__":
    parser = Parser("./StackArithmetic/StackTest/StackTest.vm")
    while parser.has_more_commands():
        c = parser.commandType()
        a1 = parser.arg1()
        a2 = parser.arg2()
        print(c, a1, a2)
        parser.advance()

    parser.close_file()