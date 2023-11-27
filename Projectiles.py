import pygame
import math
import random

from Constants import LINK_ASSETS_PLAYER

class Projectile(pygame.sprite.Sprite):
    def __init__(self,spawn_point):
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_PLAYER)
        self.offset=self.image.get_height()
        self.rect=self.image.get_rect()
        self.speed=5
        self.pos=spawn_point
        self.rect.center=self.pos
        self.posy=self.rect.centery
    def movement(self):
        if self.posy>0:
            self.pos+=self.speed
        else:
            self.kill()
    def update(self):
        self.movement()
