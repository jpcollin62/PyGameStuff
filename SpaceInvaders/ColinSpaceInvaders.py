import pygame, Baddie, background, os

def backDrop():
    screen.blit(background.image, background.rect)
    screen.blit(scoreTitle,(0,0))
    screen.blit(scorePrint, (10,50))
    screen.blit(livesTitle, (0, 650))
    screen.blit(livesPrint, (175, 650))
    screen.blit(levelTitle, (window_width-200, 0))
    screen.blit(levelPrint, (window_width-150, 50))





pygame.init()


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.font.init()
myfont = pygame.font.SysFont("Courier New", 50)
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)

window_width = 1280
window_height = 720


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

for x in range (0,7):
        pos = x*200
        tempEnemy = Baddie.Baddie(pos, 100)
        myBaddies.append(tempEnemy)

while True:
    #Makes background and enemies appear
    backDrop()

    for i in range (0, len(myBaddies)):
        surface.blit(myBaddies[i].image, myBaddies[i].rect)



    #Makes enemies move
    for i in range(0, len(myBaddies)):
        if len(myBaddies) > 0:
            myBaddies[i].moveChar()
            backDrop()
            for x in range(0, len(myBaddies)):
                surface.blit(myBaddies[x].image, myBaddies[x].rect)
            
                    
            pygame.time.wait(10)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(1)
