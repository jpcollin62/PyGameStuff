import pygame, time, Baddie, background, os

pygame.init()


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.font.init()
myfont = pygame.font.SysFont("Courier New", 50)
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)

window_width = 1600
window_height = 800


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

size = (700, 500)
screen = pygame.display.set_mode(size)

DISPLAYSURF = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('P.Earth')


surface = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Moving Spaceship")

x_move_amt = 80

#myBaddies[x] = Baddie.Baddie()
myBaddies = []

while True:
    screen.blit(background.image, background.rect)
    screen.blit(scoreTitle,(0,0))
    screen.blit(scorePrint, (10,50))
    screen.blit(livesTitle, (0, 900))
    screen.blit(livesPrint, (175, 900))
    screen.blit(levelTitle, (window_width-200, 0))
    screen.blit(levelPrint, (window_width-150, 50))
    for x in range (0,7):
        pos = x*200
        myBaddies.append(Baddie.Baddie(pos,100))
        surface.blit(myBaddies[x].image, (myBaddies[x].x, myBaddies[x].y))
        #surface.blit(Baddie.Baddie(pos,100).image, (Baddie.Baddie.getX(), Baddie.Baddie.getY()))
    
    for enemy in myBaddies:

        enemy.moveChar()
        screen.blit(background.image, background.rect)
        screen.blit(scoreTitle,(0,0))
        screen.blit(scorePrint, (10,50))
        screen.blit(livesTitle, (0, 900))
        screen.blit(livesPrint, (175, 900))
        screen.blit(levelTitle, (window_width-200, 0))
        screen.blit(levelPrint, (window_width-150, 50))
        surface.blit(enemy.image, (enemy.x, enemy.y))  
        pygame.display.update()
        time.sleep(1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)
