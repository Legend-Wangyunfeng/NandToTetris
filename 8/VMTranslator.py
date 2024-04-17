from CodeWriter import CodeWriter
from Parser import Parser, CommandType
import sys, os

def parse_singleVM(parser, code_writer):

    while parser.has_more_commands():
        
        if parser.current_command:
            c = parser.commandType()
            a1 = parser.arg1()
            a2 = parser.arg2()

            if c == CommandType.C_ARITHMETIC:
                code_writer.WriteArithmetic(a1)
            elif c == CommandType.C_PUSH or c == CommandType.C_POP:
                code_writer.WritePushPop(c, a1, a2)
            elif c == CommandType.C_IF:
                code_writer.WriteIf(a1)
            elif c == CommandType.C_GOTO:
                code_writer.WriteGoTo(a1)
            elif c == CommandType.C_LABEL:
                code_writer.WriteLabel(a1)       
            elif c == CommandType.C_FUNCTION:
                code_writer.WriteFunction(a1, a2)
            elif c == CommandType.C_RETURN:
                code_writer.WriteReturn()
            elif c == CommandType.C_CALL:
                code_writer.WriteCall(a1, a2)
            else:
                raise Exception("Unknown command type")
        parser.advance()

    parser.close_file()
    code_writer.close_file()
    
if __name__ == "__main__":
    # 读取命令行参数
    target = sys.argv[1]
    # 如果target是单个.vm文件则对其调用parse_singleVM函数, 
    # 如果target是文件夹则对文件夹下的所有.vm文件调用parse_singleVM函数，并把所有生成的.asm文件写入同一个.asm文件，以文件夹名命名
    if os.path.isfile(target):
        parser = Parser(target)
        code_writer = CodeWriter(parser.name)
        parse_singleVM(parser, code_writer)

        parser.close_file()
        code_writer.close_file()
        
    elif os.path.isdir(target):
        output_file = os.path.join(target, os.path.basename(target))
        print(output_file)
        final_code_writer = CodeWriter(output_file)
        final_code_writer.bootstrap()

        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith(".vm"):
                    parser = Parser(os.path.join(root, file))
                    code_writer = CodeWriter(parser.name)
                    parse_singleVM(parser, code_writer)
                    parser.close_file()
                
                    with open(parser.name + '.asm', "r") as f:
                        final_code_writer.Write(f.read())

        final_code_writer.close_file()
    else:
        raise Exception("Invalid target")
    


    