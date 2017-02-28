@echo off

echo -
echo Running Parser/main.py...
python Parser/main.py

echo -
echo Tests/Square.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/Square.xml" "Tests/MySquare.xml"

REM echo -
REM echo ExpressionLessSquare/MainT.xml
REM java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/Main.xml" "ExpressionLessSquare/MyMain.xml"

REM echo -
REM echo ExpressionLessSquare/SquareT.xml
REM java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/Square.xml" "ExpressionLessSquare/MySquare.xml"

REM echo -
REM echo ExpressionLessSquare/SquareGameT.xml
REM java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/SquareGame.xml" "ExpressionLessSquare/MySquareGame.xml"

REM echo -
REM echo Square/MainT.xml
REM java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/Main.xml" "Square/MyMain.xml"

REM echo -
REM echo Square/SquareT.xml
REM java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/Square.xml" "Square/MySquare.xml"

REM echo -
REM echo Square/SquareGameT.xml
REM java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/SquareGame.xml" "Square/MySquareGame.xml"

echo -