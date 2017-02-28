// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@i
M=1 // Set i to 1
@R2
M=0 // Set sum to 0

(LOOP)
	@i
	D=M
	@R0
	D=D-M
	@END
	D;JGT // If i>x end loop
	
	@R1
	D=M
	@R2
	M=M+D // R2 = R2 + y
	
	@i
	M=M+1 // i++
	@LOOP
	0;JMP // Jump to start of loop

(END)
@END
0;JMP