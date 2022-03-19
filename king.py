from piece import Piece, Position

class King(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "King", "K", False)

    def is_valid_move(self, start_pos, end_pos, board):
        if self.check_not_on_board(end_pos):
            return False
        if not self.check_move_colour(board.white_move):
            return False

        j_difference = start_pos.j - end_pos.j
        i_difference = start_pos.i - end_pos.i
        end_piece = board.get_piece(end_pos)

        if end_piece and end_piece.colour == self.colour:
            return False
        if abs(j_difference) == 1 and abs(i_difference) == 1:
            return True
        elif abs(j_difference) == 1 and abs(i_difference) == 0:
            return True
        elif abs(j_difference) == 0 and abs(i_difference) == 1:
            return True

        #castling
        kingside_rook = board.get_piece(Position(start_pos.i + 3, start_pos.j))
        queenside_rook = board.get_piece(Position(start_pos.i - 4, start_pos.j))

        if i_difference == -2 and abs(j_difference) == 0:
            print("castling kingside")
            kingside_rook.is_kingside_castling = True
            return True

        elif i_difference == 2 and abs(j_difference) == 0:
            print("castling queenside")
            queenside_rook.is_queenside_castling = True
            return True
