from enum import Enum
import datetime
import random

user = 'J'
AI = 'V'
space = '_'
LW = 5
NUsers = 1
thinkT = 3

class NoneEmptyPosition(Exception):
    pass

class RangeO(Exception):
    pass


class GameState(Enum):
    tie = 'Tie'
    notEnd = 'notEnd'
    x = 'J'  
    o = 'V'
    
class Board:
   
    def __init__(self, size):
        self.mSize = size
        self.mBoard = [[space for x in range(size)] for y in range(size)]
        self.lastMove = None

    def print(self):
        for i in range(self.mSize):
            for j in range(self.mSize):
                if j < self.mSize-1:
                    print(self.mBoard[i][j], end='|')
                else:
                    print(self.mBoard[i][j], end='')
            print()

    def getBoardPosition(self,position):
        C = position%self.mSize
        R = position//self.mSize
        return R, C

    def getLastMove(self):
        return self.lastMove

    def getRow(self, NoR):
        return self.mBoard[NoR]

    def getColumn(self, NoC):
        return [R[NoC] for R in self.mBoard]

    def getDiagonal(self):
        D1 = [self.mBoard[i][i] for i in range(self.mSize)]
        D2 = []
        j = 0
        for i in reversed(range(self.mSize)):
            D2.append(self.mBoard[i][j])
            j += 1
        return D1, D2


    def getDiagonal1(self):
        return [self.mBoard[i][i] for i in range(self.mSize)]


    def getDiagonal2(self):
        D = []
        j = 0;
        for i in reversed(range(self.mSize)):
            D.append(self.mBoard[i][j])
            j += 1
        return D

 
    def checkMainDiagonal(self, position):
        return position % (self.mSize + 1) == 0

    def checkSecondDiagonal(self, position):
        return position % (self.mSize - 1) == 0


    def drawJ(self, position):
        self.lastMove = position
        (R, C) = self.getBoardPosition(position)
        self.mBoard[R][C] = user

    def drawEmpty(self, position):
        (R, C) = self.getBoardPosition(position)
        self.mBoard[R][C] = space

    def drawV(self, position):
        self.lastMove = position
        (R, C) =  self.getBoardPosition(position)
        self.mBoard[R][C] = AI


    def checkEmptyChoice(self, position):
        (R, C) = self.getBoardPosition(position)
        return self.mBoard[R][C] == space


    def all_same(self, ListC, char):
        return all(x == char for x in ListC)


