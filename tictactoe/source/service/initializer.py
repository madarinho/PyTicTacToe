def initialize_board():
    return [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def change_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'