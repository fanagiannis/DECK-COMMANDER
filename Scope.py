import pygame

from Constants import LINK_ASSETS_AIMCURSOR
from Spawner import T

class Aim (pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_AIMCURSOR)
        self.rect=self.image.get_rect()
        self.Fired=False
    
    def fire(self):
        if self.Fired==False:
            self.Fired=True
            self.pos = self.rect.center

    def update (self):
        self.rect.center=pygame.mouse.get_pos()
