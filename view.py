def welcome():
    print('''   WELCOME 
    
Hey, hope you'll had a great time while playing this game with friend
Remeber computer couting from 0 (this is development version :P) so if 
you want mark midle square as y type 1 and  as x type b \n\n''')


def get_name():
    name = input('Hey, now is the time to introduce yourself (type your name/nickname): ')
    return name


def play_again():
    play_again = input('Would you like to play again type(y/n): ')
    return play_again


def display_board(board):
    x_pos = ['A', 'B', 'C']
    counter = 0
    print('  0 | 1 | 2')
    print(' -----------')
    for row in board:
        temp = ' | '.join([str(v) for v in row])
        print('| ' + temp + ' |' + ' ' + x_pos[counter])
        print(' -----------')
        counter += 1
