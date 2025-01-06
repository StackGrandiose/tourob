import pygame
import sys
from pygame.locals import *

pygame.init()

BLACK = (0,  0,  0)
GRAY = (99, 99, 99)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
MARGIN = 20
MATRIX_HEIGHT = 5
MATRIX_WIDTH = 4

square_size = 100


GridWidthpx = (MATRIX_WIDTH * square_size) + (MATRIX_WIDTH * square_size // 10)
GridHeightpx = (MATRIX_HEIGHT * square_size) + (MATRIX_HEIGHT * square_size // 10)
square_x = GridWidthpx // 4 - square_size // 4
square_y = GridHeightpx // 4 - square_size // 4

square_x_orig = square_x

displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('tourob GUI')

displaySurface.fill(WHITE)

for y in range(MATRIX_HEIGHT):
    square_x = square_x_orig
    pygame.draw.rect(displaySurface, BLACK, (square_x, square_y, MARGIN, square_size))
    for x in range(MATRIX_WIDTH):
        pygame.draw.rect(displaySurface, BLACK, (square_x - MARGIN, square_y, MARGIN, square_size))
        pygame.draw.rect(displaySurface, GRAY, (square_x, square_y, square_size, square_size))
        square_x += square_size + MARGIN
    pygame.draw.rect(displaySurface, BLACK, (square_x - MARGIN, square_y, MARGIN, square_size))
    square_y += square_size + MARGIN
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
