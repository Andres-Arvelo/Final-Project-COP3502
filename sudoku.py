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
easybutton, mediumbutton, hardbutton, exitBtn, restartBtn, resetBtn = [None] * 6
game_board = None

def startscreen():
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

def gameWinScreen():
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    font = pygame.font.SysFont('arial', 36)

    text = font.render("Game Won!", True, black)
    text_rect = text.get_rect()
    text_rect.centerx = 270
    text_rect.centery = 150
    screen.blit(text, text_rect) 

    #ExitButton
    exitBtn = pygame.Rect(210, 400, 120, 40)
    pygame.draw.rect(screen, orange, exitBtn)
    exitTxt = font.render("Exit", True, black)

    exitTxt_rect = exitTxt.get_rect(center = exitBtn.center)
    screen.blit(exitTxt, exitTxt_rect)
    return exitBtn

def gameOverScreen():
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    font = pygame.font.SysFont('arial', 36)

    text = font.render("Game Over :(", True, black)
    text_rect = text.get_rect()
    text_rect.centerx = 270
    text_rect.centery = 150
    screen.blit(text, text_rect) 

    #ExitButton
    restartBtn = pygame.Rect(210, 400, 120, 40)
    pygame.draw.rect(screen, orange, restartBtn)
    restartTxt = font.render("Restart", True, black)

    restartTxt_rect = restartTxt.get_rect(center = restartBtn.center)
    screen.blit(restartTxt, restartTxt_rect)
    return restartBtn

def gameScreen():
    if game_board:
        game_board.draw()

    font = pygame.font.SysFont('arial', 20)

    #reset
    resetBtn = pygame.Rect(70, 560, 100, 30)
    pygame.draw.rect(screen, orange, resetBtn)
    resetTxt = font.render("Reset", True, black)


    resetTxt_rect = resetTxt.get_rect(center = resetBtn.center)
    screen.blit(resetTxt, resetTxt_rect)

    #restart
    restartBtn = pygame.Rect(210, 560, 120, 30)
    pygame.draw.rect(screen, orange, restartBtn)
    restartTxt = font.render("Restart", True, black)

    restartTxt_rect = restartTxt.get_rect(center = restartBtn.center)
    screen.blit(restartTxt, restartTxt_rect)

    #exit
    exitBtn = pygame.Rect(370, 560, 100, 30)
    pygame.draw.rect(screen, orange, exitBtn)
    exitTxt = font.render("Exit", True, black)

    exitTxt_rect = exitTxt.get_rect(center = exitBtn.center)
    screen.blit(exitTxt, exitTxt_rect)
    return resetBtn, restartBtn, exitBtn
 
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
                elif mediumbutton and mediumbutton.collidepoint(mouse_pos):
                    state = "PLAYING"
                    game_board = Board(540, 540, screen, "medium")
                elif hardbutton and hardbutton.collidepoint(mouse_pos):
                    state = "PLAYING"
                    game_board = Board(540, 540, screen, "hard")
            if exitBtn and exitBtn.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
            if restartBtn and restartBtn.collidepoint(mouse_pos):
                state = "START"
            elif state == "PLAYING":
                if game_board:
                    row_col = game_board.click(mouse_pos[0], mouse_pos[1])
                    if row_col is not None:
                        row, col = row_col
                        game_board.select(row, col)
                    if resetBtn and resetBtn.collidepoint(mouse_pos):
                        game_board.reset_to_original()
                
        #List of Key Strokes
        key_strokes = {
                1073741906: (-1, 0),
                1073741905: (1, 0),
                1073741904: (0, -1),
                1073741903: (0, 1)
        }
        
        if state == "PLAYING":
            #Sketch
            if event.type == pygame.TEXTINPUT:
                if (event.text.isdigit()):
                    game_board.sketch(int(event.text))
            if event.type == pygame.KEYDOWN and game_board.selected:
                r,c = game_board.selected
                #Place
                if event.key == pygame.K_RETURN:
                    game_board.place_number(game_board.cells[r][c].sketched_value)
                #Arrow Keys
                if event.type == pygame.KEYDOWN and event.key in key_strokes.keys():
                    game_board.select((r+key_strokes[event.key][0])%9,(c+key_strokes[event.key][1])%9)
          
    screen.fill(white)

    if state == "START":
        easybutton, mediumbutton, hardbutton = startscreen(state)
    
    elif state == "WIN":
        exitBtn = gameWinScreen()
    
    elif state == "LOSE":
        restartBtn = gameOverScreen()

    elif state == "PLAYING":
        resetBtn, restartBtn, exitBtn = gameScreen()
        if game_board:
            if game_board.is_full():
                if game_board.check_board():
                    state = "WIN"
                else:
                    state = "LOSE"
        



    pygame.display.update()



