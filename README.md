# AIFinalProjectTTT
My name is Joseph Veltri and I have created a 5x5 Tic Tac Toe game with AI and Minimax Algortihm implementation. 

For this github document, I will be discussing the project and usage instructions for it: 
1  - Run this code on the terminal of your computer or any 3rd party application such as IDLE or PyCharm. 

2 - When prompted, please enter the name of the desired user and press enter. Please only use letters and do not leave it blank. 

3 - At random, the first player (Either the AI or the user) will select the first position between 0-24 as there is 25 possible positions. 

4 - Each player will select open positions back-and-forth until there is a winner or a full board, or tie, occurs.  

5 - At the end, it will print whether the AI has won, the user has won, or if the game has ended in a tie. 


Here is the background for each slide that is presented: 
1  - The project topic is to create a Tic Tac Toe board using MiniMax algorithm. The project objectives are to create an empty game board, to take inputs from player(s) and the AI to determine the winning side, and to build the game using Python language. The approach for this project is to use dictionaries in python, how to access dictionaries, use for loop and if-else conditions with functions in python, and implement minimax algorithm so that there is a clear winner and loser

2 - Tic taco toe’s history started with the Romans but their version was much more difficult than the one we know today. Each player used 3 pebbles, and had to move them around on each turn. Tic tac toe markings have been found etched all over Rome. Historians aren’t completely clear about the origin of the game’s name, but it could be referring to the noise of repetitive ticking or writing that goes along with the game’s play.

3 - Minimax applies search to a fairly low tree depth aided with appropriate heuristics and a well designed evaluation function. With this approach we lose the certainty in finding the best possible move, but the majority of cases the decision that minimax makes is much better than any human’s. 

4 - The first 6 variables that are listed are the constraints for the program. Normally a tic tac toe game is used with X and O, but I used J for the user as a replacement for X and for the AI I used V for O. J and V are my initials so I wanted to put my own style on this program. LW is used for the how big the board is, and it can be changed to any area. 5 is put as a 5x5 board. NUsers is the amount of users and thinkT is the amount of time the AI has to think for its next move, which can also be changed but it is set a 3 seconds. There are the exceptions classes listen in lines 12 and 15. Between lines 25 and 30 is for the constructer as it gets 1 argument and the size of the board is initialized and the last move is stored to decide who wins the game. The rest of the lines prints the game board itself. 

5 - this function gets position 0 and converts it to a board position and returns the corresponding row and column. Each of the next 4 segments are each specified for a specific job. getLastMove is the function that retunes the last move in the board. getRow gets the number of rows in the board and returns the corresponding row. getColumn has the same job as getRow but for the columns instead. getDiagonal returns and checks for all diagonals on the board. 

6 - getDiagonal1 and getDiagonal2 functions are used for returning the main diagonals of the board, 1 is used for the diagonal from top left to bottom right and 2 is used for the diagonal from top right to bottom left. checkMainDiagonal and checkSecondDiagonal are functions that gets the positions and check if the position that was selected is in either of the diagonals on the board. drawJ is a function that gets the position selected and places a J on the board. drawV is the same function as drawJ and will place a corresponding V in the selected position. drawEmpty will place a character in the other positions that were not selected so that the AI and User know they are free to select these positions. 

7 - checkEmptyChoice will check the rows and columns and all positions to see if they are empty or not. def all_same is a function that has 2 arguments, ListC is the lines in the board and char is for the J and V and checking to see if all the lines are filled with either of them. class Game is the game class and all the activities. def __init__ is a constructor with 2 arguments with numberOfPlayers and boardSize. mNameList stores the names of the players, mTurn shows who’s turn it is, mComputerFirstPosition will store the random position of the AI. In line 120, randomChoice decides who is starting the game. 

8 - getNamesP í a function that will get and store the players names. 133 to 139 are print statements that will give the parameters of storing and getting the players names. You only can put letters, you cannot leave the name blank or add numbers and when using more than 1 user and trying to put the same name twice, it will prompt you to choose again. getPlayerMove is the function that will get the move from the user. It will state the players name and ask you to select a space between 0-24 as there are 25 possible positions on the 5x5 board. If you choose outside of the range or a space that is already filled, it will print a statement listed and ask you to choose again. 

9 - checkWin gets the players turn and check to see if the user won based on the last move by checking every row and column. The last move that was made is checked on line 175 and if that move completes a 5 in a row in any order, it will detect a win for either the user or AI. 

10 - checkDraw will check if the game has ended in a draw, which basically means the entire board is filled and there is no winner. def accumulate will compute all the moves that are on the board and return them and def checkGS will check the game state and return it. 

11 - def start is starting the game entirely and making sure it runs smoothly until it is over with a victory or draw. This slide has print statements for when the AI has its turn in line 230 and between 239 and 249, there are numerous print statements for when the game ends in a tie, when the user has won, and for when the AI has won. 

12 - This slide shows numerous different arguments as depth is used for the depth of the game tree, MaxMin is to tell if we are the maximizer or the minimizer, alpha stores the best value for the maximizer, beta stores the best value for the minimizer, startTime is the time we started the search, timeLimit is the time we will search for the best move. 
The function shows us if the moves the user takes are better or worse by computing the best score and position in the given depth and then returns them. This is also called using minmax algorithm with alpha beta pruning. 

13 - def BestMoveSearch is the function that searches for the best move it find in the time that is allowed to think, which for this is 3 seconds. The function goes as deep as possible in 3 second in the game tree and return the best move. 

14 - def calcEachVar is used for checking a board line and to tally how many J’s, V’s and empty positions there are. getLineSum is for checking each line in the board and calculate the score. def evaluate function is to evaluate the board and return the score. 

15 - I have run this demo for myself and numerous friends between 50-60 times and there has only been 1 victory by the AI. All other outcomes have come in draws, that is how intelligent this algorithm is in detecting the best possible next move. It feels like it is 2 steps ahead of you and when you think you have it outmatched, it comes back with a move that will mess you your victory. 



Thank you and Enjoy! 
