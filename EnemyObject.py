import pygame
'''
enemyImage = pygame.image.load("robotEnemy.png")
enemyImage = pygame.transform.scale(enemyImage, (100,100))
enemyRect = enemyImage.get_rect()
'''

class Enemy(object):

    def __init__(self, xMove, yMove, startLeft, startTop, status = "alive"):

        enemyImage = pygame.image.load("robotEnemy.png")
        enemyImage = pygame.transform.scale(enemyImage, (100,100))
        enemyRect = enemyImage.get_rect()

        self.image = enemyImage
        self.rect = enemyRect
        
        self.status = status
        self.xMove = xMove
        self.yMove = yMove

        self.startxMove = xMove
        self.startyMove = yMove
        self.startLeft = startLeft
        self.startTop = startTop

    def movement(self, windowWidth, windowHeight):
        if self.rect.right >= windowWidth:
            self.xMove = -self.xMove
        if self.rect.left <= 0:
            self.xMove = -self.xMove

        if self.rect.bottom >= windowHeight:
            self.yMove = -self.yMove
        if self.rect.top <= 0:
            self.yMove = -self.yMove

        self.rect.left += self.xMove
        self.rect.top += self.yMove
            

    def die(self):
        self.status = "dead"
    
    def appear(self, surface):
        if self.status == "alive":
            surface.blit(self.image, self.rect)

        if self.status == "dead":
            pass

    def restart(self):
        self.rect.left = self.startLeft
        self.rect.top = self.startTop
        self.xMove = self.startxMove
        self.yMove = self.startyMove



        
