from Parser import CommandType

class CodeWriter:

    segment_map = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
    }

    def __init__(self, file_name):
        self.file_name = file_name
        self.output_file = open(file_name + '.asm', 'w')
        self.count = 0

    def WritePushPop(self, command, segment, index):
        self.output_file.write(f'// {command} {segment} {index}\n')
        if command == CommandType.C_PUSH:
            if segment == 'constant':
                self.output_file.write(f'@{index}\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')

            elif segment in ['local', 'argument', 'this', 'that']:
                self.output_file.write(f'@{index}\n')
                self.output_file.write('D=A\n')
                self.output_file.write(f'@{CodeWriter.segment_map[segment]}\n')
                self.output_file.write('A=D+M\n')
                self.output_file.write('D=M\n')
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')
                        
            elif segment == 'temp':
                self.output_file.write(f'@{index}\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@5\n')
                self.output_file.write('A=D+A\n')
                self.output_file.write('D=M\n')
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')

            elif segment == 'static':
                self.output_file.write(f'@{self.file_name.split("/")[-1]}.{index}\n')
                self.output_file.write('D=M\n')
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')
                
            elif segment == 'pointer':
                if index == '0':
                    self.output_file.write('@THIS\n')
                elif index == '1':
                    self.output_file.write('@THAT\n')
                else:
                    raise ValueError(f'Invalid index for pointer segment: {index}')
                self.output_file.write('D=M\n')
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')
                
            else:
                raise ValueError(f'Invalid segment: {segment}')
        
        else:
            if segment in ['local', 'argument', 'this', 'that']:
                self.output_file.write(f'@{CodeWriter.segment_map[segment]}\n')
                self.output_file.write('D=M\n')
                self.output_file.write(f'@{index}\n')
                self.output_file.write('D=D+A\n')
                self.output_file.write('@R13\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M-1\n')
                self.output_file.write('A=M\n')
                self.output_file.write('D=M\n')
                self.output_file.write('@R13\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                
            elif segment == 'temp':
                self.output_file.write(f'@{index}\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@5\n')
                self.output_file.write('D=D+A\n')
                self.output_file.write('@R13\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M-1\n')
                self.output_file.write('A=M\n')
                self.output_file.write('D=M\n')
                self.output_file.write('@R13\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                
            elif segment == 'static':
                self.output_file.write('@SP\n')
                self.output_file.write('M=M-1\n')
                self.output_file.write('A=M\n')
                self.output_file.write('D=M\n')
                self.output_file.write(f'@{self.file_name.split("/")[-1]}.{index}\n')
                self.output_file.write('M=D\n')
                
            elif segment == 'pointer':
                self.output_file.write('@SP\n')
                self.output_file.write('M=M-1\n')
                self.output_file.write('A=M\n')
                self.output_file.write('D=M\n')
                if index == '0':
                    self.output_file.write('@THIS\n')
                elif index == '1':
                    self.output_file.write('@THAT\n')
                else:
                    raise ValueError(f'Invalid index for pointer segment: {index}')
                self.output_file.write('M=D\n')
                
          
            else:
                raise ValueError(f'Invalid segment: {segment}')
        self.output_file.write('\n')

    def WriteArithmetic(self, command):
        if command == 'add':
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=D+M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
            
        elif command == 'sub':
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=M-D\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
    
        elif command == 'neg':
            self.output_file.write('@SP\n')
            self.output_file.write('A=M-1\n')
            self.output_file.write('M=-M\n')

        elif command == 'and':
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=D&M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
            
        elif command == 'or':
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=D|M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
            
        elif command == 'not':
            self.output_file.write('@SP\n')
            self.output_file.write('A=M-1\n')
            self.output_file.write('M=!M\n')

            
        elif command == 'eq':
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M-D\n')
            self.output_file.write(f'@TRUE_EQ_{self.count}\n')
            self.output_file.write('D;JEQ\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=0\n')
            self.output_file.write(f'@CONTINUE_EQ_{self.count}\n')
            self.output_file.write('0;JMP\n')
            self.output_file.write(f'(TRUE_EQ_{self.count})\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=-1\n')
            self.output_file.write(f'(CONTINUE_EQ_{self.count})\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
            self.count += 1
            
        elif command == 'gt':
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M-D\n')
            self.output_file.write(f'@TRUE_GT_{self.count}\n')
            self.output_file.write('D;JGT\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=0\n')
            self.output_file.write(f'@CONTINUE_GT_{self.count}\n')
            self.output_file.write('0;JMP\n')
            self.output_file.write(f'(TRUE_GT_{self.count})\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=-1\n')
            self.output_file.write(f'(CONTINUE_GT_{self.count})\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
            self.count += 1
            
        elif command == 'lt':
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M-1\n')
            self.output_file.write('A=M\n')
            self.output_file.write('D=M-D\n')
            self.output_file.write(f'@TRUE_LT_{self.count}\n')
            self.output_file.write('D;JLT\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=0\n')
            self.output_file.write(f'@CONTINUE_LT_{self.count}\n')
            self.output_file.write('0;JMP\n')
            self.output_file.write(f'(TRUE_LT_{self.count})\n')
            self.output_file.write('@SP\n')
            self.output_file.write('A=M\n')
            self.output_file.write('M=-1\n')
            self.output_file.write(f'(CONTINUE_LT_{self.count})\n')
            self.output_file.write('@SP\n')
            self.output_file.write('M=M+1\n')
            self.count += 1
            
        else:
            raise ValueError(f'Invalid arithmetic command: {command}')

    def WriteLabel(self, label):
        self.output_file.write(f'({label})\n')

    def WriteGoTo(self, label):
        self.output_file.write(f'@{label}\n')
        self.output_file.write('0;JMP\n')

    def WriteIf(self,label):
        self.output_file.write('@SP\n')
        self.output_file.write('M=M-1\n')
        self.output_file.write('A=M\n')
        self.output_file.write('D=M\n')
        self.output_file.write(f'@{label}\n')
        self.output_file.write('D;JNE\n')


    def close_file(self):
        self.output_file.close()

