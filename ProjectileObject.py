import pygame

class Projectile(object):

    def __init__(self, surface, x, y, status = "travel"): #Takes the top center of the player rectangle

        self.status = status
        self.surface = surface
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x-2.5, self.y-16, 5, 16)
        self.drawProjectile()
        

    def drawProjectile(self):
        pygame.draw.rect(self.surface, (80, 160, 255), self.rect)

    
        

    def move(self):
        
        self.rect.top += -3
        self.drawProjectile()

    
        
