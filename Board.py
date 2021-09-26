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

        # Pieces are in (y, x)
        self.board[7][0] = Rook("WhiteRook", (7, 0), 'w')
        self.board[7][7] = Rook("WhiteRook", (7, 7), 'w')
        self.board[7][1] = Knight("WhiteKnight", (7, 1), 'w')
        self.board[7][6] = Knight("WhiteKnight", (7, 6), 'w')
        self.board[7][2] = Bishop("WhiteBishop", (7, 2), 'w')
        self.board[7][5] = Bishop("WhiteBishop", (7, 5), 'w')
        self.board[7][4] = King("WhiteKing", (7, 4), 'w')
        self.board[7][3] = Queen("WhiteQueen", (7, 3), 'w')
        self.board[6] = [Pawn("WhitePawn", (6, x), 'w') for x in range(8)]

        self.board[0][0] = Rook("BlackRook", (0, 0), 'b')
        self.board[0][7] = Rook("BlackRook", (0, 7), 'b')
        self.board[0][1] = Knight("BlackKnight", (0, 1), 'b')
        self.board[0][6] = Knight("BlackKnight", (0, 6), 'b')
        self.board[0][2] = Bishop("BlackBishop", (0, 2), 'b')
        self.board[0][5] = Bishop("BlackBishop", (0, 5), 'b')
        self.board[0][4] = King("BlackKing", (0, 4), 'b')
        self.board[0][3] = Queen("BlackQueen", (0, 3), 'b')
        self.board[1] = [Pawn("BlackPawn", (1, x), 'b') for x in range(8)]

    def __init__(self):
        self.__build_board()
        self.last_clicked = None
        self.valid_moves = None

    def clicked(self, mouse_x, mouse_y):
        if mouse_x > 7 or mouse_x < 0 or mouse_y > 7 or mouse_y < 0:
            return
        if self.board[mouse_y][mouse_x] != None:
            self.last_clicked = self.board[mouse_y][mouse_x]
            self.valid_moves = self.board[mouse_y][mouse_x].clickedPiece()
        elif (mouse_y, mouse_x) in self.valid_moves:
            self.last_clicked.movePiece((mouse_y, mouse_x))
       
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

                if self.valid_moves != [] and self.valid_moves != None:
                    for move in self.valid_moves:
                        ScreenHandler.drawRect(
                            ((move[0] + 1) * 100, (move[1]+ 1) * 100),
                            rect_dim,
                            (0, 150, 150))
