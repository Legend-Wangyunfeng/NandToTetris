class CodeWriter:
    def __init__(self, output_file):
        self.output_file = open(output_file, 'w')
        self.top = []
    def WritePushPop(self, command, segment, index):
        if command == 'push':
            if segment == 'constant':
                self.output_file.write(f'@{index}\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@SP\n')
                self.output_file.write('A=M\n')
                self.output_file.write('M=D\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')
                self.top.append(index)
            elif segment in ['local', 'argument', 'this', 'that']:
                self.output_file.write(f'@{index}\n')
                self.output_file.write('D=A\n')
                self.output_file.write(f'@{segment}\n')
                self.output_file.write('A=M+D\n')
                self.output_file.write(f'M={self.top[-1]}\n')
                self.output_file.write('@SP\n')
                self.output_file.write('M=M+1\n')
                
           
            elif segment == 'temp':
                
                self.output_file.write(f'@{index}\n')
                self.output_file.write('D=A\n')
                self.output_file.write('@5\n')
                self.output_file.write('A=M+D\n')

            elif segment == 'static':
                # todo
            else:
                raise ValueError(f'Invalid segment: {segment}')


    
    def WriteArithmetic(self, command):
        if command == 'add':
            self.output_file.write('@SP\n')
            self.output_file.write('A=M-1\n')

