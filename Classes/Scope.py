import pygame

from Var.Constants import LINK_ASSETS_AIMCURSOR,LINK_ASSETS_REPAIR

class Aim (pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_AIMCURSOR)
        self.rect=self.image.get_rect()
        self.Fired=False
    
    #def fire(self):
    #    if self.Fired==False:
    #        self.Fired=True
    #        self.pos = self.rect.center
        
    def repair(self):
        self.image=pygame.image.load(LINK_ASSETS_REPAIR)
    
    def icon_reset(self):
        self.image=pygame.image.load(LINK_ASSETS_AIMCURSOR)

    def update (self):
        self.rect.center=pygame.mouse.get_pos()
