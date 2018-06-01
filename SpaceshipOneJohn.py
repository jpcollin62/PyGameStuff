import pygame, time, Baddie

pygame.init()

window_width = 1600
window_height = 800

surface = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Moving Spaceship")

x_move_amt = 5

#myBaddies[x] = Baddie.Baddie()
myBaddies = []

while True:
    
    surface.fill((255,255,255))
    for x in range (0, 8):
        pos = x*200
        myBaddies.append(Baddie.Baddie(pos))
        #
    for x in range (len(myBaddies)):
    
        surface.blit(myBaddies[x].image, myBaddies[x].rect)  

    myBaddies[0].rect.left += x_move_amt
    '''
    if myBaddies[x].rect.right >= window_width:
        x_move_amt = -x_move_amt

    if myBaddies[x].rect.left <= 0:
        x_move_amt = -x_move_amt
    
    surface.blit(myBaddies[x].image, myBaddies[x].rect)
    '''
    pygame.display.update()
    
    time.sleep(0.02)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)
