import pygame
import math

from Constants import LINK_ASSETS_ROCKET,DISPLAY_WINDOW

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_ROCKET)
        self.rect=self.image.get_rect()
        self.posx=x
        self.posy=y
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
    
    def movement(self):
        self.mouse_posx,self.mouse_posy=pygame.mouse.get_pos()
        self.angle = math.atan2(self.mouse_posy-self.posy,self.mouse_posx-self.posx)
        
        self.trajectory=math.hypot(self.mouse_posy-self.posy,self.mouse_posx-self.posx)
        self.trajectory=int(self.trajectory)

        self.dx=math.cos(self.angle)
        self.dy=math.sin(self.angle)

        #self.posx=self.mouse_posx
        #self.posy=self.mouse_posy
        if self.trajectory:
            self.trajectory-=1
            self.pos+=pygame.math.Vector2(self.dx,self.dy)
        self.rect.center=self.pos

    def update (self):
        DISPLAY_WINDOW.blit(self.image,self.rect)
        self.movement()
        



        