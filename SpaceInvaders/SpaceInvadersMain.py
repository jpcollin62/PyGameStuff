import pygame, os, time, random, PlayerObject, EnemyObject, ItemObject, ProjectileObject, background

def backDrop():
    surface.blit(background.image, background.rect)
    surface.blit(scoreTitle,(0,0))
    surface.blit(scorePrint, (10,50))
    surface.blit(livesTitle, (0, 600))
    surface.blit(livesPrint, (175, 600))
    surface.blit(levelTitle, (WINDOW_WIDTH-200, 0))
    surface.blit(levelPrint, (WINDOW_WIDTH-150, 50))

def allMove(enemyList):
    oneHit = False
    if len(enemyList) > 0:
        if time.time() - enemyList[0].lastMove >= 2:

            '''
            for i in range (0, len(enemyList)):
                enemyList[i].invaderMovement()
                backDrop()
                for x in range (0, len(enemyList)):
                    surface.blit(enemyList[i].image, enemyList[i].rect)
            '''
            for i in range (0, len(enemyList)):
                enemyList[i].invaderMovement()

            backDrop()
            for i in range (0, len(enemyList)):
                surface.blit(enemyList[i].image, enemyList[i].rect)
            


            for i in range (len(enemyList)):
                if enemyList[i].checkMove(WINDOW_WIDTH, WINDOW_HEIGHT):
                    oneHit = True
                    break

            if oneHit == True:
                for i in range (0, len(enemyList)):
                    enemyList[i].moveDown()



os.environ['SDL_VIDEO_CENTERED'] = '1'#centres the window
pygame.init()





WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)
pygame.display.set_caption("Space Invaders")
enemies = []
items = []
startItems = []
projectileList = []
shotGone = 1#variable for when the last shot was fired


background = background.Background("simpleback.jpeg", (0,0),WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.font.init()
myfont = pygame.font.SysFont("Courier New", 50)
level = 3
score = 250
lives = 5
livesTitle = myfont.render("Lives", False, (255,255,255))
livesPrint = myfont.render(str(lives), False, (255,255,255))

scoreTitle = myfont.render("Score", False, (255,255,255))
scorePrint = myfont.render(str(score), False, (255,255,255))

levelTitle = myfont.render("Level", False, (255,255,255))
levelPrint = myfont.render(str(level), False, (255,255,255))

#makes player
player = PlayerObject.Player()
player.rect.left = 450
player.rect.top = 600

#makes enemies and appends them to the list of enemies
for i in range(8):
    tempEnemy = EnemyObject.Enemy(0,0, i*75 + 31, 100, enemies)


while True:
    backDrop()
    #moves all enemies
    allMove(enemies)

    surface.blit(player.image, player.rect)

    for i in range (len(enemies)):#makes enemies appear and move
        enemies[i].appear(surface)
        enemies[i].movement(WINDOW_WIDTH, WINDOW_HEIGHT)

    player.LRMovement(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    #moves player
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE] and time.time() - shotGone >= 0.5: #leaves a gap before the enxt shot can be fired
        projectile= player.shoot(surface, projectileList)
        if projectile != False:
            projectileList.append(projectile)

    #removes projectiles if they leave the screen
    if len(projectileList)>0:
        if projectileList[0].rect.bottom<=0:
            shotGone = projectileList[0].killBullet(projectileList)

    #moves the projectiles and checks if the projectile hits the enemies
    if len(projectileList) > 0:
        for i in range (len(projectileList)):
            projectileList[i].move()

            #Checks if projectiles hit enemy
            collisionStatus = projectileList[i].checkHit(enemies, projectileList)#removes the projectile and saves the time that it hit the enemy
            if collisionStatus:
                shotGone = projectileList[i].killBullet(projectileList)


    #pygame.time.wait(1)
    pygame.display.update()
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:#hit the x and ends game
            pygame.quit()
            os._exit(1)

