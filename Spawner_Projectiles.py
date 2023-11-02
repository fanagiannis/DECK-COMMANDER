import pygame

class Spawner_Projectile():
    def __init__(self):
        self.group=pygame.sprite.Group()
        
    def spawn(self):
        Rocket=Projectile()
        self.group.add(Rocket)
    
    def movement(self):

    
    def update(self):
        self.group.update()
