
// function SimpleFunction.test 2
(SimpleFunction.test)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// push local 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@LCL
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D

// not
@SP
A=M
A=A-1
M=!M

// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D

// push argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// return
@LCL
D=M
@R13
M=D
@R13
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@R14
M=D
@SP
A=M
A=A-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
A=M
A=A-1
D=M
@THAT
M=D
@R13
A=M
A=A-1
A=A-1
D=M
@THIS
M=D
@R13
A=M
A=A-1
A=A-1
A=A-1
D=M
@ARG
M=D
@R13
A=M
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
