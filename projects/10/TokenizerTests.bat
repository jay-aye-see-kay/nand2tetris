@echo off

echo -
echo Running Tokenizer/main.py...
python Tokenizer/main.py

echo -
echo ArrayTest/MainT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ArrayTest/MainT.xml" "ArrayTest/MyMainT.xml"

echo -
echo ExpressionLessSquare/MainT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/MainT.xml" "ExpressionLessSquare/MyMainT.xml"

echo -
echo ExpressionLessSquare/SquareT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/SquareT.xml" "ExpressionLessSquare/MySquareT.xml"

echo -
echo ExpressionLessSquare/SquareGameT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/SquareGameT.xml" "ExpressionLessSquare/MySquareGameT.xml"

echo -
echo Square/MainT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/MainT.xml" "Square/MyMainT.xml"

echo -
echo Square/SquareT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/SquareT.xml" "Square/MySquareT.xml"

echo -
echo Square/SquareGameT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/SquareGameT.xml" "Square/MySquareGameT.xml"

echo -