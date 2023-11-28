import pygame
import math
import random

from Constants import LINK_ASSETS_PLAYER,COLOR_RED,DISPLAY_WINDOW
from Variables import playerpositionx,playerpositiony

class Projectile(pygame.sprite.Sprite):
    def __init__(self,spawn_point):
        super().__init__()
        self.width=5
        self.height=5
        self.size=(self.width,self.height)
        self.body=pygame.Surface(self.size)
        self.body.fill(COLOR_RED)
        self.rect=self.body.get_rect()
        self.speed=15
        self.posx=playerpositionx
        self.posy=playerpositiony
        self.pos=(self.posx,self.posy)

        mousex,mousey=pygame.mouse.get_pos()
       # self.angle= math.degrees(math.atan2((self.posy-mousey),(self.posx-mousex)))
       # self.body = pygame.transform.rotate(self.body, -self.angle)
        self.direction=(self.posx-mousex,self.posy-mousey)
        distance=math.hypot(*self.direction)
        self.direction=(self.direction[0]/distance,self.direction[1]/distance)

    def draw(self):
        self.rect=self.body.get_rect(center=self.pos)
        DISPLAY_WINDOW.blit(self.body,self.rect)
        pass

    def update(self):
        self.posx-=self.speed*self.direction[0]
        self.posy-=self.speed*self.direction[1]
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
