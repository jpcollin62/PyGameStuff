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

while True:
    surface.fill((0,0,0))
    surface.blit(player.image, player.rect)

    player.LRMovement(WINDOW_WIDTH, WINDOW_HEIGHT)
    

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        projectile= player.shoot(surface, projectileList)
        if projectile != False:
            projectileList.append(projectile)

    if len(projectileList)>0:
        print (projectileList)
        if projectileList[0].rect.bottom<=0:
            projectileList.pop(0)

    if len(projectileList) > 0:
        for i in range (len(projectileList)):
            projectileList[i].move()

        


    pygame.time.wait(10)
    pygame.display.update()
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:#hit the x and ends game
            pygame.quit()
            os._exit(1)
