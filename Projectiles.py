import pygame

from Constants import LINK_ASSETS_ROCKET

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_ROCKET)
        self.rect=self.image.get_rect()
    
    def movement():

        