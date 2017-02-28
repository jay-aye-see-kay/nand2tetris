# Converts my stored assembly functions to one tidy line
# and removed the comments
from sys import argv
from Parser import rm_comments_and_whitespace

script, filename = argv
in_txt = open(filename)
in_array = rm_comments_and_whitespace(in_txt.readlines())

filename = filename.replace(".asm",".py")
out_txt = open('clean_' + filename,'w')

for i in range(len(in_array)):
    cur_func = ""
    if in_array[i].__contains__("%%"):
        name = in_array[i].replace("%%","")
        i = i + 1
        while i < len(in_array) and in_array[i].__contains__("%%") == False:
            cur_func = cur_func + in_array[i] + '\n'
            i = i + 1
        out_txt.write('%s = %r\n' % (name, cur_func))

out_txt.close()
