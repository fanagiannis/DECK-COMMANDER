import pygame
import math
import random

from Constants import LINK_ASSETS_PLAYER,COLOR_WHITE,DISPLAY_WINDOW
from Variables import playerpositionx,playerpositiony

class Projectile(pygame.sprite.Sprite):
    def __init__(self,spawn_point):
        super().__init__()
        self.width=6
        self.height=9
        self.size=(self.width,self.height)
        self.body=pygame.Surface(self.size)
        self.body.fill(COLOR_WHITE)
        self.rect=self.body.get_rect()
        self.speed=5
        self.posx=playerpositionx
        self.posy=playerpositiony
        self.pos=(self.posx,self.posy)

        mousex,mousey=pygame.mouse.get_pos()
        self.angle= math.degrees(math.atan2(-(mousex-self.posx),(mousey-self.posy)))
        self.body = pygame.transform.rotate(self.body, self.angle)

    def draw(self):
        self.rect=self.body.get_rect(center=self.pos)
        DISPLAY_WINDOW.blit(self.body,self.rect)
        pass

    def update(self):
        self.posx+=self.speed
        self.posy+=self.speed
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
