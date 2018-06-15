import pygame, os, time, random, PlayerObject, EnemyObject, ItemObject, ProjectileObject, background, threading
def outputDirect():
    ''' Outputs the click space start line '''
    screen.blit(directions, (200,200))

def loop_play():
    is_playing = True
    start = True
    pygame.mixer.music.load("PaydayMusic.mp3")
    while is_playing:
        pygame.mixer.music.play()
        pygame.time.wait(194800)
        
def press_button_play():
    global is_playing
    global my_thread

    if not is_playing:
        is_playing = True
        my_thread = threading.Thread(target=loop_play)
        my_thread.start()
    
def backDrop():
    livesTitle = myfont.render("Lives", False, (255,255,255))
    livesPrint = myfont.render(str(lives), False, (255,255,255))

    scoreTitle = myfont.render("Score", False, (255,255,255))
    scorePrint = myfont.render(str(score), False, (255,255,255))

    levelTitle = myfont.render("Level", False, (255,255,255))
    levelPrint = myfont.render(str(level), False, (255,255,255))

    
    surface.blit(background.image, background.rect)
    surface.blit(scoreTitle,(0,0))
    surface.blit(scorePrint, (10,50))
    surface.blit(livesTitle, (0, 850))
    surface.blit(livesPrint, (175, 850))
    surface.blit(levelTitle, (WINDOW_WIDTH-200, 0))
    surface.blit(levelPrint, (WINDOW_WIDTH-150, 50))

def allMove(enemyList):
    oneHit = False
    playerDead = False
    if len(enemyList) > 0:
        if time.time() - enemyList[0].lastMove >= 0.3:#moves the enemies every 0.3 secs
            for i in range (0, len(enemyList)):
                enemyList[i].invaderMovement()

            for i in range (len(enemyList)): #gives the chance for enemies to shoot
                enemyBullet = enemyList[i].shootChance()
                if enemyBullet == False:
                    pass
                else:
                    enemyProjectiles.append(enemyBullet)
                
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
                    if enemyList[i].rect.bottom >= player.rect.top:#checks if the enemies reached the player
                        return True
                return False


def spawnEnemies():
    '''makes enemies and appends them to the list of enemies'''
    for x in range (1,6):
        for i in range(11):
            tempEnemy = EnemyObject.Enemy(0,0, i*75 + 31, x*50, enemies, surface)

def reset():
    '''respawns all enemies and decreases the user's lives when the get killed'''
    global lives, enemies
    
    enemies = []
    projectileList = []
    player.rect.left = 450
    player.rect.top = 800
    lives = lives -1
    spawnEnemies()
    
                        
                



os.environ['SDL_VIDEO_CENTERED'] = '1'#centres the window
pygame.init()

pygame.mixer.init()
is_playing = False


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 900


backgroundTitle = background.Background("TitleBack.jpg", (0,0),WINDOW_WIDTH, WINDOW_HEIGHT)
baddieImage = pygame.image.load("Enemy2.png")
baddieImage = pygame.transform.scale(baddieImage, (300,300))
baddieImagechange = pygame.image.load("Enemy2change.png")
baddieImagechange = pygame.transform.scale(baddieImagechange, (300,300))

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)
pygame.display.set_caption("Space Invaders")
enemies = []
items = []
startItems = []
projectileList = []
enemyProjectiles = []
enemyProjectileRemove = []
shotGone = 1#variable for when the last shot was fired
playerDead = False#variable for when the invaders have reached the bottom
running = True


background = background.Background("simpleback.jpeg", (0,0),WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.font.init()
myfont = pygame.font.SysFont("Courier New", 50)
level = 0
score = 0
lives = 3
goodLuckOut = myfont.render("Good Luck!", False, (255,255,255))

#makes player
player = PlayerObject.Player()
player.rect.left = 450
player.rect.top = 800



title = myfont.render("SPACE INVADERS", False, (255,255,255))
directions = myfont.render("<Press Space to Start>", False,(255,255,255))

directOn = True
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
titleOn = True
while titleOn == True:
    if is_playing == False:
        press_button_play()
    screen.fill([0,0,0])
    screen.blit(backgroundTitle.image, backgroundTitle.rect)
    if directOn == True:
        outputDirect()
        screen.blit(baddieImage, (100,400))
        directOn = False
    elif directOn == False:
        screen.blit(baddieImagechange, (100,400))
        directOn = True
    screen.blit(title, (430, 560))
    pygame.time.wait(500)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.blit(goodLuckOut, (WINDOW_WIDTH-500, WINDOW_HEIGHT-200))
                titleOn = False
                break
        elif event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)

    pygame.display.update()





spawnEnemies()

pygame.time.wait(500)

while running:      
    backDrop()
    #moves all enemies
    playerDead = allMove(enemies)

    if playerDead == True:
        reset()

    surface.blit(player.image, player.rect)

    for i in range (len(enemies)):#makes enemies appear and move
        enemies[i].appear(surface)
        enemies[i].movement(WINDOW_WIDTH, WINDOW_HEIGHT)

    player.LRMovement(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    #moves the player
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE] and time.time() - shotGone >= 0.1: #leaves a gap before the enxt shot can be fired
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
                score += 50
                shotGone = projectileList[i].killBullet(projectileList)
    #moves enemy projectiles
    if len(enemyProjectiles) > 0:
        for i in range (len(enemyProjectiles)):
            enemyProjectiles[i].enemyBulletMove()
            if enemyProjectiles[i].rect.bottom >= WINDOW_HEIGHT:
                enemyProjectileRemove.append(i)#adds the projectile to the list of projectiles to be removed

    #removes projectiles
    if len(enemyProjectileRemove) > 0:
        for i in range (len(enemyProjectileRemove)):
            enemyProjectiles.pop(enemyProjectileRemove[i])
        enemyProjectileRemove = []

    print (len(enemyProjectiles))
    
    #pygame.time.wait(1)
    pygame.display.update()
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:#hit the x and ends game
            pygame.quit()
            os._exit(1)

