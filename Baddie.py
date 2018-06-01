import random, pygame

baddieImage = pygame.image.load("Enemy2.png")

class Baddie:
    ''' Class for baddie enemy '''
    def __init__(self,left):
        ''' Initiates the Baddie character '''
        baddieRect = baddieImage.get_rect()
        self.image = baddieImage
        self.rect = baddieRect
        self.rect.left = left
        
        
    def __str__(self):
        return "Test"

