from CodeWriter import CodeWriter
from Parser import Parser, CommandType
import sys
if __name__ == "__main__":
    # 读取命令行参数
    
    parser = Parser(sys.argv[1])
    code_writer = CodeWriter(parser.name)
    while parser.has_more_commands():
        
        if parser.current_command:
            c = parser.commandType()
            a1 = parser.arg1()
            a2 = parser.arg2()
            print(c, a1, a2)
            if c == CommandType.C_ARITHMETIC:
                code_writer.WriteArithmetic(a1)
            elif c == CommandType.C_PUSH or c == CommandType.C_POP:
                code_writer.WritePushPop(c, a1, a2)
            else:
                raise ValueError(f'Invalid command')
        parser.advance()
    parser.close_file()