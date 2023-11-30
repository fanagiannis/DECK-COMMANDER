import pygame
from random import randrange
screen_height = 720
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface((100,50))
        self.image.fill((243,0,200))
        self.x = 0
        self.y = randrange(screen_height)
        self.speed = 30
    


