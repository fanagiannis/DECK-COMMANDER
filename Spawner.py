import pygame
import random 

from Target import Target

class Spawner:
    def __init__(self):
        self.group=pygame.sprite.Group
        self.spawn_time=random.randrange(30,120)
        pass

    def spawn(self,Target):
        taget_new = Target()
        self.group.add(Target_new)

