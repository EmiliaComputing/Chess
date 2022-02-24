from collections import namedtuple
Position = namedtuple ("Position", "i j")

class Piece:
    def __init__(self, colour, position, name, symbol, taken):
        self.is_passantable =False
        self.colour = colour
        self.position = position
        self.name = name
        self.symbol = symbol
        self.taken = taken

    def is_valid_move(self, start_pos, end_pos):
        return False

    def __repr__(self):
        return f"{self.symbol}"

    def check_move_colour(self, white_move):
        return (self.colour == "Black" and white_move ==0 or
                self.colour == "White" and white_move ==1)

    def check_not_on_board(self, end_pos):
        return (end_pos.i >=8 or
                end_pos.j >=8 or
                end_pos.j <= -1 or
                end_pos.i <= -1)
