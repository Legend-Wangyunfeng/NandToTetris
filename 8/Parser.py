from enum import Enum


class CommandType(Enum):
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_IF = 4
    C_GOTO = 5

class Parser:
    def __init__(self, input_file):
        # Opens the input file/stream and gets ready to parse it
        self.input_file = open(input_file, 'r')
        self.current_command = self.input_file.readline()
        self.name = input_file.split(".vm")[0]

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
            self.command_type = CommandType.C_PUSH
        elif self.current_command.startswith("pop"):
            self.command_type = CommandType.C_POP
        elif self.current_command.startswith("label"):
            self.command_type = CommandType.C_LABEL
        elif self.current_command.startswith("if-goto"):
            self.command_type = CommandType.C_IF
        elif self.current_command.startswith("goto"):
            self.command_type = CommandType.C_GOTO
        else:
            self.command_type = CommandType.C_ARITHMETIC

        return self.command_type  
        
    def arg1(self):
        if self.command_type == None:
            self.commandType()

        if self.command_type in [CommandType.C_POP, CommandType.C_PUSH, CommandType.C_LABEL, CommandType.C_IF, CommandType.C_GOTO]:
            return self.current_command.split(" ")[1]
        elif self.command_type == CommandType.C_ARITHMETIC:
            return self.current_command.split(" ")[0]
        
    def arg2(self):
        if self.command_type == CommandType.C_PUSH or self.command_type == CommandType.C_POP:
            return self.current_command.split(" ")[2]
        else:
            return None
        
    def close_file(self):
        self.input_file.close()
        
