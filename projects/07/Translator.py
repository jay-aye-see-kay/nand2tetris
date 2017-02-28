from sys import argv
from Parser import commandType, arg1, arg2, rm_comments_and_whitespace
from CWriter import writePushPop, writeArithmetic
from clean_functions import *
Debug = True

def main(filename):
    in_txt = open(filename)
    in_array = in_txt.readlines()
    in_array = rm_comments_and_whitespace(in_array)
    # Remove any folders from the filename
    while filename.find('/') != -1: filename = filename[filename.find('/')+1:]
    out_txt = open(filename.replace(".vm", ".asm"),'w')
    out_txt.write(tmp_init)

    block_no = 0
    for line in in_array:
        cType = commandType(line)
        if Debug == True: out_txt.write("\n// %s\n" % line)
        if cType == "C_PUSH" or cType == "C_POP":
            line, block_inc = writePushPop(cType, arg1(line), arg2(line))
            out_txt.write(line)
        elif cType == "C_ARITHMETIC":
            line, block_inc = writeArithmetic(arg1(line), block_no)
            out_txt.write(line)
        if block_inc: block_no = block_no + 1

    out_txt.close()

#script, filename = argv
#main(filename)
