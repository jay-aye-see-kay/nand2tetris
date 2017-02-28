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

    elif command == "C_PUSH" and segment == "static":
        push_asm = push_s_x.replace("$arg2$", str(index))
        return push_asm, False
    elif command == "C_POP" and segment == "static":
        pop_asm = pop_s_x.replace("$arg2$", str(index))
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
