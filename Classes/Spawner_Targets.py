import pygame

from Classes.Target import Target

class Spawner():
    def __init__(self,time):
        self.group=pygame.sprite.Group()
        self.time_set=time
        self.spawn_time=self.time_set

    def spawn(self):
        T = Target()
        self.group.add(T)
    
    def reset_timer(self):
        self.spawn_time=self.time_set
        
    def update(self):
        self.group.update()
        if self.spawn_time==0:
            self.spawn()
            self.reset_timer()
        self.spawn_time-=1

