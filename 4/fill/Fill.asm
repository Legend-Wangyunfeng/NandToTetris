// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
@8192
D=A
@final
M=D

(Loop1)
    @i
    M=0

    @KBD
    D=M

    @Loop3
    D;JEQ

    @i
    M=0

    (Loop2)
        @i
        D=M
        @SCREEN
        A=A+D
        M=-1

        @1
        D=A
        @i
        M=D+M
        
        @final
        D=M 
        @i
        D=D-M
        @Loop2
        D;JGT

        @Loop1
        0;JEQ
    
    

    (Loop3)
        @i
        D=M
        @SCREEN
        A=A+D
        M=0

        @1
        D=A
        @i
        M=D+M
        
        @final
        D=M 
        @i
        D=D-M
        @Loop3
        D;JGT

        @Loop1
        0;JEQ
