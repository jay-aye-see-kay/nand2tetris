from sys import argv
import Parser, Code

# Open .asm file and assign it to in_txt
script, filename = argv
in_txt = open(filename)

# create output file assigned to out_txt and change extension
out_txt = open(filename.replace(".asm", ".hack"),'w')
# create array from lines in input file, loop through and process
in_array = in_txt.readlines()
in_array = rm_comments_and_whitespace(in_array)

# --------  -------- first pass --------  --------
# add labels to symbol table
ROM_Address = 0
symbol_table = Code.symbol_table

for line in in_array:
    cType = Parser.commandType(line)     # get the command type
    if cType == "A_COMMAND" or cType == "C_COMMAND":
        ROM_Address = ROM_Address + 1
    elif cType == "L_COMMAND":
        symbol_table[Parser.symbol(line)] = ROM_Address

# --------  -------- second pass --------  --------
# add variables to symbol table, and substitute for numbers
RAM_Address = 32
pro_array = list()
for line in in_array:
    if Parser.commandType(line) == "A_COMMAND":
        instruction = Parser.symbol(line)
        try:
            int(instruction)
            pass
        except ValueError:
            if not symbol_table.has_key(instruction):
                symbol_table[instruction] = RAM_Address
                RAM_Address = RAM_Address + 1
            line = "@" + instruction.replace(instruction, str(symbol_table[instruction]))

    pro_array.append(line)

# --------  -------- third pass --------  --------
# translate to binary
for line in pro_array:
    cType = Parser.commandType(line)     # get the command type

    if cType == "A_COMMAND":
    	out = Parser.symbol(line)
    	out = format(int(out), 'b').zfill(16)
    	out_txt.write("%s\n" % out)

    elif cType == "C_COMMAND":
    	out = "111" + Parser.comp(line) + Parser.dest(line) + Parser.jump(line)
    	out_txt.write("%s\n" % out)

    else:
    	pass

out_txt.close()
