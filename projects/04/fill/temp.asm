	@SCREEN		//SCREEN is first pxl value
	D=A			//pxl -> D
	@pxl
	M=D			//pxl -> M
	
(LOOP)
	//if A register = keyboard (24576) then end loop
	@pxl
	D=M			//pxl -> D
	@KBD
	D=D-A		//KBD is one value higher than the last screen value. If result is 0 or greater, end loop
	@END
	D;JGE
	
	//retrieve screen pixel value from memory location "pxl"
	@pxl
	D=M			//pxl -> D
	A=D			//pxl -> A
	
	//set pixel location to black (-1 = 111111111111111 = all back) and increment pixel location
	M=-1		//set "pixel word" to black
	A=A+1		//increment mem register by 1
	
	//record pixel location to memory "pxl"
	D=A			//pxl -> D
	@pxl
	M=D			//pxl -> M
	
	@LOOP
	0;JMP
	
(END)
	@END
	0;JMP
