class Game:
    def __init__(self):
        
        self.board = [["" for i in range(8)] for i in range(8)]
        self.pieces = []
        
        for i in range(8):
            pawn = Pawn("White",(i, 1))
            self.pieces.append(pawn)
            
        for i in range(8):
            pawn = Pawn("Black",(i, 6))
            self.pieces.append(pawn)

        knight1 = Knight("White",(1, 0))
        knight2 = Knight("White",(6, 0))
        knight3 = Knight("Black",(1, 7))
        knight4 = Knight("Black",(6, 7))
        self.pieces.append(knight1)
        self.pieces.append(knight2)
        self.pieces.append(knight3)
        self.pieces.append(knight4)

        bishop1 = Bishop("White",(2, 0))
        bishop2 = Bishop("White",(5, 0))
        bishop3 = Bishop("Black",(2, 7))
        bishop4 = Bishop("Black",(5, 7))
        self.pieces.append(bishop1)
        self.pieces.append(bishop2)
        self.pieces.append(bishop3)
        self.pieces.append(bishop4)

        rook1 = Rook("White", (0, 0))
        rook2 = Rook("White", (7, 0))
        rook3 = Rook("Black", (0, 7))
        rook4 = Rook("Black", (7, 7))
        self.pieces.append(rook1)
        self.pieces.append(rook2)
        self.pieces.append(rook3)
        self.pieces.append(rook4)

        queen1 = Queen("White", (3, 0))
        queen2 = Queen("Black", (3, 7))
        self.pieces.append(queen1)
        self.pieces.append(queen2)

        king1 = King("White", (4, 0))
        king2 = King("Black", (4, 7))
        self.pieces.append(king1)
        self.pieces.append(king2)

        for piece in self.pieces:
            self.add_piece(piece)

    def display(self):
        for row in self.board:
            print(row)

    def add_piece(self, piece):
        position = piece.position
        self.board[position[1]][position[0]] = piece
                
                

class Piece:
    def __init__(self, colour, position, name, symbol, taken):
        self.colour = colour
        self.position = position
        self.name = name
        self.symbol = symbol
        self.taken = taken

    def __repr__(self):
        return self.symbol

class Pawn(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Pawn", "P", False)

class Knight(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Knight", "N", False)

class Bishop(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Bishop", "B", False)

class Rook(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Rook", "R", False)

class Queen(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "Queen", "Q", False)

class King(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position, "King", "K", False)


game = Game()
game.display()

