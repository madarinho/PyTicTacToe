def print_board(board):
    printHorizontal()
    printRowWalls()
    printRow(board,0)
    printRowWalls()
    printHorizontal()
    printRowWalls()
    printRow(board,1)
    printRowWalls()
    printHorizontal()
    printRowWalls()
    printRow(board,2)
    printRowWalls()
    printHorizontal()

def printHorizontal():
    print("=========================")
def printRowWalls():
    print("|       |       |       |")
def printRow(board,i):
    print("|  ",board[i][0],"  |  ",board[i][1],"  |  ",board[i][2],"  |")