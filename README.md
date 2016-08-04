# sudoku_generator

	This is a very simple program for generating valid sudoku 
	using backtracking depth first visit.
	The concept is: for each cell tries to put a random int between 1 and 9
	if it works proceed to the next cell, if there is a conflict takes another
	integer and repeat the process, if there are no more ints to take (9 tries)
	go back to the previous cell and try another number.
	You can see this problem like a big tree-graph, where each node is a different 
	sudoku board configuration.
	The space of the different states is something like 9^81 which is really unpractical
	We are using depth first visit to eliminare quickly invalid sub-graph

	If you want to create a playable game, just take a valid board generated with this program and 
	delete some cells, the more you eliminate the harder the game is.
	There are some strategies for eliminating cells, like random delete and symmetrical delete
	
