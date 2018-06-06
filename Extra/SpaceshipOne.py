import pygame, time

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)

pygame.display.set_caption("Moving Baddie")

space = pygame.image.load("baddie.png")
space = pygame.transform.scale(space, (200,200))
spaceRect = space.get_rect()

spaceRect.topleft = (0, 0)

X_MOVE_AMT = 5 #Number of pixels the spaceship will move at one time
Y_MOVE_AMT = 5 #up down movement

#Game loop
counter = 0
while True:
    surface.fill((255,255,255))

    spaceRect.left += X_MOVE_AMT
    spaceRect.top += Y_MOVE_AMT

    if spaceRect.right >= WINDOW_WIDTH:
        X_MOVE_AMT = -X_MOVE_AMT
        counter += 1
    if spaceRect.left <= 0:
        counter += 1
        X_MOVE_AMT = -X_MOVE_AMT

    if spaceRect.top <= 0:
        Y_MOVE_AMT = -Y_MOVE_AMT

    if spaceRect.bottom >= WINDOW_HEIGHT:
        Y_MOVE_AMT = -Y_MOVE_AMT

    surface.blit(space, spaceRect)
    pygame.display.update()

    time.sleep(0.02)

    if counter >= 5:
        pygame.quit()
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)
