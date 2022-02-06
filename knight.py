from piece import Piece, Position

class Knight(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Knight", "N", False)

    def is_valid_move(self, start_pos, end_pos, board):
        if self.check_not_on_board(end_pos):
            return False

        if not self.check_move_colour(board.white_move):
            return False

        j_difference = start_pos.j - end_pos.j
        i_difference = start_pos.i - end_pos.i

        end_piece = board.get_piece(end_pos)

        if  ((abs(j_difference) == 2 and abs(i_difference) == 1) or
            (abs(i_difference) == 2 and abs(j_difference) == 1)):
            if end_piece and end_piece.colour != self.colour:
                return True
            if not(end_piece):
                return True
