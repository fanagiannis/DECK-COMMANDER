import pygame
import sys

from pygame.locals import *
from Testing.Projectiles import Projectile

class Spawner_Projectile():
    def __init__(self):
        self.group=pygame.sprite.Group()
        
    def spawn(self):
        Rocket=Projectile()
        self.group.add(Rocket)
    
    def update(self):
        self.group.update()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP:
                if event.button==1:
                    self.update()

