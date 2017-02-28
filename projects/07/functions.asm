%%tmp_init%%
// Initialize
	// SP = 256
	@256
	D=A
	@SP
	M=D
	// LCL = 300
	@300
	D=A
	@LCL
	M=D
	// ARG = 400
	@400
	D=A
	@ARG
	M=D
	// THIS = 3000
	@3000
	D=A
	@THIS
	M=D
	// THAT = 3010
	@3010
	D=A
	@THAT
	M=D

%%push_c_x%%
	@$arg2$
	D=A		// store x in D
	@SP
	A=M		// point to top of stack
	M=D		// store x there
	@SP
	M=M+1	// M[SP]++

%%push_a_x%% // needs arg1(str) for register, and arg2(int) for value
	//LCL10 to D
	@$arg1$	// A = LCL*
	D=M		// D = LCL
	@$arg2$	// A = 5 (arg2)
	A=D+A	// A = LCL + 10 = LCL10*
	D=M		// D = LCL10
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// SP++
	@SP
	M=M+1

%%pop_a_x%%  // needs arg1(str) for register, and arg2(int) for value
	// LCLx* into D
	@$arg1$
	D=M		// D = LCL
	@$arg2$		// A = arg2
	D=D+A	// D = LCLx*
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// stack [-1] into D
	@SP
	A=M-1	// pointing to SP[-1]
	D=M		// D contains value to be popped
	// get LCLx from stack
	@SP
	A=M		// M = LCLx*
	A=M		// M = LCLx
	M=D		//LCLx = stack[-1]!!!!!!!
	@SP
	M=M-1	// SP--

%%push_t_x%% // needs arg2(int) for value
	//TempX to D
	@5		// A = Temp0
	D=A		// D = Temp0
	@$arg2$	// A = 5 (arg2)
	A=D+A	// A = LCL + 10 = LCL10*
	D=M		// D = LCL10
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// SP++
	@SP
	M=M+1

%%pop_t_x%%  // needs arg2(int) for value
	// tempx into D
	@5
	D=A		// D = Temp0
	@$arg2$		// A = arg2
	D=D+A	// D = LCLx*
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// stack [-1] into D
	@SP
	A=M-1	// pointing to SP[-1]
	D=M		// D contains value to be popped
	// get LCLx from stack
	@SP
	A=M		// M = LCLx*
	A=M		// M = LCLx
	M=D		//LCLx = stack[-1]!!!!!!!
	@SP
	M=M-1	// SP--

%%push_p_x%% // needs arg2(int) for value
	//pointer to D
	@3
	D=A		// D = pointer0
	@$arg2$	// A = arg2
	A=D+A	// A = pointer0 + arg2
	D=M		// D = LCL10
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// SP++
	@SP
	M=M+1

%%pop_p_x%%  // needs arg2(int) for value
	// pointer into D
	@3
	D=A		// D = pointer0
	@$arg2$		// A = arg2
	D=D+A	// D = pointer0 + arg2
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// stack [-1] into D
	@SP
	A=M-1	// pointing to SP[-1]
	D=M		// D contains value to be popped
	// get LCLx from stack
	@SP
	A=M		// M = LCLx*
	A=M		// M = LCLx
	M=D		//LCLx = stack[-1]!!!!!!!
	@SP
	M=M-1	// SP--

%%push_s_x%% // needs arg2(int) for value
	//static0 to D
	@16
	D=A		// D = static0
	@$arg2$	// A = arg2
	A=D+A	// A = static0 + arg2
	D=M		// D = LCL10
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// SP++
	@SP
	M=M+1

%%pop_s_x%%  // needs arg2(int) for value
	// static0 into D
	@16
	D=A		// D = static0
	@$arg2$		// A = arg2
	D=D+A	// D = static0 + arg2
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// stack [-1] into D
	@SP
	A=M-1	// pointing to SP[-1]
	D=M		// D contains value to be popped
	// get LCLx from stack
	@SP
	A=M		// M = LCLx*
	A=M		// M = LCLx
	M=D		//LCLx = stack[-1]!!!!!!!
	@SP
	M=M-1	// SP--

%%a_add%%
	@SP
	M=M-1	// move one down stack to y
	A=M		// point to top of stack
	D=M		// store y in D
	A=A-1	// move down again to x
	M=M+D	// x = x + y

%%a_sub%%
	@SP
	M=M-1	// move one down stack to y
	A=M		// point to top of stack
	D=M		// store y in D
	A=A-1	// move down again to x
	M=M-D	// x = x - y

%%a_neg%%
	@SP
	A=M
	A=A-1	// point at x
	M=-M	// x = -x, pointer doesn't move

%%a_eq%%	//if x=y return true
	@SP
	M=M-1	// move pointer to y
	A=M		// point to y
	D=M		// store y in D
	A=A-1	// pointer--
	D=M-D	// x - y
	@SP
	M=M-1	// M[SP]--
	@$block$.TRUE
	D;JEQ	// jump to true code if D=0, Continue if False
	D=0		// 0 represents False
	@SP
	A=M		// point to top of stack
	M=D		// insert false value
	@SP
	M=M+1	// move stack pointer up
	@$block$.END
	0;JMP	// all done
	($block$.TRUE)
	@0
	D=A-1	// have to enter 0 - 1, not enough bits for A = -1
	@SP
	A=M		// point to top of stack
	M=D		// insert true value
	@SP
	M=M+1	// move stack pointer up
	($block$.END)

%%a_gt%%	//if x>y return true
	@SP
	M=M-1	// move pointer to y
	A=M		// point to y
	D=M		// store y in D
	A=A-1	// pointer--
	D=M-D	// x - y
	@SP
	M=M-1	// M[SP]--
	@$block$.TRUE
	D;JGT	// jump to true code if D>0, Continue if False
	D=0		// 0 represents False
	@SP
	A=M		// point to top of stack
	M=D		// insert false value
	@SP
	M=M+1	// move stack pointer up
	@$block$.END
	0;JEQ	// all done
	($block$.TRUE)
	@0
	D=A-1	// have to enter 0 - 1, not enough bits for A = -1
	@SP
	A=M		// point to top of stack
	M=D		// insert true value
	@SP
	M=M+1	// move stack pointer up
	($block$.END)

%%a_lt%%	//if x<y return true
	@SP
	M=M-1	// move pointer to y
	A=M		// point to y
	D=M		// store y in D
	A=A-1	// pointer--
	D=M-D	// x - y
	@SP
	M=M-1	// M[SP]--
	@$block$.TRUE
	D;JLT	// jump to true code if D<0, Continue if False
	D=0		// 0 represents False
	@SP
	A=M		// point to top of stack
	M=D		// insert false value
	@SP
	M=M+1	// move stack pointer up
	@$block$.END
	0;JMP	// all done
	($block$.TRUE)
	@0
	D=A-1	// have to enter 0 - 1, not enough bits for A = -1
	@SP
	A=M		// point to top of stack
	M=D		// insert true value
	@SP
	M=M+1	// move stack pointer up
	($block$.END)

%%a_and%%
	@SP
	M=M-1	// move one down stack to y
	A=M		// point to top of stack
	D=M		// store y in D
	A=A-1	// move down again to x
	M=M&D	// x = x & y

%%a_or%%
	@SP
	M=M-1	// move one down stack to y
	A=M		// point to top of stack
	D=M		// store y in D
	A=A-1	// move down again to x
	M=M|D	// x = x or y

%%a_not%%
	@SP
	A=M		// move mem to M[SP]
	A=A-1	// point at x
	M=!M	// x = !x, pointer doesn't move
