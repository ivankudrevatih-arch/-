

board = ['','','',
         '','','',
         '','','',]

current_player = 'X'


def print_board():
    print(board[0], board[1], board[2], sep='|')
    print('-----')
    print(board[3], board[4], board[5], sep='|')
    print('-----')
    print(board[6], board[7], board[8], sep='|')


def change_player():
    global current_player


    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'

def is_win():
    if board[0] == board[1] == board[2] and board[0] != '':
        return True




def game():
    while True:
        print_board()
        user_turn = int(input(f'[{current_player}]| Зробіть хід(1-9):'))

        if 1 <= user_turn <= 9 and board[user_turn - 1] =='':
            board[user_turn - 1] = current_player
            change_player()

game()



































