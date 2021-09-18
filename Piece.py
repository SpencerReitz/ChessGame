import pygame
import pygame.image

class Piece:
    def __init__(self, image, location, color, screen):
        self.image    = image
        self.location = location
        self.color    = color
        self.screen = screen

    def draw(self):
        pieceImage = pygame.image.load(self.image)
        scaledPieceImage = pygame.transform.scale(pieceImage, (100, 100))
        self.screen.blit(scaledPieceImage, ((self.location[0] + 1) * 100, (self.location[1] + 1) * 100))

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
    pass

class Queen(Piece):
    pass

class Bishop(Piece):
    pass

class King(Piece):
    pass