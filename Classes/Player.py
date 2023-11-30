import pygame
import math

from pygame.locals import *
from Var.Constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imageload=pygame.image.load(LINK_ASSETS_SPACESHIP)
        self.image=pygame.transform.scale(self.imageload,(100,100))
        self.body_image=pygame.image.load(LINK_ASSETS_SPACESHIP)
        self.image_rotated=self.image
        self.rect=self.body_image.get_rect()
        self.rect_rotated=self.rect
        self.offset=self.body_image.get_height()
        self.posx=DISPLAY_WIDTH/2
        self.posy=DISPLAY_HEIGHT-self.offset
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos  
        self.canfire=True
        self.ammo_supplies=150
        self.maxammo=10
        self.score=0
        self.ammo=self.maxammo
        self.IsReloading=False

    def rotation(self):
        self.mouseposx,self.mouseposy=pygame.mouse.get_pos()
        self.angle=math.degrees(math.atan2(self.posy-self.mouseposy,self.posx-self.mouseposx))
        self.image_rotated=pygame.transform.rotate(self.image,-self.angle+90)
        self.rect_rotated=self.image_rotated.get_rect(center=self.rect.center)

    def reload(self):
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_r]:
            if self.ammo_supplies>1:
                if self.ammo<self.maxammo:
                    self.IsReloading=True
                else:
                    self.IsReloading=False 
                if self.IsReloading:
                    self.ammo_supplies-=0.05
                    self.ammo+=0.05
                    
            else:
                print("NO AMMO!")

    def update(self):
        #DISPLAY_WINDOW.blit(self.body_image,self.pos)
        #self.rotation()
        pass