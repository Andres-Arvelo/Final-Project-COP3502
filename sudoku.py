import pygame, sys
from sudoku_generator import *

pygame.init()


screen = pygame.display.set_mode((540, 600)) #Creates the screen
pygame.display.set_caption("Sudoku") #makes the caption

screen.fill((255,255,245))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #allows for user to click out of sudoku
            pygame.quit()
            sys.exit()



    pygame.display.update()