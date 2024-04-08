from enum import Enum
from SymbolTable import SymbolTable

class CommandType(Enum):
    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2

class Parser:
    def __init__(self, input_file):
        # Opens the input file/stream and gets ready to parse it
        self.input_file = open(input_file, 'r')
        self.current_command = self.input_file.readline()
        self.name = input_file.split("/")[-1].split(".asm")[0] + ".hack"
        self.output_file = open(self.name, 'w')

        self.command_type = None
        self.symbol = ""
        self.dest = ""
        self.comp = ""
        self.jump = ""

        self.symbol_table = SymbolTable()
        self.pc = 0
        self.variable_ram = 16
        
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
        # Returns the type of the current command.
        if self.current_command[0] == "@":
            return CommandType.A_COMMAND
        elif self.current_command[0] == "(":
            return CommandType.L_COMMAND
        else:
            return CommandType.C_COMMAND

    def getSymbol(self):
        # Returns the symbol or decimal Xxx of the current command.
        # Should be called only if commandType() is A_COMMAND.
        if self.commandType() == CommandType.A_COMMAND:
            tmp = self.current_command.split("@")[1].strip()
            if not tmp.isdigit():
                if self.symbol_table.contains(tmp):
                    self.symbol = self.symbol_table.getAddress(tmp)
                else:
                    self.symbol_table.addEntry(tmp, self.variable_ram)
                    self.symbol = self.variable_ram
                    self.variable_ram += 1
            else:
                self.symbol = tmp

        elif self.commandType() == CommandType.L_COMMAND:
            self.symbol = self.current_command.split("(")[1].strip(")")
        else:
            self.symbol = ""
    
    def getDest(self):
        # Returns the dest mnemonic in the current C-command.
        # Should be called only if commandType() is C_COMMAND.
        lst = self.current_command.split("=")
        self.dest = lst[0].strip() if len(lst) > 1 else ""
    
    def getComp(self):
        # Returns the comp mnemonic in the current C-command.
        # Should be called only if commandType() is C_COMMAND.
        lst_0 = self.current_command.split("=")
        lst_1 = self.current_command.split(";")
        if len(lst_1) == 1:
            # 无跳转指令
            self.comp = lst_0[1].strip() if len(lst_0) > 1 else lst_0[0].strip()
        else:
            # 有跳转指令
            self.comp = lst_1[0].strip()

        
    def getJump(self):
        # Returns the jump mnemonic in the current C-command.
        # Should be called only if commandType() is C_COMMAND.
        lst = self.current_command.split(";")
        self.jump = lst[1].strip() if len(lst) > 1 else ""


    def reload_file(self):
        self.input_file.seek(0)
        self.current_command = self.input_file.readline()


    def close_file(self):
        self.input_file.close()
        self.output_file.close()
    