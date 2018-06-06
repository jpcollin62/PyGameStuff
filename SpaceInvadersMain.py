import pygame, os,random, PlayerObject, EnemyObject, ItemObject, ProjectileObject
#github
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

#makes player
player = PlayerObject.Player()
player.rect.left = 450
player.rect.top = 600

#makes enemies and appends them to the list of enemies
tempEnemy = EnemyObject.Enemy(0,0, 200,100, enemies)#creates an enemy an appends it to the list

tempEnemy = EnemyObject.Enemy(5,0, 300,0, enemies)

tempEnemy = EnemyObject.Enemy(3,0, 69, 400, enemies)


while True:
    #makes sprites appear
    surface.fill((0,0,0))

    surface.blit(player.image, player.rect)

    for i in range (len(enemies)):#makes enemies appear and move
        enemies[i].appear(surface)
        enemies[i].movement(WINDOW_WIDTH, WINDOW_HEIGHT)

    player.LRMovement(WINDOW_WIDTH, WINDOW_HEIGHT)
    

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        projectile= player.shoot(surface, projectileList)
        if projectile != False:
            projectileList.append(projectile)

    #removes projectiles if they leave the screen
    if len(projectileList)>0:
        if projectileList[0].rect.bottom<=0:
            projectileList.pop(0)

    #moves the projectiles
    if len(projectileList) > 0:
        for i in range (len(projectileList)):
            projectileList[i].move()

            #Checks if projectiles hit enemy
            projectileList[i].checkHit(enemies)
        


    pygame.time.wait(10)
    pygame.display.update()
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:#hit the x and ends game
            pygame.quit()
            os._exit(1)
