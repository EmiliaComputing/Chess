# Chess Project

### Introduction
I decided to create a working chess game as it is a game I am passionate about. This project is the most important one to me and it is the one which I have spent the most time working on. The target audience is chess players.

My project is for two players and when opened, an electronic chess board is displayed on the screen. After every move, it checks whether the move is a legal move and if not, it cannot be played. Special moves such as en passant and castling have also been included as features of this project. 

A different feature of this project was that the program keeps track of whose move it is and does not allow a colour to move outside of its own turn, making it easier for the users as they would not have to do this themselves.

### Project Goals/Requirements
I decided to code this project using python because I wanted to use the arcade library as a way of displaying the graphics. 

As this was a large project, I put every class into a separate file to make it easier to search for bugs when they occurred. Six of the files determine how each of the pieces move, one file (piece.py) controls all of the pieces and determines whether special moves such as en passant are legal as well as deciding whether it was a move for white or a move for black, another file (chess.py) keeps track of which piece is on which square and the final file (visualisation.py) displays the chess board and pieces. 

Two of the subroutines included in this project are the functions which take place when a pawn is promoted.

The end goal of the project was to have a playable chess game for two players which could identify which moves were legal and which were not as well as allowing special moves such as castling and en passant to take place.

### Design
This program has a graphical user interface and the user interacts with this program by clicking and dragging the pieces to move them to their chosen square.

There are not usually buttons on the screen, however, when a pawn is promoted, buttons appear on the screen which allow the user to select the piece which they want to promote the pawn to. If these buttons are present, they appear in a coloured box in the centre of the chess board. Once the piece has been selected, the buttons on the screen are removed and the chess board returns to its normal state.

Furthermore, the colours I have used for the chess board are light and dark grey as these are typical colours used on both online and real life chess boards. For the box which appears when a pawn is promoted, I used the colour “rhythm” from the arcade library which is a blue-grey colour, as I felt that it was visually appealing and looked pleasant against the colours which I used in the chess board.

The following pseudocode shows how the rook piece moves:
'''
FOR z IN RANGE 8:
   y_difference = y position at start - y position at end
   x_difference = x position at start - x position at end
   end_piece = board.get_piece(the piece on the end square if any is present)


   IF absolute y_difference = z AND IF absolute x_difference = 0:
      IF NOT end_piece:
         RETURN TRUE
      END IF

      IF end_piece AND end_piece NOT = colour of own pieces:
         RETURN TRUE
      END IF
   END IF

   IF absolute x_difference = z AND IF absolute y_difference = 0:
      IF NOT end_piece:
         RETURN TRUE
      END IF

      IF end_piece AND end_piece NOT = colour of own pieces:
         RETURN TRUE
      END IF
   END IF
'''

###  Issues during the project and how I resolved them
Whilst creating this project, I encountered some errors including that there was also a problem which occurred when a pawn was promoted. This error resulted in problems such as the selected piece not appearing on the board. This was fixed by appending the pieces to the pieces list, thus allowing them to be visible on the screen.

Additionally, one issue which happened whilst this project was being made was an issue involving the chess move en passant. With this issue, the piece which was being taken would not be removed from the board, therefore stopping en passant from working. This was an issue as there was a maths error in the process which found the square of the piece being taken; it was resolved by subtracting two from the maths at the point where the pawn was removed from the board rather than the point where the variable was declared. 

Another error which occurred during the making of this program was created when I moved each class into a separate file. A circular error happened when I was importing the different classes into each file. This was fixed by changing the order in which the different classes were imported into the separate files.  

### Evaluation
I feel that the project went well because I overcame the errors which occurred during the making of this program and that it achieved the overall aim which I had set for the project. This project has fulfilled my expectations and has been successful in accomplishing the final purpose of the project. 

Moreover, I experienced a variety of difficulties and errors whilst completing this project including an issue with en passant, an issue with promotion and a circular error. I was successful in overcoming these problems and achieving my final goal of building a working chess game which could identify whether or not a move was legal and could then not allow illegal moves to take place.

If I were to do this project again, I would check the maths involved before it was needed in order to eliminate errors which may occur as a result of faulty mathematical equations. I would also ensure that circular errors would not occur whilst importing classes into different files. Finally, I would start building my project with each class in a separate file rather than adding that feature later in the process of creating the project.

