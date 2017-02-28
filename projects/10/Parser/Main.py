from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine
import os

def main(path):

    # for each file in the path:
    os.chdir(path)
    for filename in os.listdir(path):
        if filename[-5:] == '.jack':
            # open .jack file, read it as one string, create new JackTokenizer class 
            inStr = open(filename).read()
            compilation = CompilationEngine(inStr)

            # create a xml file for output
            out_txt = open('My' + filename[:-5] + '.xml','w')

            # run through string by tokens, adding them to the output file
            xml = compilation.compileClass()
            out_txt.write(xml)
            
            # close xml file
            out_txt.close()

def tokenize(path):

    # for each file in the path:
    os.chdir(path)
    for filename in os.listdir(path):
        if filename[-5:] == '.jack':
            # open .jack file, read it as one string, create new JackTokenizer class 
            inStr = open(filename).read()
            jackFile = JackTokenizer(inStr)

            # create a xml file for output
            out_txt = open('My' + filename[:-5] + 'T.xml','w')
            out_txt.write('<tokens>\n')

            # run through string by tokens, adding them to the output file
            while(jackFile.hasMoreTokens()):
                jackFile.advance()
                out_txt.write(jackFile.writeXML())
            
            # close xml file
            out_txt.write('</tokens>')
            out_txt.close()

main("C:/Users/John/Documents/nand2tetris/projects/10/ArrayTest/")
main("C:/Users/John/Documents/nand2tetris/projects/10/ExpressionLessSquare/")
main("C:/Users/John/Documents/nand2tetris/projects/10/Square/")


#main("C:/Users/John/Documents/nand2tetris/projects/10/Tests/")
#tokenize("C:/Users/John/Documents/nand2tetris/projects/10/Tests/")
