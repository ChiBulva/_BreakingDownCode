/
\ 
/
\ 
/
\ 
/
main -> |Var #1: 'int argc' |Var #2: ' char **argv'
	If Statement
	/
	\ 
	If Statement
	/
	\ 
	For Loop
	/
	\ 
	For Loop
	/
		For Loop
	\ 
	For Loop
	/
			GenerateWorldMap <-- function call with 2 variables!
	\ 
	For Loop
	For Loop
	/
		For Loop
		/
		\ 
	\ 
	For Loop
	/
		For Loop
		/
			If Statement
			/
			\ 
		\ 
	\ 
	For Loop
	/
		If Statement
		If Statement
	\ 
	For Loop
	/
		For Loop
		/
		\ 
	\ 
	For Loop
	/
		If Statement
	\ 
	If Statement
	/
		For Loop
		/
			For Loop
			/
				If Statement
			\ 
		\ 
	\ 
	/
		For Loop
		/
			For Loop
			/
				If Statement
				If Statement
				If Statement
			\ 
		\ 
		If Statement
		For Loop
		/
			For Loop
			/
					FloodFill4 <-- function call with 2 variables!
				If Statement
				If Statement
			\ 
		\ 
		For Loop
		/
			For Loop
			/
					FloodFill4 <-- function call with 2 variables!
				If Statement
				If Statement
			\ 
		\ 
	\ 
\ 
/
FloodFill4 -> |Var #1: 'int x' |Var #2: ' int y' |Var #3: ' int OldColor'
	If Statement
	/
		If Statement
			FloodFill4 <-- function call with 3 variables!
		If Statement
			FloodFill4 <-- function call with 3 variables!
		If Statement
		If Statement
			FloodFill4 <-- function call with 3 variables!
			FloodFill4 <-- function call with 3 variables!
		If Statement
			FloodFill4 <-- function call with 3 variables!
			FloodFill4 <-- function call with 3 variables!
	\ 
\ 
/
GenerateWorldMap
	For Loop
	/
		If Statement
		/
			If Statement
		\ 
		/
			If Statement
		\ 
	\ 
\ 
/
BumpPixel
	If Statement
	/
		If Statement
		else
		/
			Switch Statement
			/
				If Statement
				/
				\ 
				If Statement
				/
				\ 
				If Statement
				/
				\ 
			\ 
		\ 
	\ 
\ 
/
GIFNextPixel -> |Var #1: ' void '
	If Statement
		BumpPixel <-- function call with 1 variables!
\ 
/
	If Statement
	If Statement
	For Loop
	/
	\ 
	If Statement
\ 
/
\ 
/
		char_init <-- function call with 1 variables!
		GIFNextPixel <-- function call with 1 variables!
	For Loop
		GIFNextPixel <-- function call with 1 variables!
	While Loop
	/
			GIFNextPixel <-- function call with 1 variables!
		While Loop
		/
		\ 
		If Statement
		If Statement
		/
			If Statement
		\ 
		If Statement
		If Statement
		If Statement
		/
		\ 
		If Statement
		If Statement
		/
			If Statement
			/
			\ 
		\ 
	\ 
\ 
/
\ 
/
	If Statement
	While Loop
	/
	\ 
	If Statement
	/
		If Statement
		/
			else
		\ 
		/
			If Statement
		\ 
	\ 
	If Statement
	/
		While Loop
		/
		\ 
			flush_char <-- function call with 1 variables!
		If Statement
			writeerr <-- function call with 1 variables!
	\ 
\ 
/

\ 
/
	Do while loop
	/
		While Loop
	\ 
	For Loop
\ 
/
writeerr
\ 
/
char_init
\ 
/
	If Statement
		flush_char <-- function call with 0 variables!
\ 
/
flush_char
	If Statement
	/
	\ 
\ 
149
370
394
472
528
1000
1046
1066
1093
