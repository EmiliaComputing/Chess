from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King
from piece import Position

class Game:
    def __init__(self):
        self.board = [["" for i in range(8)] for i in range(8)]
        self.pieces = []
        self.white_move = 1

        for i in range(8):
            pawn = Pawn("White",Position(i, 1))
            self.pieces.append(pawn)

        for i in range(8):
            pawn = Pawn("Black",Position(i, 6))
            self.pieces.append(pawn)

        knight1 = Knight("White",Position(1, 0))
        knight2 = Knight("White",Position(6, 0))
        knight3 = Knight("Black",Position(1, 7))
        knight4 = Knight("Black",Position(6, 7))
        self.pieces.append(knight1)
        self.pieces.append(knight2)
        self.pieces.append(knight3)
        self.pieces.append(knight4)

        bishop1 = Bishop("White",Position(2, 0))
        bishop2 = Bishop("White",Position(5, 0))
        bishop3 = Bishop("Black",Position(2, 7))
        bishop4 = Bishop("Black",Position(5, 7))
        self.pieces.append(bishop1)
        self.pieces.append(bishop2)
        self.pieces.append(bishop3)
        self.pieces.append(bishop4)

        rook1 = Rook("White", Position(0, 0))
        rook2 = Rook("White", Position(7, 0))
        rook3 = Rook("Black", Position(0, 7))
        rook4 = Rook("Black", Position(7, 7))
        self.pieces.append(rook1)
        self.pieces.append(rook2)
        self.pieces.append(rook3)
        self.pieces.append(rook4)

        queen1 = Queen("White", Position(3, 0))
        queen2 = Queen("Black", Position(3, 7))
        self.pieces.append(queen1)
        self.pieces.append(queen2)

        king1 = King("White", Position(4, 0))
        king2 = King("Black", Position(4, 7))
        self.pieces.append(king1)
        self.pieces.append(king2)

        for piece in self.pieces:
            self.add_piece(piece)

    def add_piece(self, piece):
        position = piece.position
        self.board[position.j][position.i] = piece

    def set_piece(self, piece, position):
        self.board[position.j][position.i] = piece

    def get_piece(self, position):
        return self.board[position.j][position.i]
