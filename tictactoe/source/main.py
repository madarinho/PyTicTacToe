from tictactoe.source.service.initializer import initialize_board,change_player
from tictactoe.source.service.validator import validate_input, validate_win
from tictactoe.source.service.visualizer import print_board

win = False;
player = "X";
board = initialize_board()
for i in range(9):
    print_board(board)
    
    print(player,"turn")
    
    valid_input=False
    while (not valid_input):
        row = int(input("row 1-3:")) - 1
        column = int(input("column 1-3:")) - 1
        valid_input = validate_input(board,row,column)
    board[row][column] = player
    win = validate_win(board)
    if (win):
        break
    player = change_player(player)

if (win):
    print(player,"wins!")
else:
    print("Tie")
print_board(board)