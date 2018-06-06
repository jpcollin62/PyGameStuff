import pygame, sys, os, background
import time
from pygame.locals import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.font.init()
myfont = pygame.font.SysFont("Courier New", 50)
window_width = 1800
window_height = 1000
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)

background = background.Background("simpleback.jpeg", (0,0),window_width, window_height)

level = 3
score = 250
lives = 5
livesTitle = myfont.render("Lives", False, (255,255,255))
livesPrint = myfont.render(str(lives), False, (255,255,255))

scoreTitle = myfont.render("Score", False, (255,255,255))
scorePrint = myfont.render(str(score), False, (255,255,255))

levelTitle = myfont.render("Level", False, (255,255,255))
levelPrint = myfont.render(str(level), False, (255,255,255))

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

DISPLAYSURF = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('P.Earth')
while True: # main game loopdirection = ''
    screen.fill([255,255,255])
    screen.blit(background.image, background.rect)
    screen.blit(scoreTitle,(0,0))
    screen.blit(scorePrint, (10,50))
    screen.blit(livesTitle, (0, 900))
    screen.blit(livesPrint, (175, 900))
    screen.blit(levelTitle, (window_width-200, 0))
    screen.blit(levelPrint, (window_width-150, 50))
    for event in pygame.event.get():
        if event.type == QUIT:           
            pygame.quit()
            os._exit(1)
    pygame.display.update() 

