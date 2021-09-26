from ScreenHandler import ScreenHandler
from Piece import Pawn, Bishop, Knight, Queen, Rook, King

class Board():

    def __build_board(self):
        self.board = []
        for i in range(8):
            new = []
            for j in range(8):
                new.append(None)
            self.board.append(new)

        self.board[0][0] = Rook("WhiteRook", (0, 0), 'w')
        self.board[0][7] = Rook("WhiteRook", (0, 7), 'w')
        self.board[0][1] = Knight("WhiteKnight", (0, 1), 'w')
        self.board[0][6] = Knight("WhiteKnight", (0, 6), 'w')
        self.board[0][2] = Bishop("WhiteBishop", (0, 2), 'w')
        self.board[0][5] = Bishop("WhiteBishop", (0, 5), 'w')
        self.board[0][3] = King("WhiteKing", (0, 3), 'w')
        self.board[0][4] = Queen("WhiteQueen", (0, 4), 'w')
        self.board[1] = [Pawn("WhitePawn", (1, x), 'w') for x in range(8)]

        self.board[0][0] = Rook("BlackRook", (0, 0), 'b')
        self.board[0][7] = Rook("BlackRook", (0, 7), 'b')
        self.board[0][1] = Knight("BlackKnight", (0, 1), 'b')
        self.board[0][6] = Knight("BlackKnight", (0, 6), 'b')
        self.board[0][2] = Bishop("BlackBishop", (0, 2), 'b')
        self.board[0][5] = Bishop("BlackBishop", (0, 5), 'b')
        self.board[0][4] = King("BlackKing", (0, 4), 'b')
        self.board[0][3] = Queen("BlackQueen", (0, 3), 'b')
        self.board[1] = [Pawn("BlackPawn", (1, x), 'w') for x in range(8)]

    def __init__(self):
        self.__build_board()
       
    def draw(self):
        whiteSquare = (255, 255, 255)
        greySquare = (160, 160, 160)
        backgroundColor = (102, 178, 255)
        ScreenHandler.drawBackground(backgroundColor)
        rect_dim = (100, 100)
        color = whiteSquare

        for col in range(8):
            for row in range(8):
                if col % 2 == row % 2:
                    color = whiteSquare
                else:
                    color = greySquare
                ScreenHandler.drawRect(
                    ((row + 1) * 100, (col + 1) * 100), 
                    rect_dim,
                    color)

                if self.board[col][row] != None:
                    self.board[col][row].draw()