class Game:
    def __init__(self, numberOfPlayers, boardSize):
        self.mBoard = Board(boardSize)
        self.mBoardSize = boardSize
        self.mNumP = numberOfPlayers
        self.mNameL = [' ']*numberOfPlayers
        self.mTurn = None
        self.mCompFP = None
        self.randomChoice()
        self.mBM = 0

    def randomChoice(self):
        turn = random.choice(['AI', 'Player'])
        if turn == 'AI':
            self.mCompFP = random.randrange(self.mBoard.mSize ** 2)
            self.mTurn = 1
        else:
            self.mTurn = 0


    def getNamesP(self):
        counter = 1
        while counter <= self.mNumP:
            try:
                playerName = input('Enter name for player: ')
                if not playerName:
                    raise ValueError("Name cannot be blank, enter name: ")
                if not playerName.isalpha():
                    raise ValueError("Only use letters, try again!")
                if playerName in self.mNameL:
                    raise ValueError("Please choose a different name")

                self.mNameL[counter - 1] = playerName
                counter += 1
            except ValueError as e:
                print(e)
            except Exception:
                print("Error")


    def getPlayerMove(self):
        while True:
            try:
                playerMove = int(input(self.mNameL[self.mTurn] + ', please select a space [0-24]: '))
                if not (0 <= playerMove <= (self.mBoardSize ** 2 - 1)):
                    raise RangeO("Wrong position, please choose again " + str(self.mBoardSize ** 2 - 1))

                if not self.mBoard.checkEmptyChoice(playerMove):
                    raise NoneEmptyPosition("This space is already filled, please choose another")

                return playerMove

            except (RangeO, NoneEmptyPosition) as e:
                print(e)
            except ValueError as e:
                print("Choose only between 0-24")
            except Exception:
                print("Error")


    def checkWin(self, turn):
        char = ''
        if turn % 2 == 0:
            char = 'J'
        else:
            char = 'V'
        lastMove = self.mBoard.getLastMove()
        R, col = self.mBoard.getBoardPosition(lastMove)

        if self.mBoard.all_same(self.mBoard.getRow(R), char) or \
                self.mBoard.all_same(self.mBoard.getColumn(col), char):
            return True

        if self.mBoard.checkMainDiagonal(lastMove):
            if self.mBoard.all_same(self.mBoard.getDiagonal1(), char):
                return True

        if self.mBoard.checkSecondDiagonal(lastMove):
            if self.mBoard.all_same(self.mBoard.getDiagonal2(), char):
                return True

        return False


    def checkDraw(self):
        for i in range(self.mBoard.mSize ** 2):
            if self.mBoard.checkEmptyChoice(i):
                return False
        return True


    def accumulate(self):
        MovesAll = []
        for i in range(self.mBoard.mSize ** 2):
            if self.mBoard.checkEmptyChoice(i):
                MovesAll.append(i)
        return MovesAll


    def checkGS(self):
        if self.checkWin(0):
            return GameState.x

        if self.checkWin(1):
            return GameState.o

        if self.checkDraw():
            return GameState.tie

        return GameState.notEnd


    def start(self):
        self.getNamesP()
        while True:
            self.mBoard.print()
            self.mTurn %= 2
            if self.mTurn % 2 == 0:
                playerMove = self.getPlayerMove()
                self.mBoard.drawJ(playerMove)
            else:
                print('The AI will be selecting a space from 0-24... ')
                if self.mCompFP is not None:
                    compM = self.mCompFP
                    self.mCompFP = None
                else:
                    compM = self.BestMoveSearch()

                self.mBoard.drawV(compM)

            gameResult = self.checkGS()
            if gameResult.value != 'notEnd':
                self.mBoard.print()
                if gameResult.value == 'Tie':
                    print('The game has ended in a tie!')
                else:
                    if self.mTurn % 2 == 0:
                        print(self.mNameL[self.mTurn] + 'is the winner!')
                    else:
                        print('The AI has won!')
                break

            self.mTurn += 1


    def MinMaximum(self, depth, MaxMin, alpha, beta, startTime, timeLimit):

        moves = self.accumulate()
        score = self.evaluate()
        position = None

        if datetime.datetime.now() - startTime >= timeLimit:
            self.mTimePassed = True

        if not moves or depth == 0 or self.mTimePassed:
            gameResult = self.checkGS()
            if gameResult.value == 'J':
                return -10**(self.mBoard.mSize+1), position
            elif gameResult.value == 'V':
                return 10**(self.mBoard.mSize+1), position
            elif gameResult.value == 'TIE':
                return 0, position

            return score, position

        if MaxMin:
            for i in moves:
                    self.mBoard.drawV(i)
                    score, dummy = self.MinMaximum(depth-1, not MaxMin, alpha, beta, startTime, timeLimit)
                    if score > alpha:
                        alpha = score
                        position = i
                        self.mBM = i

                    self.mBoard.drawEmpty(i)
                    if beta <= alpha:
                        break

            return alpha, position
        else:
            for i in moves:
                self.mBoard.drawJ(i)
                score, dummy = self.MinMaximum(depth-1, not MaxMin, alpha, beta, startTime, timeLimit)
                if score < beta:
                    beta = score
                    position = i
                    self.mBM = i
                self.mBoard.drawEmpty(i)
                if alpha >= beta:
                    break

            return beta, position


    def BestMoveSearch(self):
        startTime = datetime.datetime.now()
        endTime = startTime + datetime.timedelta(0, thinkT)
        depth = 1
        position = None
        self.mTimePassed = False
        while True:
            currentTime = datetime.datetime.now()
            if currentTime >= endTime:
                break
            best, position = self.MinMaximum(depth, True, -10000000, 10000000, currentTime, endTime-currentTime)
            depth += 1

        if position is None:
            position = self.mBM

        return position


    def calcEachVar(self, line):
        vSum = line.count(AI)
        jSum = line.count(user)
        noneSum = line.count(space)
        return vSum, jSum, noneSum


    def getLineSum(self, line):
        score = 0
        vSum, jSum, noneSum = self.calcEachVar(line)
        if jSum == 0 and vSum != 0:
            if vSum == self.mBoard.mSize:
                score += 11 ** (vSum - 1)
            score += 10 ** (vSum - 1)
        if vSum == 0 and jSum != 0:
            score += -(10 ** (jSum - 1))
        return score


    def evaluate(self):
        score = 0
        for i in range(self.mBoard.mSize):
            score += self.getLineSum(self.mBoard.getRow(i))
            score += self.getLineSum(self.mBoard.getColumn(i))

        diagonals = self.mBoard.getDiagonal()
        for i in range(2):
            score += self.getLineSum(diagonals[i])
        return score

game = Game(NUsers, LW)
game.start()
