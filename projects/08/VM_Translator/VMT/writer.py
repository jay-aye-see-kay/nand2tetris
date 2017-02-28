from clean_functions import *

arg1_dict = {
"local":"LCL",
"argument":"ARG",
"this":"THIS",
"that":"THAT"
}

def writeArithmetic(command, block_no):
    # write the translated command to file
    if command == "add":
        return a_add, False
    elif command == "sub":
        return a_sub, False
    elif command == "neg":
        return a_neg, False
    elif command == "eq":
        return a_eq.replace('$block$', ("block%s" % block_no)), True
    elif command == "gt":
        return a_gt.replace('$block$', ("block%s" % block_no)), True
    elif command == "lt":
        return a_lt.replace('$block$', ("block%s" % block_no)), True
    elif command == "and":
        return a_and, False
    elif command == "or":
        return a_or, False
    elif command == "not":
        return a_not, False

def writePushPop(command, segment, index):
    # write the given push or pop command to file
    if command == "C_PUSH" and segment == "constant":
        push_asm = push_c_x.replace("$arg2$", str(index))
        return push_asm, False

    elif command == "C_PUSH" and segment == "temp":
        push_asm = push_t_x.replace("$arg2$", str(index))
        return push_asm, False
    elif command == "C_POP" and segment == "temp":
        pop_asm = pop_t_x.replace("$arg2$", str(index))
        return pop_asm, False

    elif command == "C_PUSH" and segment == "pointer":
        push_asm = push_p_x.replace("$arg2$", str(index))
        return push_asm, False
    elif command == "C_POP" and segment == "pointer":
        pop_asm = pop_p_x.replace("$arg2$", str(index))
        return pop_asm, False

    elif command == "C_PUSH":
        arg1 = arg1_dict[segment]
        push_asm = push_a_x.replace("$arg2$", str(index))
        push_asm = push_asm.replace("$arg1$", arg1)
        return push_asm, False
    elif command == "C_POP":
        arg1 = arg1_dict[segment]
        pop_asm = pop_a_x.replace("$arg2$", str(index))
        pop_asm = pop_asm.replace("$arg1$", arg1)
        return pop_asm, False

def writeStaticPush(index, filename):
    push_asm = push_s_x.replace("$f_name$", filename)
    push_asm = push_asm.replace("$arg2$", str(index))
    return push_asm

def writeStaticPop(index, filename):
    pop_asm = pop_s_x.replace("$f_name$", filename)
    pop_asm = pop_asm.replace("$arg2$", str(index))
    return pop_asm

def writeInit():
    # Replaces the SP, ARG, THIS, and THAT values, returns init code.
    out = writeCall('Sys.init', 0, 0)
    return '@256\nD=A\n@SP\nM=D\n' + out

def writeLabel(label, func):
    # returns assembly code of a label within a fucntion (func$label)
    return '(' + str(func) + '$' + str(label) + ')\n'

def writeGoto(label, func):
    # returns assembly code of an unconditional jump to func$label
    return '@' + str(func) + '$' + str(label) + '\n0;JMP\n'

def writeIf(label, func):
    # returns assembly code of a jump if top of stack !=0: to func$label
    return if_goto.replace('$label$', str(func) + '$' + str(label))

def writeFunction(arg1, arg2):
    # writes a label fuction start then pushes one 0 onto the stack for each arg2
    line = '(' + str(arg1) + ')\n'
    arg2 = int(arg2)
    if arg2 > 0:
        for arg in range(arg2):
            line = line + push_c_x.replace("$arg2$", '0')
    return line

def writeCall(arg1, arg2, call_no):
    # writes the return code
    out = f_call.replace('$f_name$', arg1)
    out = out.replace('$n$', str(arg2))
    return out.replace('$RCALLNO$', str(call_no))

def writeReturn():
    # writes the return code
    return f_return
