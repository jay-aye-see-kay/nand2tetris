from tables import *
from clean_functions import *

def commandType(word):
    # split line into words, first word is the command, get command from dict
    if not commands.has_key(word):
        return "Error: command not found"
    else:
        return commands[word]

def rm_comments_and_whitespace(in_array):
    # removes; commments, leading and trailing whitespace, empty array elements
    out_array = list()
    for line in in_array:
        if line.__contains__("//"): line = line[ : line.find("//") ]
        line = line.strip()
        if line != '': out_array.append(line)
    return out_array

def getArgs(line):
    # split the line into it's 3 arguments, returns '' for arguments not present
    line = line.split(' ')
    cmd = line[0]
    arg1, arg2 = '', ''
    if len(line) > 1: arg1 = line[1]
    if len(line) > 2: arg2 = line[2]
    return cmd, arg1, arg2

def clean_up_functions():
    # open fuctions .asm
    in_txt = open('VMT/functions.asm')
    out_txt = open('VMT/clean_functions.py', 'w')

    in_array = rm_comments_and_whitespace(in_txt.readlines())

    for i in range(len(in_array)):
        cur_func = ""
        if in_array[i].__contains__("%%"):
            name = in_array[i].replace("%%","")
            i = i + 1
            while i < len(in_array) and in_array[i].__contains__("%%") == False:
                cur_func = cur_func + in_array[i] + '\n'
                i = i + 1
            out_txt.write('%s = %r\n' % (name, cur_func))

    in_txt.close()
    out_txt.close()
