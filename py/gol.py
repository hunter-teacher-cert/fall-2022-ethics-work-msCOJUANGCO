# gol.py
# Nicole Cojuangco
# CSCI 77800 Fall 2022
# collaborators: (from summer session code created with Saranii, Amanda, Ben, Nicole) 
# consulted: 

"""
Game of Life:

Survivals:
* A living cell with 2 or 3 living neighbours will survive for the next generation.

Deaths:
* Each cell with >3 neighbours will die from overpopulation.
* Every cell with <2 neighbours will die from isolation.

 Births:
* Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.

NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.

"""""""""

import time
import random

#create empty board
def createNewBoard(rows, cols):
  board = [[" " for i in range(cols)] for j in range(rows)] 
  return board #/amanda: dead cells are ' ' 

#print board 
def printBoard(board):
  rows = len(board)
  cols = len(board[0])

  for x in range(rows):
    for y in range(cols):
      print(board[x][y], end = " ")
  print()


#set cells
def setCell(board, r, c, val):
  board [r][c] = val

#Count living neigbours of board[r][c] 
def countNeighbours(board, r, c):
  count = 0 #initialize
  
# iterate until the row cvalue is less than or equal to row+1 which is the row below the target 
  for rowN in range(r-1, r+2): #goes up to but doesn't include the last starts with the row above
    if rowN >=0 and rowN <len(board): #checks for in bound
      for colN in range(c-1,c+2):
        if colN >=0 and colN<len(board[r]):
          if rowN ==r and colN == c:
            continue
          else: #if there is a neighbor
               #count the neighbors IF it's alive
               #if (neighbor == alive) 
            if board[rowN][colN]== 'X':
              count = count+1
  return count

def getNextGenCell(board,r,c):
  currentCell=board[r][c] 
  count = countNeighbours(board, r, c)
  nextCell = board[r][c]

#checks  for conditions to determine data for new boar
  if(currentCell == 'X'):
    if(count == 2 or count ==3):
      nextCell = 'X'
#less than 2, or greater than 3 then DIE
    else:
      nextCell = '+'
      #DEAD
  else:
    # if neighbors is exactly 3, reborn alive
    if(count==3):
      nextCell = 'X'
    else: #not, stay dead
      nextCell = '+'

  return nextCell

def genNextBoard(board):
  # get rows and cols from the given board
  rows = len(board)
  cols = len(board[0])
  #assemble the board using the parts already created 
  newBoard = createNewBoard(rows,cols)
  nextCell = '@'

  #traverse
  for i in range(rows):
    for j in range(cols):
      nextCell = getNextGenCell(board,i,j)
      setCell(newBoard,i,j,nextCell)

  return newBoard

board = createNewBoard(25,25) #initializer
    
# print board
print("\nWelcome to the Game of Life")

printBoard(board)   
# breathe life into some cells:
setCell(board, 0, 0, 'X')
setCell(board, 0, 1, 'X')
setCell(board, 1, 0, 'X')

"""
CODE FROM SUMMER (this is where left of reviewing/converting)
    System.out.println("\nTesting Count Neighbors");
    int c11 = countNeighbours(board, 1, 1 );  // should return 3
    int c01 = countNeighbours(board, 0, 1 );  // should return 2
    int c02 = countNeighbours(board, 0, 2 );  // should return 1
    int c55 = countNeighbours(board, 5, 5 );  // should return 0
    System.out.println("(1,1) returns " + c11);
    System.out.println("(0,1) returns " + c01);
    System.out.println("(0,2) returns " + c02);
    System.out.println("(5,5) returns " + c55);

    // public static char getNextGenCell( char[][] board,int r, int c )
    System.out.println("\nTesting getNextGenCell");
    char cell11 = getNextGenCell(board, 1, 1);   // should return X alive
    System.out.println("(1,1) will turn " + cell11);
    char cell01 = getNextGenCell(board, 0, 1);  //  should stay alive
    System.out.println("(0,1) will turn " + cell01);
    char cell02 = getNextGenCell(board, 0, 2);   // should stay dead
    System.out.println("(0,2) will turn " + cell02);
    char cell55 = getNextGenCell(board, 5, 5);  //  should stay dead
    System.out.println("(5,5) will turn " + cell55);

    System.out.println("\nTesting generateNextBoard");
    
    
    
    // TASK:
    // Once your initial version is running,
    // try out different starting configurations of living cells...
    // (Feel free to comment out the above three lines.)

    // System.out.println("Gen X:");
    // printBoard(board);
    // System.out.println("--------------------------\n\n");
    
    board = generateNextBoard(board);

    System.out.println("Gen X+1:");
    printBoard(board);
    System.out.println("--------------------------\n\n");
  }//end main()

}//end class
""""""
