import pygame, time, random, ProjectileObject

class Enemy(object):

    def __init__(self, xMove, yMove, startLeft, startTop, enemyList, surface, status = "alive"):
        #loads the images and the rect
        enemyImage = pygame.image.load("Enemy2.png")
        enemyImage = pygame.transform.scale(enemyImage, (50,30))
        enemyRect = enemyImage.get_rect()

        self.image = enemyImage
        self.rect = enemyRect

        self.surface = surface

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
        '''space invader left and right movement'''
        self.rect.left += self.setMove


    def checkMove(self, windowWidth, windowHeight):
        '''checks if the enemy will go off the screen'''
        if self.rect.right + self.setMove >= windowWidth-20:
            return True

        elif self.rect.left + self.setMove < 20:
            return True

        else:
            return False



    def invaderMovement(self):
        '''moves the space invader and saves the last time that the invader moves'''
        self.LRMove()
        self.lastMove = time.time()
        

    def moveDown(self):
        '''moves the invader down.  used after the enemy is going to hit the wall'''
        self.setMove = -self.setMove

        self.rect.top += 30

        

    def die(self):
        self.status = "dead"
    
    def appear(self, surface):
        if self.status == "alive":
            surface.blit(self.image, self.rect)

        if self.status == "dead":
            pass

    def shootChance(self):
        '''enemy has 1 in 80 chance to shoot'''
        chance = random.randint(0, 80)
        if chance == 0:
            projectile = ProjectileObject.Projectile(self.surface, self.rect.centerx, self.rect.bottom, False)
            return projectile
        else:
            return False

    def restart(self):
        '''returns the enemy to its original position'''
        self.rect.left = self.startLeft
        self.rect.top = self.startTop
        self.xMove = self.startxMove
        self.yMove = self.startyMove



        
