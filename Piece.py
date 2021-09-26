from ScreenHandler import ScreenHandler

class Piece:
    def __init__(self, image, location, color):
        self.image    = image
        self.location = location
        self.color    = color

    def draw(self):
        ScreenHandler.drawSprite(
            self.image,
            (100, 100),
            ((self.location[1] + 1) * 100, (self.location[0] + 1) * 100)
        )

    def clickedPiece(self, newLocation):
        if ((newLocation[0] == self.location[0]) and (newLocation[1] == self.location[1])):
            print(self.location)

    def movePiece(self, location):
        self.loaction = location

class Knight(Piece):
    pass

class Rook(Piece):
    pass

class Pawn(Piece):
    def __init__(self, image, location, color):
        super().__init__(image, location, color)
        self.first_move = True

    def getMoves(self):
        if (self.first_move):
            #one or two given not blocked
            self.first_move = False
        else:
            #one, given not blocked
            pass

class Queen(Piece):
    pass

class Bishop(Piece):
    pass

class King(Piece):
    pass
