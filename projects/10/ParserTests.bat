@echo off

echo -
echo Running Parser/main.py...
python Parser/main.py

echo -
echo ArrayTest/Main.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ArrayTest/Main.xml" "ArrayTest/MyMain.xml"

echo -
echo ExpressionLessSquare/Main.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/Main.xml" "ExpressionLessSquare/MyMain.xml"

echo -
echo ExpressionLessSquare/Square.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/Square.xml" "ExpressionLessSquare/MySquare.xml"

echo -
echo ExpressionLessSquare/SquareGame.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "ExpressionLessSquare/SquareGame.xml" "ExpressionLessSquare/MySquareGame.xml"

echo -
echo Square/MainT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/Main.xml" "Square/MyMain.xml"

echo -
echo Square/SquareT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/Square.xml" "Square/MySquare.xml"

echo -
echo Square/SquareGameT.xml
java -classpath "%CLASSPATH%;C:/Users/John/Documents/nand2tetris/tools/bin/classes" TextComparer "Square/SquareGame.xml" "Square/MySquareGame.xml"

echo -