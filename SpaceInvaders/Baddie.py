import random, pygame

baddieImage = pygame.image.load("Enemy2.png")

class Baddie(object):
    ''' Class for baddie enemy '''
    def __init__(self,startX,startY,xMovAmnt=50):
        ''' Initiates the Baddie character '''
        self.x = startX
        self.y = startY
        self.xMovAmnt = xMovAmnt
        self.image = baddieImage
        self.rect = self.image.get_rect()
        
    def getX(self):
        return self.x


    def getY(self):
        return self.y
        
    def moveChar(self):
        self.x += self.xMovAmnt
        
        
    def __str__(self):
        return "Test"

