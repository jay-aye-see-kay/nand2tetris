@256
D=A
@SP
M=D
@300
D=A
@LCL
M=D
@400
D=A
@ARG
M=D
@3000
D=A
@THIS
M=D
@3010
D=A
@THAT
M=D

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block0.TRUE
D;JEQ
D=0
@SP
A=M
M=D
@SP
M=M+1
@block0.END
0;JMP
(block0.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block0.END)

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block1.TRUE
D;JEQ
D=0
@SP
A=M
M=D
@SP
M=M+1
@block1.END
0;JMP
(block1.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block1.END)

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block2.TRUE
D;JEQ
D=0
@SP
A=M
M=D
@SP
M=M+1
@block2.END
0;JMP
(block2.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block2.END)

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block3.TRUE
D;JLT
D=0
@SP
A=M
M=D
@SP
M=M+1
@block3.END
0;JMP
(block3.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block3.END)

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block4.TRUE
D;JLT
D=0
@SP
A=M
M=D
@SP
M=M+1
@block4.END
0;JMP
(block4.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block4.END)

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block5.TRUE
D;JLT
D=0
@SP
A=M
M=D
@SP
M=M+1
@block5.END
0;JMP
(block5.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block5.END)

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block6.TRUE
D;JGT
D=0
@SP
A=M
M=D
@SP
M=M+1
@block6.END
0;JEQ
(block6.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block6.END)

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block7.TRUE
D;JGT
D=0
@SP
A=M
M=D
@SP
M=M+1
@block7.END
0;JEQ
(block7.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block7.END)

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
M=M-1
@block8.TRUE
D;JGT
D=0
@SP
A=M
M=D
@SP
M=M+1
@block8.END
0;JEQ
(block8.TRUE)
@0
D=A-1
@SP
A=M
M=D
@SP
M=M+1
(block8.END)

// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 53
@53
D=A
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

// push constant 112
@112
D=A
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

// neg
@SP
A=M
A=A-1
M=-M

// and
@SP
M=M-1
A=M
D=M
A=A-1
M=M&D

// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
@SP
M=M-1
A=M
D=M
A=A-1
M=M|D

// not
@SP
A=M
A=A-1
M=!M
