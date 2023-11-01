import pygame

from Target import Target

class Spawner:
    def __init__(self):
        self.group=pygame.sprite.Group()
        self.spawn_time=80

    def spawn(self):
        T = Target()
        self.group.add(T)
        
    def update(self):
        self.group.update()
        if self.spawn_time==0:
            self.spawn()
            print("aa")
            self.spawn_time=80
        self.spawn_time-=1

