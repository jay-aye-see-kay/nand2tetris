// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(START)
	//If keyboard input exists got to BLACKEN, otherwise whiten screen
	@KBD
	D=M			//keyboard input -> D
	@BLACKEN
	D;JNE		//jump to BLACKEN if KBD /= 0
	
//-----------------------------------------------------Loop to whiten screen
	@SCREEN		//SCREEN is first pxl value
	D=A			//pxl -> D
	@pxl
	M=D			//pxl -> M
	
(WLOOP)
	//if A register = keyboard (24576) then end loop
	@pxl
	D=M			//pxl -> D
	@KBD
	D=D-A		//KBD is one value higher than the last screen value. If result is 0 or greater, end loop
	@START
	D;JGE
	
	//retrieve screen pixel value from memory location "pxl"
	@pxl
	A=M			//pxl -> A
	
	//set pixel location to white (0 = all white) and increment pixel location
	M=0			//set "pixel word" to white
	A=A+1		//increment mem register by 1
	
	//record pixel location to memory "pxl"
	D=A			//pxl -> D
	@pxl
	M=D			//pxl -> M
	
	@WLOOP
	0;JMP
	
//-----------------------------------------------------Loop to blacken screen	
(BLACKEN)
	@SCREEN		//SCREEN is first pxl value
	D=A			//pxl -> D
	@pxl
	M=D			//pxl -> M
	
(BLOOP)
	//if A register = keyboard (24576) then end loop
	@pxl
	D=M			//pxl -> D
	@KBD
	D=D-A		//KBD is one value higher than the last screen value. If result is 0 or greater, end loop
	@START
	D;JGE
	
	//retrieve screen pixel value from memory location "pxl"
	@pxl
	A=M			//pxl -> A
	
	//set pixel location to black (-1 = 111111111111111 = all back) and increment pixel location
	M=-1		//set "pixel word" to black
	A=A+1		//increment mem register by 1
	
	//record pixel location to memory "pxl"
	D=A			//pxl -> D
	@pxl
	M=D			//pxl -> M
	
	@BLOOP
	0;JMP