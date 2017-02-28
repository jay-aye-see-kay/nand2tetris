import os
from Parser import rm_comments_and_whitespace
from Translator import main

vms = {
0: "/StackArithmetic/SimpleAdd/SimpleAdd.vm",
1: "/StackArithmetic/StackTest/StackTest.vm",
2: "/MemoryAccess/BasicTest/BasicTest.vm",
3: "/MemoryAccess/PointerTest/PointerTest.vm",
4: "/MemoryAccess/StaticTest/StaticTest.vm"
}
asms = {
0: "/StackArithmetic/SimpleAdd/SimpleAdd.asm",
1: "/StackArithmetic/StackTest/StackTest.asm",
2: "/MemoryAccess/BasicTest/BasicTest.asm",
3: "/MemoryAccess/PointerTest/PointerTest.asm",
4: "/MemoryAccess/StaticTest/StaticTest.asm"
}
outs = {
0: "SimpleAdd.asm",
1: "StackTest.asm",
2: "BasicTest.asm",
3: "PointerTest.asm",
4: "StaticTest.asm"
}

def test_it():
    # for each vm file, translate it to current directory then open it and
    # compare it with the last asm file (known correct)
    for i in range(5):
        main(os.getcwd() + vms[i])

        old_txt = open(os.getcwd() + asms[i])
        old_array = old_txt.readlines()
        old_array = rm_comments_and_whitespace(old_array)

        new_txt = open(outs[i])
        new_array = new_txt.readlines()
        new_array = rm_comments_and_whitespace(new_array)

        if len(old_array) != len(new_array):
            print "%s error: old file lengths different" % outs[i]
            return

        for line_no in range(len(new_array)):
            if new_array[line_no] != old_array[line_no]:
                print "%s error: line %d" % (outs[i], line_no)
                return

        print "%s assembled perfectly" % outs[i]

test_it()
