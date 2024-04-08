import sys
from Code import Ccode, Acode
from Parser import Parser, CommandType

if __name__ == "__main__":

    parser = Parser(sys.argv[1])
    acode = Acode()
    ccode = Ccode()

    # 一次遍历
    while parser.has_more_commands():
        if parser.current_command:
            
            if parser.commandType() == CommandType.L_COMMAND:
                parser.getSymbol()
                if not parser.symbol_table.contains(parser.symbol):
                    parser.symbol_table.addEntry(parser.symbol, parser.pc)
            else:
                parser.pc += 1
        parser.advance()
        
    parser.reload_file()
    parser.pc = 0
    # 二次遍历
    while parser.has_more_commands():
        # print(parser.current_command)
        if parser.current_command:
            if parser.commandType() == CommandType.A_COMMAND:
                parser.getSymbol()
                acode.getBinary(parser.symbol)
                parser.output_file.write(f"{acode.binary}")
            elif parser.commandType() == CommandType.C_COMMAND:
                parser.getJump()
                parser.getDest()
                parser.getComp()
            
                ccode.getDest(parser.dest)
                ccode.getComp(parser.comp)
                ccode.getJump(parser.jump)
                ccode.getBinary()
                parser.output_file.write(f"{ccode.binary}")
        parser.advance()

    parser.close_file()