import pygame, ProjectileObject

class Player(object):

    def __init__(self):

        playerImage = pygame.image.load("Player.png")
        playerImage = pygame.transform.scale(playerImage, (50,50))
        playerRect = playerImage.get_rect()
        self.image = playerImage
        self.rect = playerRect

        
    def movement(self, windowWidth, windowHeight):#decide between the enemy or player method of moving (self.xMove?)
        '''how the player moves'''
        x = 0
        y = 0
        

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top >= 0:
            y = -5
        if pressed[pygame.K_DOWN] and self.rect.bottom <= windowHeight:
            y = 5
        if pressed[pygame.K_LEFT] and self.rect.left >= 0:
            x = -5
        if pressed[pygame.K_RIGHT] and self.rect.right <= windowWidth:
            x = 5

        self.rect.left += x
        self.rect.top += y

    def LRMovement(self, windowWidth, windowHeight):#decide between the enemy or player method of moving (self.xMove?)
        '''how the player moves'''
        x = 0
        

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.left >= 0:
            x = -5
        if pressed[pygame.K_RIGHT] and self.rect.right <= windowWidth:
            x = 5

        self.rect.left += x

    def collisionCheck (self, obj):
        if self.rect.colliderect(obj.rect):
            return True

        else:
            return False

    def shoot(self, surface, projectileList):
        if len(projectileList) == 0:#prints the first projectile on the screen
            projectile = ProjectileObject.Projectile(surface, self.rect.centerx, self.rect.top)
            return projectile
        return False
