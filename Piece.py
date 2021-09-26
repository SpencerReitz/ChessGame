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

    def clickedPiece(self):
        print(self.getMoves())
        return self.getMoves()

    def getMoves(self):
        print('Not Implemented, Abstract')
        return []

    def movePiece(self, location):
        self.location = location
        print("Moved piece to", location)

class Knight(Piece):
    def getMoves(self):
        print('Not Implemented')
        return []

class Rook(Piece):
    def getMoves(self):
        print('Not Implemented')
        return []

class Pawn(Piece):
    def __init__(self, image, location, color):
        super().__init__(image, location, color)
        self.first_move = True

    def getMoves(self): 
        moves = []
        if (self.first_move):
            if self.color == 'b':
                moves = [(self.location[1], self.location[0] + 1), (self.location[1], self.location[0] + 2)]
            else:
                moves = [(self.location[1], self.location[0] - 1), (self.location[1], self.location[0] - 2)]
        else:
            if self.color == 'b':
                moves = [(self.location[1], self.location[0] + 1)]
            else:
                moves = [(self.location[1], self.location[0] - 1)]
        return moves

    def movePiece(self, location):
        self.first_move = False
        super().movePiece(location)

class Queen(Piece):
    def getMoves(self):
        print('Not Implemented')
        return []

class Bishop(Piece):
     def getMoves(self):
        print('Not Implemented')
        return []

class King(Piece):
    def getMoves(self):
        print('Not Implemented')
        return []
