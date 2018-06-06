import pygame, time
pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)
pygame.display.set_caption("Moving Spaceship")

space = pygame.image.load("spaceship.jpg")
spaceRect = space.get_rect()

spaceRect.topleft = (100,100)

X_MOVE_AMT = 5
counter = 0

while True:
    surface.fill ((255, 255, 255))

    spaceRect.left += X_MOVE_AMT

    if spaceRect.right >= WINDOW_WIDTH:

        counter += 1
        X_MOVE_AMT = - X_MOVE_AMT
        
    if spaceRect.left <= 0:

        counter += 1
        X_MOVE_AMT = - X_MOVE_AMT
        
    surface.blit (space, spaceRect)
    pygame.display.update()

    if counter == 10:
        pygame.quit ()
        os._exit (1)

    time.sleep (0.02)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit ()
            os._exit(1)
