import pygame
import math
import random

from Var.Constants import LINK_ASSETS_PLAYER,COLOR_RED,COLOR_GREEN,DISPLAY_WINDOW
from Var.Variables import P,P2,Target_spawn

class Projectile(pygame.sprite.Sprite):
    def __init__(self,spawn_point,color):
        super().__init__()
        self.width=5
        self.height=5
        self.size=(self.width,self.height)
        self.body=pygame.Surface(self.size)
        self.body.fill(color)
        if(color==COLOR_RED):
            self.parentID=1
        elif(color==COLOR_GREEN):
            self.parentID=2
        self.rect=self.body.get_rect()
        self.speed=30
        self.posx,self.posy=spawn_point
        self.pos=(self.posx,self.posy)
       
       # mousex,mousey=pygame.mouse.get_pos()
       # self.direction=(self.posx-mousex,self.posy-mousey)
       # distance=math.hypot(*self.direction)
       # self.direction=(self.direction[0]/distance,self.direction[1]/distance)

    def draw(self):
        self.rect=self.body.get_rect(center=self.pos)
        DISPLAY_WINDOW.blit(self.body,self.rect)

    def update(self):
        self.posy-=self.speed
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
        if self.posy<-10:
            self.kill()
        if pygame.sprite.spritecollide(self,Target_spawn.group,True):
            self.kill()
            if(self.parentID==1):
                P.score+=P.scoreinc
            if(self.parentID==2):
                P2.score+=P2.scoreinc
