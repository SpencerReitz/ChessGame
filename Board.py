from ScreenHandler import ScreenHandler

class Board():

    def __build_board(self):
        self.board = []
        for i in range(8):
            new = []
            for j in range(8):
                new.append(None)
            self.board.append(new)

    def __init__(self):
        self.__build_board()
       
    def draw(self):
        yPosition = 100
        whiteSquare = (255, 255, 255)
        greySquare = (160, 160, 160)
        backgroundColor = (102, 178, 255)
        ScreenHandler.drawBackground(backgroundColor)
        ScreenHandler.drawRect((200, 200), (100, 100))
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