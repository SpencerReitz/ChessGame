import pygame
from pygame import mouse
import pygame.image
from Piece import Knight
from Piece import Rook
from Piece import Pawn
from Piece import Queen
from Piece import Bishop
from Piece import King
from Board import Board

## Makes the game screen and names the window
pygame.init()
pygame.font.init()
pygame.display.set_caption('Spencer\'s Chess Game')
screen = pygame.display.set_mode((1200, 1000))

# Starts the game
game = True

# Create the board and piece objects
board = Board(screen)

# A list for all pieces to live in so piece drawing is an easy loop
listOfPieces = []
clickSubscribers = []

BR = Rook('BlackRook.png', (0, 0), 'black', screen)
BN = Knight('BlackKnight.png', (1, 0), 'black', screen)
BB = Bishop('BlackBishop.png', (2, 0), 'black', screen)
BQ = Queen('BlackQueen.png', (3, 0), 'black', screen)
BK = King('BlackKing.png', (4, 0), 'black', screen)
BB2 = Bishop('BlackBishop.png', (5, 0), 'black', screen)
BN2 = Knight('BlackKnight.png', (6, 0), 'black', screen)
BR2 = Rook('BlackRook.png', (7, 0), 'black', screen)
BP1 = Pawn('BlackPawn.png', (0, 1), 'black', screen)
BP2 = Pawn('BlackPawn.png', (1, 1), 'black', screen)
BP3 = Pawn('BlackPawn.png', (2, 1), 'black', screen)
BP4 = Pawn('BlackPawn.png', (3, 1), 'black', screen)
BP5 = Pawn('BlackPawn.png', (4, 1), 'black', screen)
BP6 = Pawn('BlackPawn.png', (5, 1), 'black', screen)
BP7 = Pawn('BlackPawn.png', (6, 1), 'black', screen)
BP8 = Pawn('BlackPawn.png', (7, 1), 'black', screen)

listOfPieces.append(BR)
listOfPieces.append(BN)
listOfPieces.append(BB)
listOfPieces.append(BQ)
listOfPieces.append(BK)
listOfPieces.append(BB2)
listOfPieces.append(BN2)
listOfPieces.append(BR2)
listOfPieces.append(BP1)
listOfPieces.append(BP2)
listOfPieces.append(BP3)
listOfPieces.append(BP4)
listOfPieces.append(BP5)
listOfPieces.append(BP6)
listOfPieces.append(BP7)
listOfPieces.append(BP8)

WR = Rook('WhiteRook.png', (0, 7), 'white', screen)
WN = Knight('WhiteKnight.png', (1, 7), 'white', screen)
WB = Bishop('WhiteBishop.png', (2, 7), 'white', screen)
WQ = Queen('WhiteQueen.png', (3, 7), 'white', screen)
WK = King('WhiteKing.png', (4, 7), 'white', screen)
WN2 = Knight('WhiteKnight.png', (5, 7), 'white', screen)
WB2 = Bishop('WhiteBishop.png', (6, 7), 'white', screen)
WR2 = Rook('WhiteRook.png', (7, 7), 'white', screen)
WP1 = Pawn('WhitePawn.png', (0, 6), 'white', screen)
WP2 = Pawn('WhitePawn.png', (1, 6), 'white', screen)
WP3 = Pawn('WhitePawn.png', (2, 6), 'white', screen)
WP4 = Pawn('WhitePawn.png', (3, 6), 'white', screen)
WP5 = Pawn('WhitePawn.png', (4, 6), 'white', screen)
WP6 = Pawn('WhitePawn.png', (5, 6), 'white', screen)
WP7 = Pawn('WhitePawn.png', (6, 6), 'white', screen)
WP8 = Pawn('WhitePawn.png', (7, 6), 'white', screen)

listOfPieces.append(WR)
listOfPieces.append(WN)
listOfPieces.append(WB)
listOfPieces.append(WQ)
listOfPieces.append(WK)
listOfPieces.append(WB2)
listOfPieces.append(WN2)
listOfPieces.append(WR2)
listOfPieces.append(WP1)
listOfPieces.append(WP2)
listOfPieces.append(WP3)
listOfPieces.append(WP4)
listOfPieces.append(WP5)
listOfPieces.append(WP6)
listOfPieces.append(WP7)
listOfPieces.append(WP8)

def attach(piece):
    clickSubscribers.append(piece)

def detach(piece):
    clickSubscribers.remove(piece)

def notify(newLocation):
    for piece in clickSubscribers:
        piece.clickedPiece(newLocation)

for piece in listOfPieces:
    attach(piece)
# Main game loop
while game:

    # Makes sure there is no errors and will quit the program if something goes wrong
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif pygame.mouse.get_pressed()[0]:
            mouseX = int(pygame.mouse.get_pos()[0] / 100) - 1
            mouseY = int(pygame.mouse.get_pos()[1] / 100) - 1
            newLocation = (mouseX, mouseY)
            notify(newLocation)

    # Draws the board and pieces after every move
    board.draw()

    for pieces in listOfPieces:
        pieces.draw()

    # Displays everything made before this point
    pygame.display.flip()