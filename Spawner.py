import pygame
import random 

from Target import Target

class Spawner:
    def __init__(self):
        self.group=pygame.sprite.Group()
        self.spawn_time=80
        pass

    def spawn(self):
        T = Target()
        self.group.add(T)

    def update(self):
        self.group.update(self)
        if self.spawn_time==0:
            self.spawn()
            self.spawn_time-=1

