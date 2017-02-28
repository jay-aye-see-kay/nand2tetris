import os
from helper import *
from writer import *
Debug = True

#filenames = (
#'C:/Users/John/Documents/nand2tetris/projects/08/ProgramFlow/BasicLoop/BasicLoop.vm',
#'C:/Users/John/Documents/nand2tetris/projects/08/ProgramFlow/FibonacciSeries/FibonacciSeries.vm',
#'C:/Users/John/Documents/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm',
#'C:/Users/John/Documents/nand2tetris/projects/08/VM_Translator/test.vm'
#)

def main():

    path = "C:/Users/John/Documents/nand2tetris/projects/09/TextEditor/"
    os.chdir(path)

    # Get top foldername
    foldername = path[:len(path)-1]
    while foldername.find('/') != -1: foldername = foldername[foldername.find('/')+1:]

    out_txt = open(foldername + '.asm','w')
    out_txt.write(writeInit())
    block_no, call_no = 0, 1
    cur_func = 'null'

    for filename in os.listdir(path):

        if filename[len(filename)-3:] == '.vm':
            in_array = open(filename).readlines()
            in_array = rm_comments_and_whitespace(in_array)

            for line in in_array:
                cmd, arg1, arg2 = getArgs(line)
                cType = commandType(cmd)
                block_inc = False
                if Debug == True: out_txt.write("\n// %s\n" % line)

                if cType == "C_PUSH" and arg1 == 'static':
                    line = writeStaticPush(arg2, filename[:len(filename)-3])
                elif cType == "C_POP" and arg1 == 'static':
                    line = writeStaticPop(arg2, filename[:len(filename)-3])
                elif cType == "C_PUSH" or cType == "C_POP":
                    line, block_inc = writePushPop(cType, arg1, arg2)
                elif cType == "C_ARITHMETIC":
                    line, block_inc = writeArithmetic(cmd, block_no)
                elif cType == "C_LABEL":
                    line = writeLabel(arg1, cur_func)
                elif cType == "C_GOTO":
                    line = writeGoto(arg1, cur_func)
                elif cType == "C_IF":
                    line = writeIf(arg1, cur_func)
                elif cType == "C_FUNCTION":
                    cur_func = arg1
                    line = writeFunction(arg1, arg2)
                elif cType == "C_CALL":
                    line = writeCall(arg1, arg2, call_no)
                    call_no = call_no + 1
                elif cType == "C_RETURN":
                    line = writeReturn()

                out_txt.write(line)
                if block_inc: block_no = block_no + 1

    #out_txt.close()

# update asm functions and run VM Translator for every file specified at top
clean_up_functions()
#for filename in filenames:
main()
