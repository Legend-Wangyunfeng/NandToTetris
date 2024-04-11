// CommandType.C_PUSH argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D

// CommandType.C_PUSH constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP that 0
@THAT
D=M
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// CommandType.C_PUSH constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP that 1
@THAT
D=M
@1
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// CommandType.C_PUSH argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_PUSH constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
// CommandType.C_POP argument 0
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

(LOOP)
// CommandType.C_PUSH argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
@END
0;JMP
(COMPUTE_ELEMENT)
// CommandType.C_PUSH that 0
@0
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_PUSH that 1
@1
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
// CommandType.C_POP that 2
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// CommandType.C_PUSH pointer 1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_PUSH constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
// CommandType.C_POP pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D

// CommandType.C_PUSH argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_PUSH constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
// CommandType.C_POP argument 0
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

@LOOP
0;JMP
(END)
