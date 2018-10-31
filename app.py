import os
import view
from player import Player
from board import Board

os.system("clear")  
def main():
    view.welcome()
    play_again = 'y'
    player1 = Player('X', view.get_name())
    player2 = Player('O', view.get_name())
    players = [player1, player2]
    while play_again == 'y':
        game = True
        board = Board(3)
        while game:
            for player in players:
                os.system("clear")
                view.display_board(board.board)
                y, x = player.player_move()
                while not board.change_state_of_cell(y, x, player = player.mark):
                    print('That field is already occupied. Try again')
                    y, x = player.player_move()
                if board.is_board_full():
                    print('Board is full. Noone win')
                    game = False
                    break
                elif board.check_victory(y, x, player.mark):
                    print('Player {} won the game.'.format(player.name))
                    game = False
                    break
        play_again = view.play_again()

if __name__ == '__main__':
    main()