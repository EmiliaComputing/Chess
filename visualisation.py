import arcade
import chess

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
        self.chess_game.display()
        self.squares = arcade.SpriteList()
        self.pieces = arcade.SpriteList()
        self.held_piece = None

    def setup(self):
        for j in range(8):
            for i in range(8):
                if i%2 == 0:
                    if j%2 != 0:
                        square_colour =  'Light_Square'
                    else:
                        square_colour = 'Dark_Square'
                else:
                    if j%2 == 0:
                        square_colour =  'Light_Square'
                    else:
                        square_colour = 'Dark_Square'
                        
                x = i * SQUARE_SIZE + SQUARE_SIZE//2
                y = j * SQUARE_SIZE + SQUARE_SIZE//2
                width =  SQUARE_SIZE
                height =  SQUARE_SIZE
                
                square =  SQUARE_IMAGES[square_colour]
                square_sprite = arcade.Sprite(f"Images/{square}", 0.55)
                square_sprite.center_x = x
                square_sprite.center_y = y
                self.squares.append(square_sprite)
                
                piece = self.chess_game.board[j][i]
                if piece:
                    img = PIECE_IMAGES[f"{piece.colour}_{piece.name}"]
                    piece_sprite =  arcade.Sprite(f"Images/{img}", 0.5)
                    piece_sprite.center_x = x
                    piece_sprite.center_y = y
                    self.pieces.append(piece_sprite)
                            
    def on_draw(self):
        arcade.start_render()
        self.squares.draw()
        self.pieces.draw()
    
    def on_mouse_press(self, x, y, buttons, modifiers):
        pieces_clicked = arcade.get_sprites_at_point((x, y), self.pieces)
        if pieces_clicked:
            self.held_piece = pieces_clicked[0]

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.held_piece:
            self.held_piece.center_x += dx
            self.held_piece.center_y += dy

    def on_mouse_release(self, x, y, buttons, modifiers):
        if self.held_piece:
            for square in self.squares:
                if abs(square.center_x - x) < SQUARE_SIZE // 2 and abs(square.center_y - y) < SQUARE_SIZE // 2:            
                    self.held_piece.center_x = square.center_x
                    self.held_piece.center_y = square.center_y
            
            pieces = arcade.check_for_collision_with_list(self.held_piece, self.pieces)
            
            if pieces:
                piece = pieces[0]
                self.pieces.remove(piece)

            self.held_piece = None

game = Game()
game.setup()
arcade.run()
