import pygame
import pygame.image


class Board():

    def __build_board(self):
        self.board = []
        for i in range(8):
            new = []
            for j in range(8):
                new.append(None)
            self.board.append(new)

    def __init__(self, screen):
        self.screen = screen
        self.__build_board()
       
    def draw(self):
        yPosition = 100
        whiteSquare = (255, 255, 255)
        greySquare = (160, 160, 160)
        backgroundColor = (102, 178, 255)
        self.screen.fill(backgroundColor)
        for i in range (4):
            for j in range(4):
                pygame.draw.rect(self.screen, whiteSquare, pygame.Rect(100, yPosition, 100, 100))
                pygame.draw.rect(self.screen, greySquare, pygame.Rect(200, yPosition, 100, 100))            
                pygame.draw.rect(self.screen, whiteSquare, pygame.Rect(300, yPosition, 100, 100))
                pygame.draw.rect(self.screen, greySquare, pygame.Rect(400, yPosition, 100, 100))  
                pygame.draw.rect(self.screen, whiteSquare, pygame.Rect(500, yPosition, 100, 100))
                pygame.draw.rect(self.screen, greySquare, pygame.Rect(600, yPosition, 100, 100))  
                pygame.draw.rect(self.screen, whiteSquare, pygame.Rect(700, yPosition, 100, 100))
                pygame.draw.rect(self.screen, greySquare, pygame.Rect(800, yPosition, 100, 100))  
                pygame.draw.rect(self.screen, greySquare, pygame.Rect(100, yPosition + 100, 100, 100))
                pygame.draw.rect(self.screen, whiteSquare, pygame.Rect(200, yPosition + 100, 100, 100))            
                pygame.draw.rect(self.screen, greySquare, pygame.Rect(300, yPosition + 100, 100, 100))
                pygame.draw.rect(self.screen, whiteSquare, pygame.Rect(400, yPosition + 100, 100, 100))  
                pygame.draw.rect(self.screen, greySquare, pygame.Rect(500, yPosition + 100, 100, 100))
                pygame.draw.rect(self.screen, whiteSquare, pygame.Rect(600, yPosition + 100, 100, 100))  
                pygame.draw.rect(self.screen, greySquare, pygame.Rect(700, yPosition + 100, 100, 100))
                pygame.draw.rect(self.screen, whiteSquare, pygame.Rect(800, yPosition + 100, 100, 100))        
            yPosition += 200