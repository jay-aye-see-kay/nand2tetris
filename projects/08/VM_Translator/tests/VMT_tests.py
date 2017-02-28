from nose.tools import *
from VMT import helper
from VMT import writer
from VMT.tables import commands

def test_commandType():
    # Test the commandType function finds all comannds in dict
    # check it handles errors and enpty inputs
    for cmd in commands:
        assert_equal(helper.commandType(cmd), commands[cmd])
    assert_equal(helper.commandType('find somethin 4'), 'Error: command not found')
    assert_equal(helper.commandType(''), 'Error: command not found')

def test_writeLabel():
    result = "(f1$lab1)\n"
    assert_equal(writer.writeLabel('lab1', 'f1'), result)

def test_writeGoto():
    result = "@f2$lab2\n0;JMP\n"
    assert_equal(writer.writeGoto('lab2', 'f2'), result)

def test_writeGoto():
    result = '@SP\nM=M-1\nA=M\nD=M\n@f3$lab3\nD;JNE\n'
    assert_equal(writer.writeIf('lab3', 'f3'), result)

def test_getArgs():
    assert_equal(helper.getArgs("push label 3"), ('push', 'label', '3'))
    assert_equal(helper.getArgs("goto label "), ('goto', 'label', ''))
    assert_equal(helper.getArgs("add"), ('add', '', ''))

def test_writeFuction():
    result = '(f1)\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
    assert_equal(writer.writeFunction('f1', '1'), result)
    result = '(f1)\n'
    assert_equal(writer.writeFunction('f1', '0'), result)
    result = '(f1)\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
    assert_equal(writer.writeFunction('f1', '4'), result)
