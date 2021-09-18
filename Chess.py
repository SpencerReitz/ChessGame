import pygame
import pygame.image
from Piece import Knight

## Makes the game screen and names the window
pygame.init()
pygame.font.init()
pygame.display.set_caption('Spencer\'s Chess Game')
screen = pygame.display.set_mode((1200, 1000))

# Sets the colors on the board and in the background
whiteSquare = (255, 255, 255)
greySquare = (160, 160, 160)
backgroundColor = (102, 178, 255)

# Initializes the piece images
BK = pygame.image.load("BlackKing.png")
BK = pygame.transform.scale(BK, (100, 100)) 

# Just places the base game
def initialGameState():
    screen.blit(BK, (100, 100))
    BN = Knight('BlackKnight.png', (100, 100), 'black', screen)
    BN.draw()

# Callable funition that will draw an 8x8 chess board with grey and white squares and a blue background
def boardCreation():
    screen.fill(backgroundColor)
    yPosition = 100
    for i in range (4):
        for j in range(4):
            pygame.draw.rect(screen, whiteSquare, pygame.Rect(100, yPosition, 100, 100))
            pygame.draw.rect(screen, greySquare, pygame.Rect(200, yPosition, 100, 100))            
            pygame.draw.rect(screen, whiteSquare, pygame.Rect(300, yPosition, 100, 100))
            pygame.draw.rect(screen, greySquare, pygame.Rect(400, yPosition, 100, 100))  
            pygame.draw.rect(screen, whiteSquare, pygame.Rect(500, yPosition, 100, 100))
            pygame.draw.rect(screen, greySquare, pygame.Rect(600, yPosition, 100, 100))  
            pygame.draw.rect(screen, whiteSquare, pygame.Rect(700, yPosition, 100, 100))
            pygame.draw.rect(screen, greySquare, pygame.Rect(800, yPosition, 100, 100))  
            pygame.draw.rect(screen, greySquare, pygame.Rect(100, yPosition + 100, 100, 100))
            pygame.draw.rect(screen, whiteSquare, pygame.Rect(200, yPosition + 100, 100, 100))            
            pygame.draw.rect(screen, greySquare, pygame.Rect(300, yPosition + 100, 100, 100))
            pygame.draw.rect(screen, whiteSquare, pygame.Rect(400, yPosition + 100, 100, 100))  
            pygame.draw.rect(screen, greySquare, pygame.Rect(500, yPosition + 100, 100, 100))
            pygame.draw.rect(screen, whiteSquare, pygame.Rect(600, yPosition + 100, 100, 100))  
            pygame.draw.rect(screen, greySquare, pygame.Rect(700, yPosition + 100, 100, 100))
            pygame.draw.rect(screen, whiteSquare, pygame.Rect(800, yPosition + 100, 100, 100))        
        yPosition += 200

# Starts the game
game = True



# Main game loop
while game:

    # Makes sure there is no errors and will quit the program if something goes wrong
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            game = False
    # Calling the board creation to get an initial chess board
    boardCreation()
    initialGameState()

    # Displays everything made before this point
    pygame.display.flip()