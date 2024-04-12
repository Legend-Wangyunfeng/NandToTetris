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
        code_writer.bootstrap()
        parse_singleVM(parser, code_writer)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith(".vm"):
                    parser = Parser(os.path.join(root, file))
                    code_writer = CodeWriter(parser.name)
                    parse_singleVM(parser, code_writer)
        # 把所有生成的.asm文件写入同一个.asm文件，以文件夹名命名

        output_file = os.path.join(target, os.path.basename(target) + ".asm")
        print(output_file)
        with open(output_file, "w") as f:
            output_file.write('@256\n')
            output_file.write('D=A\n')
            output_file.write('@SP\n')
            output_file.write('M=D\n')
            WriteCall('Sys.init', '0')
            for file in files:
                if file.endswith(".asm"):
                    with open(os.path.join(root, file), "r") as g:
                        f.write(g.read())

    else:
        raise Exception("Invalid target")
    


    