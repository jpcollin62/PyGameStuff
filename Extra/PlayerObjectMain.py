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
    
    surface.blit(player.image, player.rect)
    pygame.display.update()

    time.sleep(0.02)

    if counter >= 5:
        pygame.quit()
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)
