from piece import Piece

class Rook(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Rook", "R", False)

    def is_valid_move(self, start_pos, end_pos, board):
        if self.check_not_on_board(end_pos):
            return False

        if not self.check_move_colour(board.white_move):
            return False

        for z in range(8):
            j_difference = start_pos.j - end_pos.j
            i_difference = start_pos.i - end_pos.i
            end_piece = board.get_piece(end_pos)

            if abs(j_difference) == z:
                if abs(i_difference) == 0:
                    if end_piece and end_piece.colour != self.colour:
                        return True
                    if not(end_piece):
                        return True

            if abs(j_difference) == 0:
                if abs(i_difference) == z:
                    if end_piece and end_piece.colour != self.colour:
                        return True
                    if not(end_piece):
                        return True
