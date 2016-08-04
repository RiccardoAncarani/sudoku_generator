'''
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

	Written by Ancarani Riccardo
'''

import sys
import random

def same_row(x, y): # checks if there are conflicts in the same row
   val = matrix[x][y]
   for i in range(y):
      if(matrix[x][i] == val and ( i != y )):
         return False
   return True


def same_col(x, y): # checks if there are conflicts in the same column
   val = matrix[x][y]
   for i in range(x):
      if(matrix[i][y] == val and ( i != x )):
         return False
   return True

def same_block(x, y): # this function checks if there are conflicts in the same block
   val = matrix[x][y]
   a = x/3
   b = y/3
   for i in range(a*3,a*3+3):
      for j in range(b*3,b*3+3):
         if(matrix[i][j] == val and (i != x and j != y)):
            return False
   return True


def create(x ,y):
   #print matrix
   if(x == 9 or y == 9): # reached end of matrix, done.
      return True
   val = matrix[x][y]
   for i in range(1,10):
      matrix[x][y] = random.randint(1,9)
      if(same_row(x,y) and same_col(x,y) and same_block(x,y)): # if there are no conflicts move forward
         if(y == 8):
            x = x +1
         y = (y +1) % 9
         if(create(x,y) == True): # recursively call create function on the next cell
            return True # work done.
   matrix[x][y] = 0 # no numbers aviable for this cell, go back
   return False  
         
def printMatrix():
   for i in range(9):
      for j in range(9):
         sys.stdout.write(str(matrix[i][j]))
         sys.stdout.flush()
      print "\n"
      

matrix = [[0 for x in range(9)] for i in range(9)] # init matrix of zeros
create(0,0)
printMatrix()

