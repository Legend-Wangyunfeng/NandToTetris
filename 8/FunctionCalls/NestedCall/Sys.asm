(Sys.init)
// CommandType.C_PUSH constant 4000	
@4000	
D=A
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D

// CommandType.C_PUSH constant 5000
@5000
D=A
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

@Sys.main$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(Sys.main$ret.0)
// CommandType.C_POP temp 1
@1
D=A
@5
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
@LOOP
0;JMP
(Sys.main)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
// CommandType.C_PUSH constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D

// CommandType.C_PUSH constant 5001
@5001
D=A
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

// CommandType.C_PUSH constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP local 1
@LCL
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

// CommandType.C_PUSH constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP local 2
@LCL
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

// CommandType.C_PUSH constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP local 3
@LCL
D=M
@3
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

// CommandType.C_PUSH constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

@Sys.add12$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(Sys.add12$ret.1)
// CommandType.C_POP temp 0
@0
D=A
@5
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

// CommandType.C_PUSH local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_PUSH local 1
@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_PUSH local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_PUSH local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_PUSH local 4
@4
D=A
@LCL
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
@LCL
D=M
@R15
M=D
@5
A=D-A
D=M
@R14
M=D
// pop argument 0
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

@ARG
D=M
@SP
M=D+1
@R15
A=M-1
D=M
@THAT
M=D
@R15
D=M
@2
A=D-A
D=M
@THIS
M=D
@R15
D=M
@3
A=D-A
D=M
@ARG
M=D
@R15
D=M
@4
A=D-A
D=M
@LCL
M=D
@R14
A=M
0;JMP
(Sys.add12)
// CommandType.C_PUSH constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// CommandType.C_POP pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D

// CommandType.C_PUSH constant 5002
@5002
D=A
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

// CommandType.C_PUSH constant 12
@12
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
@LCL
D=M
@R15
M=D
@5
A=D-A
D=M
@R14
M=D
// pop argument 0
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

@ARG
D=M
@SP
M=D+1
@R15
A=M-1
D=M
@THAT
M=D
@R15
D=M
@2
A=D-A
D=M
@THIS
M=D
@R15
D=M
@3
A=D-A
D=M
@ARG
M=D
@R15
D=M
@4
A=D-A
D=M
@LCL
M=D
@R14
A=M
0;JMP
