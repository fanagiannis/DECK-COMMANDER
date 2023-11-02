import pygame

from Constants import LINK_ASSETS_ROCKET

class Spawner_Projectile():
    def __init__(self):
        self.image=pygame.image.load(LINK_ASSETS_ROCKET)
        self.group=pygame.sprite.Group()
        
    def spawn(self):
        Rocket=Projectile()
        self.group.add(Rocket)
    
    def movement(self):

    
    def update(self):
        self.group.update()
