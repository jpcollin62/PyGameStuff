import pygame
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location,window_width,window_height):
        pygame.sprite.Sprite.__init__(self)
        image_file = pygame.image.load(image_file)
        self.image = pygame.transform.scale(image_file,(window_width,window_height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
