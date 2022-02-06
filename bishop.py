from piece import Piece

class Bishop(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Bishop", "B", False)

    def is_valid_move(self, start_pos, end_pos, board):
        if self.check_not_on_board(end_pos):
            return False

        if not self.check_move_colour(board.white_move):
            return False

        j_difference = start_pos.j - end_pos.j
        i_difference = start_pos.i - end_pos.i
        end_piece = board.get_piece(end_pos)

        if abs(i_difference) == abs(j_difference):
            if end_piece and end_piece.colour != self.colour:
                return True
            elif not(end_piece):
                return True
