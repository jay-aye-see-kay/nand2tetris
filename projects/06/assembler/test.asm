@256	//A=256,D=0,M=0
D=A		//A=256,D=256,M=0
@SP		//A=SP,D=256,M=0
M=D		//A=SP,D=256,M=256
@4		//A=4,D=?,M=?
D=A		//A=4,D=4,M=?
@SP		//A=SP,D=4,M=256
A=M		//A=256,D=4,M=0
M=4		//A=256,D=4,M=4
@SP		//A=SP,D=?,M=256
A=M		//A=256,D=?,M=4
D=A+1	//A=256,D=257,M=4
@SP		//A=SP,D=257,M=256
M=D		//A=SP,D=257,M=257
@5		//A=4,D=?,M=?
D=A		//A=4,D=5,M=?
@SP		//A=SP,D=5,M=256
A=M		//A=256,D=5,M=0
M=4		//A=256,D=5,M=5
@SP
A=M
D=A+1
@SP
M=D