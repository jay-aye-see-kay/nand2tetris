def commandType(line):
    # trim lines well before they get here
    # returns C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION,
    # C_CALL. C_ARITHMETIC is returned for ALL arithmetic commands
    if line == "add" or line == "sub" or line == "neg" or line == "eq" or line == "gt" or line == "lt" or line == "and" or line == "or" or line == "not":
        return "C_ARITHMETIC"
    elif line[0:4] == "push":
        return "C_PUSH"
    elif line[0:3] == "pop":
        return "C_POP"
    else:
        return ""

def arg1(line):
    # return first arg (string) of command, don't run for C_RETURN
    space1 = line.find(" ")
    space2 = line.find(" ", space1 + 1)

    if space1 == -1: return line
    if space2 == -1: space2 = len(line)

    return line[ space1 + 1 : space2 ]

def arg2(line):
    # return 2nd arg (int) of command, only run for C_PUSH,
    # C_POP, C_FUNCTION, C_CALL
    space1 = line.find(" ")
    space2 = line.find(" ", space1 + 1)

    if space1 == -1: return line
    if space2 == -1: space2 = len(line)

    return int(line[ space2 + 1 : ])

def rm_comments_and_whitespace(in_array):
    out_array = list()
    for line in in_array:
        if line.__contains__("//"): line = line[ : line.find("//") ]
        line = line.strip()
        if line != '': out_array.append(line)
    return out_array
