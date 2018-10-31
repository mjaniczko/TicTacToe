import numpy as np


class Board():
    
    def __init__(self, size):
        self.size = size
        self.board = [ [' ' for x in range(self.size)] for x in range(self.size) ]

    def is_board_full(self):
        for row in self.board:
            for col in row:
                if col is ' ':
                    return False
        return True

    def change_state_of_cell(self, y, x, player):
        x = Board.letters_to_coords(x)
        if self.board[x][y] is not ' ':
            return False
        else:
            self.board[x][y] = player
            return True
     
    @staticmethod
    def letters_to_coords(x):
        if isinstance(x, int):
            return x
        codes = {'A': 0, 'B': 1, 'C': 2}
        return codes[x]


    def get_row(self, x):
        row = self.board[x]
        return row
    
    def get_col(self, y):
        return [el[y] for el in self.board]
    
    def get_diagonal(self, direction):
        if direction == 'l':
            return np.diag(self.board)
        if direction == 'r':
            return np.fliplr(self.board).diagonal(0)[::1]
    
    
    def diagonals_of(self, x, y):
        diagonals = []
        if x == y:
            diagonals.append('l')
        if x + y == self.size - 1:
            diagonals.append('r')
        return diagonals
    
    def check_victory(self, y, x, mark):
        x = Board.letters_to_coords(x)

        def all_owned (fields):
            return all(field == mark for field in fields)

        shapes_to_check = [self.get_row(x), self.get_col(y), 
                           *(self.get_diagonal(d) for d in self.diagonals_of(x, y))]

        return any(all_owned(shape) for shape in shapes_to_check)