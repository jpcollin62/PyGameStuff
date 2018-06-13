import pygame, time

class Enemy(object):

    def __init__(self, xMove, yMove, startLeft, startTop, enemyList,status = "alive"):
        #loads the images and the rect
        enemyImage = pygame.image.load("Enemy2.png")
        enemyImage = pygame.transform.scale(enemyImage, (50,30))
        enemyRect = enemyImage.get_rect()

        self.image = enemyImage
        self.rect = enemyRect

        #makes it appear at the desired location
        self.rect.left = startLeft
        self.rect.top = startTop

        #saves the current live status and the current x and y move speeds
        self.status = status
        self.xMove = xMove
        self.yMove = yMove

        #remembers the beginning position and speed of the enemy
        self.startxMove = xMove
        self.startyMove = yMove
        self.setMove = 20
        self.startLeft = startLeft
        self.startTop = startTop

        #Saves the current time
        self.lastMove = (time.time())

        #appends it to the list of enemies
        enemyList.append(self)

    def movement(self, windowWidth, windowHeight):
        '''Free enemy movement'''
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

    def LRMove(self):
        self.rect.left += self.setMove


    def checkMove(self, windowWidth, windowHeight):
        if self.rect.right + self.setMove >= windowWidth-20:
            return True

        elif self.rect.left + self.setMove < 20:
            return True

        else:
            return False



    def invaderMovement(self):
        self.LRMove()
        self.lastMove = time.time()
        

    def moveDown(self):
        self.setMove = -self.setMove

        self.rect.top += 30

        

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



        
