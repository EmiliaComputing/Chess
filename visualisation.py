import arcade
import chess
from piece import Position
import time

#promotion pieces
from queen import Queen
from rook import Rook
from bishop import Bishop
from knight import Knight

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

        #game variables
        self.chess_game = chess.Game()
        self.squares = arcade.SpriteList()
        self.pieces = arcade.SpriteList()
        self.held_piece_img = None
        self.held_piece = None

        #position
        self.start_pos = None
        self.end_pos = None

        #display
        self.show_window = False

        #promotion
        self.is_promoting = False
        self.promotion_square = None

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

    def promote(self, held_piece_img, end_pos):
        self.is_promoting = True
        self.show_window = True

        self.queen_sprite = arcade.Sprite(f"Images/white_queen.png", 0.5)
        self.queen_sprite.set_position(SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2)
        self.queen_sprite.name = "queen"
        self.pieces.append(self.queen_sprite)

        self.rook_sprite = arcade.Sprite(f"Images/white_rook.png", 0.5)
        self.rook_sprite.set_position(SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2)
        self.rook_sprite.name = "rook"
        self.pieces.append(self.rook_sprite)

        self.bishop_sprite = arcade.Sprite(f"Images/white_bishop.png", 0.5)
        self.bishop_sprite.set_position(SCREEN_WIDTH/2 + 50, SCREEN_HEIGHT/2)
        self.bishop_sprite.name = "bishop"
        self.pieces.append(self.bishop_sprite)

        self.knight_sprite = arcade.Sprite(f"Images/white_knight.png", 0.5)
        self.knight_sprite.set_position(SCREEN_WIDTH/2 + 150, SCREEN_HEIGHT/2)
        self.knight_sprite.name = "knight"
        self.pieces.append(self.knight_sprite)

    def draw_window(self):
        #add later:
        #start_game_message = "Good luck!"
        #end_game_message = f"{colour} won"
        #check_message = "Check"

        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 400, 200, arcade.color.RHYTHM)
        arcade.draw_rectangle_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 380, 180, arcade.color.BLACK, 5)

    def on_draw(self):
        arcade.start_render()
        self.squares.draw()
        self.pieces.draw()

        if self.show_window == True:
            self.draw_window()

            if self.is_promoting == True:
                self.pieces.draw()

    def remove_promotion_sprites(self):
        if self.queen_sprite:
            self.pieces.remove(self.queen_sprite)
        if self.rook_sprite:
            self.pieces.remove(self.rook_sprite)
        if self.bishop_sprite:
            self.pieces.remove(self.bishop_sprite)
        if self.knight_sprite:
            self.pieces.remove(self.knight_sprite)

    def on_mouse_press(self, x, y, buttons, modifiers):
        pieces_clicked = arcade.get_sprites_at_point((x, y), self.pieces)
        if pieces_clicked and not self.show_window:
            indices = self.indices(x, y)
            self.held_piece_img = pieces_clicked[0]
            self.held_piece = self.chess_game.board[indices.j][indices.i]
            self.start_pos = indices

        if pieces_clicked and self.show_window:
            for piece in pieces_clicked:
                if piece.name:
                    piece_type = piece.name

                    if self.promotion_square.j == 0:
                        colour = "Black"

                    else:
                        colour = "White"

                    if piece.name == "queen":
                        new_piece = Queen(colour, self.promotion_square)
                        new_sprite = arcade.Sprite(f"Images/{colour.lower()}_queen.png", 0.5)
                        self.pieces.append(new_sprite)

                    elif piece.name == "rook":
                        new_piece = Rook(colour, self.promotion_square)
                        new_sprite = arcade.Sprite(f"Images/{colour.lower()}_rook.png", 0.5)
                        self.pieces.append(new_sprite)

                    elif piece.name == "bishop":
                        new_piece = Bishop(colour, self.promotion_square)
                        new_sprite = arcade.Sprite(f"Images/{colour.lower()}_bishop.png", 0.5)
                        self.pieces.append(new_sprite)

                    elif piece.name == "knight":
                        new_piece = Knight(colour, self.promotion_square)
                        new_sprite = arcade.Sprite(f"Images/{colour.lower()}_knight.png", 0.5)
                        self.pieces.append(new_sprite)

                    self.chess_game.set_piece(new_piece, self.promotion_square)
                    print(self.promotion_square)
                    new_sprite.set_position(*self.coordinates(self.promotion_square))

                    self.remove_promotion_sprites()

                    self.show_window = False
                    self.is_promoting = False

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.held_piece_img:
            self.held_piece_img.center_x += dx
            self.held_piece_img.center_y += dy

    def on_mouse_release(self, x, y, buttons, modifiers):
        if not self.held_piece:
            return

        self.end_pos = self.indices(x, y)

        if self.held_piece.is_valid_move(self.start_pos, self.end_pos, self.chess_game):
            self.chess_game.white_move += 1

            if self.chess_game.white_move ==2:
                self.chess_game.white_move = 0

            if ((self.end_pos.j == 0 or self.end_pos.j == 7) and
                self.chess_game.get_piece(self.start_pos).name == "Pawn"):
                self.promote(self.held_piece_img, self.end_pos)

                piece = self.chess_game.get_piece(self.end_pos)

                self.pieces.remove(self.held_piece_img)

                self.is_promoting = True
                self.promotion_square = self.end_pos
                self.show_window = True

            self.held_piece_img.set_position(*self.coordinates(self.end_pos))

            self.chess_game.set_piece("", self.start_pos)
            self.chess_game.set_piece(self.held_piece, self.end_pos)

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

                if piece.colour == "Black":
                    if (position.i == piece.position.i) and (position.j == piece.position.j - 2):
                        self.pieces.remove(image)

                elif piece.colour == "White":
                    if (position.i == piece.position.i) and (position.j == piece.position.j + 2):
                        self.pieces.remove(image)

        for piece in self.chess_game.pieces:
            if piece.name == "Rook":
                if piece.is_kingside_castling:
                    self.chess_game.set_piece("", piece.position)
                    self.chess_game.set_piece(piece, Position(piece.position.i -2, piece.position.j))

game = Game()
game.setup_board()
game.setup_pieces()

arcade.run()
