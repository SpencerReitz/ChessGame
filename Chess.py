import pygame
import pygame.image

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
BQ = pygame.image.load("BlackQueen.png")
BQ = pygame.transform.scale(BQ, (100, 100)) 
BB = pygame.image.load("BlackBishop.png")
BB = pygame.transform.scale(BB, (100, 100))
BP = pygame.image.load("BlackPawn.png")
BP = pygame.transform.scale(BP, (100, 100))
BN = pygame.image.load("BlackKnight.png")
BN = pygame.transform.scale(BN, (100, 100))
BR = pygame.image.load("BlackRook.png")
BR = pygame.transform.scale(BR, (100, 100))

WK = pygame.image.load("WhiteKing.png")
WK = pygame.transform.scale(WK, (100, 100))
WQ = pygame.image.load("WhiteQueen.png")
WQ = pygame.transform.scale(WQ, (100, 100))
WB = pygame.image.load("WhiteBishop.png")
WB = pygame.transform.scale(WB, (100, 100))
WP = pygame.image.load("WhitePawn.png")
WP = pygame.transform.scale(WP, (100, 100))
WN = pygame.image.load("WhiteKnight.png")
WN = pygame.transform.scale(WN, (100, 100))
WR = pygame.image.load("WhiteRook.png")
WR = pygame.transform.scale(WR, (100, 100))


# Just places the base game
def initialGameState():
    screen.blit(BR, (100, 100))
    screen.blit(BN, (200, 100))
    screen.blit(BB, (300, 100))
    screen.blit(BQ, (400, 100))
    screen.blit(BK, (500, 100))
    screen.blit(BB, (600, 100))
    screen.blit(BN, (700, 100))
    screen.blit(BR, (800, 100))
    screen.blit(BP, (100, 200))
    screen.blit(BP, (200, 200))
    screen.blit(BP, (300, 200))
    screen.blit(BP, (400, 200))
    screen.blit(BP, (500, 200))
    screen.blit(BP, (600, 200))
    screen.blit(BP, (700, 200))
    screen.blit(BP, (800, 200))

    screen.blit(WR, (100, 800))
    screen.blit(WN, (200, 800))
    screen.blit(WB, (300, 800))
    screen.blit(WQ, (400, 800))
    screen.blit(WK, (500, 800))
    screen.blit(WB, (600, 800))
    screen.blit(WN, (700, 800))
    screen.blit(WR, (800, 800))
    screen.blit(WP, (100, 700))
    screen.blit(WP, (200, 700))
    screen.blit(WP, (300, 700))
    screen.blit(WP, (400, 700))
    screen.blit(WP, (500, 700))
    screen.blit(WP, (600, 700))
    screen.blit(WP, (700, 700))
    screen.blit(WP, (800, 700))

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