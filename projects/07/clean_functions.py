tmp_init = '@256\nD=A\n@SP\nM=D\n@300\nD=A\n@LCL\nM=D\n@400\nD=A\n@ARG\nM=D\n@3000\nD=A\n@THIS\nM=D\n@3010\nD=A\n@THAT\nM=D\n'
push_c_x = '@$arg2$\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
push_a_x = '@$arg1$\nD=M\n@$arg2$\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
pop_a_x = '@$arg1$\nD=M\n@$arg2$\nD=D+A\n@SP\nA=M\nM=D\n@SP\nA=M-1\nD=M\n@SP\nA=M\nA=M\nM=D\n@SP\nM=M-1\n'
push_t_x = '@5\nD=A\n@$arg2$\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
pop_t_x = '@5\nD=A\n@$arg2$\nD=D+A\n@SP\nA=M\nM=D\n@SP\nA=M-1\nD=M\n@SP\nA=M\nA=M\nM=D\n@SP\nM=M-1\n'
push_p_x = '@3\nD=A\n@$arg2$\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
pop_p_x = '@3\nD=A\n@$arg2$\nD=D+A\n@SP\nA=M\nM=D\n@SP\nA=M-1\nD=M\n@SP\nA=M\nA=M\nM=D\n@SP\nM=M-1\n'
push_s_x = '@16\nD=A\n@$arg2$\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
pop_s_x = '@16\nD=A\n@$arg2$\nD=D+A\n@SP\nA=M\nM=D\n@SP\nA=M-1\nD=M\n@SP\nA=M\nA=M\nM=D\n@SP\nM=M-1\n'
a_add = '@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M+D\n'
a_sub = '@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M-D\n'
a_neg = '@SP\nA=M\nA=A-1\nM=-M\n'
a_eq = '@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@SP\nM=M-1\n@$block$.TRUE\nD;JEQ\nD=0\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@$block$.END\n0;JMP\n($block$.TRUE)\n@0\nD=A-1\n@SP\nA=M\nM=D\n@SP\nM=M+1\n($block$.END)\n'
a_gt = '@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@SP\nM=M-1\n@$block$.TRUE\nD;JGT\nD=0\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@$block$.END\n0;JEQ\n($block$.TRUE)\n@0\nD=A-1\n@SP\nA=M\nM=D\n@SP\nM=M+1\n($block$.END)\n'
a_lt = '@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@SP\nM=M-1\n@$block$.TRUE\nD;JLT\nD=0\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@$block$.END\n0;JMP\n($block$.TRUE)\n@0\nD=A-1\n@SP\nA=M\nM=D\n@SP\nM=M+1\n($block$.END)\n'
a_and = '@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M&D\n'
a_or = '@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M|D\n'
a_not = '@SP\nA=M\nA=A-1\nM=!M\n'
