import pygame
import math
import random

from Assets.Sound_effects import explosion_sound

from Var.Constants import LINK_ASSETS_PLAYER,COLOR_RED,COLOR_GREEN,DISPLAY_WINDOW,LINK_ASSETS_TARGETEXPLOSION
from Var.Variables import P,P2,Target_spawn


class Projectile(pygame.sprite.Sprite):
    def __init__(self,spawn_point,color):
        super().__init__()
        try:
            self.width=5
            self.height=5
            self.image_destroyed = pygame.image.load(LINK_ASSETS_TARGETEXPLOSION)
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
            mousex,mousey=pygame.mouse.get_pos()
            self.direction=(self.posx-mousex,self.posy-mousey)
            distance=math.hypot(*self.direction)
            self.direction=(self.direction[0]/distance,self.direction[1]/distance)
        except pygame.error as e:
            print(f"Error in object iniialization : {e}")

    def draw(self):
        self.rect=self.body.get_rect(center=self.pos)
        DISPLAY_WINDOW.blit(self.body,self.rect)

    def update(self):
        self.posy-=self.speed
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
        collision=pygame.sprite.spritecollide(self,Target_spawn.group,True)
        if self.posy<-10:
            self.kill()
        if collision:
           # for target in Target_spawn.group:
           #     hitpos_x=self.rect.x - target.rect.x
           #     hitpos_y=self.rect.y - target.rect.y
           # DISPLAY_WINDOW.blit(pygame.surface.Surface(LINK_ASSETS_TARGETEXPLOSION),self.rect)
            explosion_sound.play()
            self.kill()
            if(self.parentID==1):
                P.score+=P.scoreinc
            if(self.parentID==2):
                P2.score+=P2.scoreinc
            
