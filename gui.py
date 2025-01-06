import pygame, sys
from pygame.locals import *

pygame.init()

BLACK = (0,  0,  0)
GRAY = (99, 99, 99)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
MARGIN = 20
GRID_HEIGHT = 5
GRID_WIDTH = 4


displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('tourob GUI')

displaySurface.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
