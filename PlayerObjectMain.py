import pygame, time, PlayerObject

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)
pygame.display.set_caption("Player Test")

player = PlayerObject.Player()
player.rect.left = 450
player.rect.bottom = 600

counter = 0
while True:
    surface.fill((255,255,255))

    x,y = player.movement()
    
    player.rect.left += x
    player.rect.top +=y

    '''if playerRect.right >= WINDOW_WIDTH:
        X_MOVE_AMT = -X_MOVE_AMT
        counter += 1
    if playerRect.left <= 0:
        counter += 1
        X_MOVE_AMT = -X_MOVE_AMT

    if playerRect.top <= 0:
        Y_MOVE_AMT = -Y_MOVE_AMT

    if playerRect.bottom >= WINDOW_HEIGHT:
        Y_MOVE_AMT = -Y_MOVE_AMT'''

    
    surface.blit(player.image, player.rect)
    pygame.display.update()

    time.sleep(0.02)

    if counter >= 5:
        pygame.quit()
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)
