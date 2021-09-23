# Top 2 lines just get rid of message saying hi from pygame community in your terminal
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame import mouse
from Board import Board

## Makes the game screen and names the window
pygame.init()
pygame.font.init()
pygame.display.set_caption('Spencer\'s Chess Game')

# Starts the game
game = True

# Create the board and piece objects
board = Board()

# A list for all pieces to live in so piece drawing is an easy loop
listOfPieces = []
clickSubscribers = []

def attach(piece):
    clickSubscribers.append(piece)

def detach(piece):
    clickSubscribers.remove(piece)

def notify(newLocation):
    for piece in clickSubscribers:
        piece.clickedPiece(newLocation)

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

    # Displays everything made before this point
    pygame.display.flip()