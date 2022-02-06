from piece import Piece, Position

class Pawn(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Pawn", "P", False)
        self.promote = False
        self.passant_count = 0

    def is_valid_move(self, start_pos, end_pos, board):

        if self.check_not_on_board(end_pos):
           return False

        start_piece = board.get_piece(start_pos)
        end_piece = board.get_piece(end_pos)
        left_piece = board.get_piece(Position(start_pos.i - 1, start_pos.j)) if start_pos.i > 0 else None
        right_piece = board.get_piece(Position(start_pos.i + 1, start_pos.j)) if start_pos.i <7 else None
        j_difference = start_pos.j - end_pos.j
        i_difference = start_pos.i - end_pos.i

        #Pawn movement
        if (self.colour == "White" and
            board.white_move == 1):
            if (start_pos.j == 1 and
                j_difference == -2 and
                i_difference == 0 and
                not end_piece):
                self.is_passantable = True
                return True

            if (j_difference == -1 and
                i_difference == 0 and
                not end_piece):

                if end_pos.j == 0:
                    self.promote = True

                return True

            #Taking
            if (abs(i_difference) == 1 and
                j_difference == -1):

                if (end_piece and
                    end_piece.colour != self.colour):
                    return True

                #En passant
                if (not end_piece and
                    right_piece and
                    right_piece.colour != self.colour and
                    right_piece.is_passantable):
                    right_piece.taken = True
                    print("En passant")
                    return True

                if (not end_piece and
                    left_piece and
                    left_piece.colour != self.colour and
                    left_piece.is_passantable):
                    left_piece.taken = True
                    print("En passant")
                    return True

        if (self.colour == "Black" and
            board.white_move ==0):

            #pawn movement
            if (start_pos.j == 6 and
                j_difference == 2 and
                i_difference == 0 and
                not end_piece):
                self.is_passantable = True
                return True

            if (j_difference == 1 and
                i_difference == 0 and
                not end_piece):
                return True

            #Taking
            if  (abs(i_difference) == 1 and
                j_difference == 1):
                if (end_piece and
                    end_piece.colour != self.colour):
                    return True

                #En Passant
                if ((not end_piece) and
                    right_piece and
                    right_piece.colour != self.colour and
                    right_piece.is_passantable):
                    print("En passant")
                    right_piece.taken = True
                    return True

                if ((not end_piece) and
                    left_piece and
                    left_piece.colour != self.colour and
                    left_piece.is_passantable):
                    print("En passant")
                    left_piece.taken = True
                    return True
