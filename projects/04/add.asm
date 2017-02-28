// Adds two numbers
// Usage: adds values in RAM[0] and RAM[1], outputs result to RAM[2]

@0
D=M

@1
D=D+M

@2
M=D

(END)
@END
0;JMP