import Code

def commandType(line):
	# returns current command type
	# A_COMMAND, C_COMMAND, or L_COMMAND
	if line[0] == "@":
		return "A_COMMAND"
	elif line.__contains__("=") or line.__contains__(";"):
		return "C_COMMAND"
	elif line.__contains__("(") and line.__contains__(")"):
		return "L_COMMAND"

def symbol(line):
	# returns the symbol or decimal @xxx or (xxx) of the current command
	# should only be called when commandType is A or L
	line = line.replace("@", "")
	line = line.replace("(", "")
	line = line.replace(")", "")
	return line

def dest(line):
	# returns dest mnemonic in current c command
	if line.__contains__("="): # if dest != 0
		return Code.dest(line[0:line.find("=")])
	else: # dest = 0
		return Code.dest("0")

def comp(line): # returns comp mnemonic in current c command
	# trim "dest=" part off if it exists
	if line.__contains__("="): line = line[ line.find("=")+1 : ]
	# trim "jump=" part off if it exists
	if line.__contains__(";"): line = line[ : line.find(";") ]
	# if nothing remains, comp = 0
	if line.__len__() == 0: line = "0"
	# lookup value from mnemonic and return it
	return Code.comp(line)

def jump(line):
	# returns jump mnemonic in current c command
	if line.__contains__(";"): # if the jump != 0
		return Code.jump(line[line.find(";")+1:])
	else:
		return Code.jump("0")

def rm_comments_and_whitespace(in_array):
    out_array = list()
    for line in in_array:
        if line.__contains__("//"): line = line[ : line.find("//") ]
        line = line.strip()
        if line != '': out_array.append(line)
    return out_array
