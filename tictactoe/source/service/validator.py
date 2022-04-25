options_range = set([0,1,2])

def validate_input(board,row,column):
    if (row not in options_range):
        print("row not in range")
        return False
    if (column not in options_range):
        print("column not in range")
        return False
    if (not board[row][column] == ' '):
        print("position already filled")
        return False
    return True

def validate_win(board):
    return False