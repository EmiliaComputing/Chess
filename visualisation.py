import arcade
import chess
from piece import Position

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "CHESS"

SQUARE_SIZE = SCREEN_WIDTH//8

PIECE_IMAGES = {"White_Pawn":"white_pawn.png",
                "White_Knight":"white_knight.png",
                "White_Bishop":"white_bishop.png",
                "White_King":"white_king.png",
                "White_Queen":"white_queen.png",
                "White_Rook":"white_rook.png",
                "Black_Pawn":"black_pawn.png",
                "Black_Knight":"black_knight.png",
                "Black_Bishop":"black_bishop.png",
                "Black_King":"black_king.png",
                "Black_Queen":"black_queen.png",
                "Black_Rook":"black_rook.png"}

SQUARE_IMAGES = {"Light_Square":"light_square.png",
                "Dark_Square":"dark_square.png"}

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.chess_game = chess.Game()
        self.squares = arcade.SpriteList()
        self.pieces = arcade.SpriteList()
        self.held_piece_img = None
        self.held_piece = None
        self.start_pos = None
        self.end_pos = None

    def coordinates(self, position):
        return position.i* SQUARE_SIZE + SQUARE_SIZE//2, position.j* SQUARE_SIZE + SQUARE_SIZE//2

    def indices(self, x, y):
        return Position(x //SQUARE_SIZE, y //SQUARE_SIZE)

    def setup_board(self):
        for j in range(8):
            for i in range(8):
                if (i+j)%2 == 0:
                    square_colour =  'Dark_Square'
                else:
                    square_colour = 'Light_Square'

                square =  SQUARE_IMAGES[square_colour]
                square_sprite = arcade.Sprite(f"Images/{square}", 0.55)

                square_sprite.set_position(*self.coordinates(Position(i, j)))
                self.squares.append(square_sprite)

    def setup_pieces(self):
         for j in range(8):
            for i in range(8):
                piece = self.chess_game.board[j][i]
                if piece:
                    img = PIECE_IMAGES[f"{piece.colour}_{piece.name}"]
                    piece_sprite =  arcade.Sprite(f"Images/{img}", 0.5)
                    piece_sprite.set_position(*self.coordinates(Position(i, j)))
                    self.pieces.append(piece_sprite)

    def on_draw(self):
        arcade.start_render()
        self.squares.draw()
        self.pieces.draw()

    def on_mouse_press(self, x, y, buttons, modifiers):
        pieces_clicked = arcade.get_sprites_at_point((x, y), self.pieces)
        if pieces_clicked:
            indices = self.indices(x, y)
            self.held_piece_img = pieces_clicked[0]
            self.held_piece = self.chess_game.board[indices.j][indices.i]
            self.start_pos = indices

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.held_piece_img:
            self.held_piece_img.center_x += dx
            self.held_piece_img.center_y += dy

    def on_mouse_release(self, x, y, buttons, modifiers):
        if  not self.held_piece:
            return
        print("finding end_pos")
        self.end_pos = self.indices(x,  y)
        print("end pos found")
        if self.held_piece.is_valid_move(self.start_pos, self.end_pos, self.chess_game):
            print("starting if statement")
            self.chess_game.white_move += 1
            if self.chess_game.white_move ==2:
                self.chess_game.white_move = 0
            print("setting img position")
            self.held_piece_img.set_position(*self.coordinates(self.end_pos))
            print("resetting start_pos")
            self.chess_game.set_piece("", self.start_pos)
            print("setting end pos")
            self.chess_game.set_piece(self.held_piece, self.end_pos)
            print("displaying board")
            self.chess_game.display()

            pieces = arcade.check_for_collision_with_list(self.held_piece_img, self.pieces)

            if pieces:
                piece_ = pieces[0]
                self.pieces.remove(piece_)

            for piece in self.chess_game.pieces:
                if (piece.name == "Pawn" and
                    piece.is_passantable):
                    piece.passant_count += 1
                    if piece.passant_count == 2:
                        piece.is_passantable = False
                        piece.passant_count = 0

        else:
            self.held_piece_img.set_position(*self.coordinates(self.start_pos))

            self.held_piece_img = None
            self.held_piece = None

        for piece in self.chess_game.pieces:
          if piece.taken:
             self.chess_game.set_piece(None, piece.position)
             for image in self.pieces:
                 position = self.indices(image.center_x, image.center_y)
                 print(f"image: {position}, piece: {piece.position}")
                 if (position.i == piece.position.i - 1) and (position.j == piece.position.j - 1):
                     self.pieces.remove(image)

game = Game()
game.setup_board()
game.setup_pieces()
arcade.run()
