import pygame, sys
from pygame.key import start_text_input
from sudoku_generator import SudokuGenerator
from cell import Cell
from board import Board


pygame.init()
white = (255,255,255)
black = (0,0,0)
orange = (255, 140, 0)
green = (0, 255, 0)
red = (255,0,0)
screen = pygame.display.set_mode((540, 600)) #Creates the screen
pygame.display.set_caption("Sudoku") #makes the caption
screen.fill(white)
state = "START"
easybutton, mediumbutton, hardbutton = None, None, None
game_board = None

def startscreen(state):
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    font = pygame.font.SysFont('arial', 36)

    text = font.render("START", True, black)
    text_rect = text.get_rect()
    text_rect.centerx = 270
    text_rect.centery = 150
    screen.blit(text, text_rect)

    #Easyt button section
    easybutton = pygame.Rect(70, 400, 100, 40)
    pygame.draw.rect(screen, green, easybutton)
    easytext = font.render("Easy", True, black)


    easytext_rect = easytext.get_rect(center = easybutton.center)
    screen.blit(easytext, easytext_rect)

    #medium button
    mediumbutton = pygame.Rect(210, 400, 120, 40)
    pygame.draw.rect(screen, orange, mediumbutton)
    mediumtext = font.render("Medium", True, black)

    mediumtext_rect = mediumtext.get_rect(center = mediumbutton.center)
    screen.blit(mediumtext, mediumtext_rect)

    #hard button
    hardbutton = pygame.Rect(370, 400, 100, 40)
    pygame.draw.rect(screen, red, hardbutton)
    hardtext = font.render("Hard", True, black)

    hardtext_rect = hardtext.get_rect(center = hardbutton.center)
    screen.blit(hardtext, hardtext_rect)
    return easybutton, mediumbutton, hardbutton




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #allows for user to click out of sudoku
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if state == "START":
                if easybutton and easybutton.collidepoint(mouse_pos):
                    state = "PLAYING"
                    game_board = Board(540, 540, screen, "easy")
                if mediumbutton and mediumbutton.collidepoint(mouse_pos):
                    state = "PLAYING"
                    game_board = Board(540, 540, screen, "medium")
                if hardbutton and hardbutton.collidepoint(mouse_pos):
                    state = "PLAYING"
                    game_board = Board(540, 540, screen, "hard")

            elif state == "PLAYING":
                if game_board:
                    row_col = game_board.click(mouse_pos[0], mouse_pos[1])
                    if row_col:
                        row, col = row_col
                        game_board.select(row, col)


    screen.fill(white)

    if state == "START":
        easybutton, mediumbutton, hardbutton = startscreen(state)

    if state == "PLAYING":
        if game_board:
            game_board.draw()



    pygame.display.update()

