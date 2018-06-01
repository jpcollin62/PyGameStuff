import pygame

class Item(object):

    def __init__(self, left, top,status = "uncollected"):

        itemImage = pygame.image.load("static.png")
        itemImage = pygame.transform.scale(itemImage, (30,30))
        itemRect = itemImage.get_rect()

        self.image = itemImage
        self.rect = itemRect

        self.left = left
        self.top = top
        self.status = status

    def collectCheck(self, player):
        '''Checks if the item is being touched by the player'''
        collisionStatus = False
        if player.rect.colliderect(self.rect):
            self.status = "collected"
            collisionStatus = True

            return collisionStatus
            

    def appear(self, surface):
        if self.status == "uncollected":
            surface.blit(self.image, self.rect)

    def restart(self):
        self.status = "uncollected"
            
