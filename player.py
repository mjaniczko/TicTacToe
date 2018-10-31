import random

class Player():

    def __init__(self, mark, name):
        self.mark = mark
        self.name = name 
    
    def player_move(self):
        y = 5
        while y < 0 or y > 2:
            try:
                y = int(input('Type y pos (form 0 - 2): '))
            except ValueError:
                y = 5
        x = 'x'
        while x != 'A' and x != 'B' and x != 'C':
            x = input('Type x pos (A or B or C): ').upper()
            
        return (y, x)

