import pygame
import random 

from Target import Target

class Spawner:
    def __init__(self,time):
        self.group=pygame.sprite.Group
        self.spawn_time=time
        pass

    def spawn(self,Target):
        T = Target()
        self.group.add(T)

    def update(self):
        self.group.update()
        if self.spawn_time==0:
            self.spawn()
            self.spawn_time-=1

