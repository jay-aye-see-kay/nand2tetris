%%init%%
// Initialize
	// SP = $SP$
	@$SP$
	D=A
	@SP
	M=D
	// LCL = $LCL$
	@$LCL$
	D=A
	@LCL
	M=D
	// ARG = $ARG$
	@$ARG$
	D=A
	@ARG
	M=D
	// THIS = $THIS$
	@$THIS$
	D=A
	@THIS
	M=D
	// THAT = $THAT$
	@$THAT$
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

%%push_s_x%% // needs $arg2$ and $f_name$
	@$f_name$.$arg2$
	D=M				// getting static f.x -> D
	@16
	// D to stack
	@SP		// A = SP*
	A=M		// A = SP
	M=D		// M[SP] = D
	// SP++
	@SP
	M=M+1

%%pop_s_x%%  // needs $arg2$ and $f_name$
	// SP--
	@SP
	M=M-1
	// SP -> D
	@SP
	A=M		// pointing to SP
	D=M		// D contains value to be popped
	// D -> static f.x
	@$f_name$.$arg2$
	M=D				// getting D -> static f.x

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

	%%if_goto%%
	@SP
	M=M-1  // move SP down one
	A=M
	D=M		// set D to top of stack
	@$label$
	D;JNE		// jump if D != 0

%%f_call%% //call %f_name% %n% (+ $RCALLNO$)
	// push r_address, using the label declared below
	@RET_ADDRESS_CALL$RCALLNO$
	D=A		// store address in D
	@SP
	A=M		// point to top of stack
	M=D		// store x there
	@SP
	M=M+1	// M[SP]++

	// push LCL, save the LCL of the calling function
	@LCL
	D=M		// store x in D
	@SP
	A=M		// point to top of stack
	M=D		// store x there
	@SP
	M=M+1	// M[SP]++

	// push ARG, save the ARG of the calling function
	@ARG
	D=M		// store x in D
	@SP
	A=M		// point to top of stack
	M=D		// store x there
	@SP
	M=M+1	// M[SP]++

	// push THIS, save the THIS of the calling function
	@THIS
	D=M		// store x in D
	@SP
	A=M		// point to top of stack
	M=D		// store x there
	@SP
	M=M+1	// M[SP]++

	// push THAT, save the THAT of the calling function
	@THAT
	D=M		// store x in D
	@SP
	A=M		// point to top of stack
	M=D		// store x there
	@SP
	M=M+1	// M[SP]++

	// ARG = SP-n-5, reposition ARG (n = number of args)
	@SP
	D=M		// SP -> D
	@$n$	// n is number of inputs
	D=D-A
	@5
	D=D-A	// D = SP-n-5
	@ARG
	M=D		// ARG = SP-n-5

	// LCL = SP, reposition LCL
	@SP
	D=M
	@LCL
	M=D		// LCL = SP

	// goto f, transfer control
	@$f_name$
	0; JMP

	// (r_address), declare a label for the return address
	(RET_ADDRESS_CALL$RCALLNO$)

%%f_return%%
	// FRAME(R13) = LCL
	@LCL
	D=M		// LCL -> D
	@R13
	M=D		// D -> R13

	//RET = *(FRAME-5)
	@R13
	D=M			//D=FRAME
	@5
	A=D-A		// A=FRAME-5
	D=M
	@R14
	M=D		// Return address -> R14

	//*ARG = pop(), put the return value in *ARG
	@SP
	A=M
	A=A-1	// *SP-1
	D=M		// D = return value
	@ARG
	A=M		// *ARG
	M=D		// *ARG = *(SP-1)

	//SP =  ARG + 1, restore the SP of the caller
	@ARG
	D=M+1
	@SP
	M=D

	//THAT = *(FRAME - 1), restore THAT of the caller
	@R13
	A=M		// pointing at *FRAME
	A=A-1	// pointing at *(FRAME-1)
	D=M
	@THAT
	M=D		// Old that -> that

	//THIS = *(FRAME - 2), restore THIS of the caller
	@R13
	D=M			//D=FRAME
	@2
	A=D-A		// A=FRAME-5
	D=M
	@THIS
	M=D

	//ARG = *(FRAME - 3), restore ARG of the caller
	@R13
	D=M			//D=FRAME
	@3
	A=D-A		// A=FRAME-5
	D=M
	@ARG
	M=D

	//LCL = *(FRAME - 4), restore LCL of the caller
	@R13
	D=M			//D=FRAME
	@4
	A=D-A		// A=FRAME-5
	D=M
	@LCL
	M=D

	//goto RET, go to return address (found in the caller's code)
	@R14
	A=M
	0;JMP
