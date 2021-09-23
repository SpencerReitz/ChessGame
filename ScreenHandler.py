import pygame
import pygame.image
from pygame.image import load

class ScreenHandler():
    screen_width = 1200
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))

    def drawSprite(spriteName: str, scale : tuple, location: tuple):
        image = load(f"assets/sprites/{spriteName}.png")
        scaledImage = pygame.transform.scale(image, scale)
        ScreenHandler.screen.blit(scaledImage, location)

    def drawBackground(color):
        ScreenHandler.screen.fill(color)

    def drawRect(location, dimension, color = (255, 0, 0)):
        pygame.draw.rect(
            ScreenHandler.screen,
            color,
            pygame.Rect(
                location,
                dimension
            )
        )

