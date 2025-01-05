import pygame, sys
from pygame.locals import *

pygame.init()

BLACK = (0,  0,  0)
GRAY = (99, 99, 99)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
GRID_HEIGHT = 5
GRID_WIDTH = 4

displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Charlie Chunker GUI Ver. 0.1')

displaySurface.fill(GRAY)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
