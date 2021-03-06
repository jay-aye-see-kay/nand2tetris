from compiler import JackTokenizer
import os

def main(path):

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

def tmp(filename):
    # open .jack file, read it as one string, create new JackTokenizer class 
    inStr = open(filename).read()
    jackFile = JackTokenizer(inStr)

    # create a xml file for output
    out_txt = open(filename[:-5] + '_tidy.txt','w')
    
    # close xml file
    out_txt.write(jackFile.string)
    out_txt.close()

#tmp("C:/Users/John/Documents/nand2tetris/projects/10/Square/Main.jack")