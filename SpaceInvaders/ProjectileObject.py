import pygame, time

class Projectile(object):

    def __init__(self, surface, x, y, playerShot = True): #Takes the top center of the player rectangle

        self.surface = surface
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x-2.5, self.y-16, 5, 16)
        if playerShot == True:
            self.drawProjectile()

        else:
            self.drawEnemyProjectile()

        
        

    def drawProjectile(self):
        pygame.draw.rect(self.surface, (80, 160, 255), self.rect)

    def drawEnemyProjectile(self):
        pygame.draw.rect(self.surface, (250, 100, 100), self.rect)

    
        

    def move(self):
        
        self.rect.top += -15
        self.drawProjectile()

    def enemyBulletMove(self):

        self.rect.top += 8
        self.drawEnemyProjectile()

    
    def checkHit(self, enemyList, projectileList):
        deadEnemies = []
        if len(enemyList) > 0:
            for i in range (len(enemyList)):
                if self.rect.colliderect(enemyList[i].rect):
                    enemyList.remove(enemyList[i])
                    return True

        return False

    def killBullet(self, projectileList):
        projectileList.remove(self)
        shotKill = time.time()
        return shotKill
                
