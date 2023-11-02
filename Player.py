import pygame
import math

from pygame.locals import *
from Constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_PLAYER)
        self.image_rotated=self.image
        self.rect=self.image.get_rect()
        self.rect_rotated=self.rect
        self.offset=self.image.get_height()/2
        self.posx=DISPLAY_WIDTH/2
        self.posy=DISPLAY_HEIGHT-self.offset
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos  
        self.canfire=True
        self.maxammo=10
        self.score=0
        self.ammo=self.maxammo

    def rotation(self):
        self.mouseposx,self.mouseposy=pygame.mouse.get_pos()
        self.angle=math.degrees(math.atan2(self.posy-self.mouseposy,self.posx-self.mouseposx))
        self.image_rotated=pygame.transform.rotate(self.image,-self.angle)
        self.rect_rotated=self.image_rotated.get_rect(center=self.rect.center)

    def reload(self):
        pressed_key=pygame.key.get_pressed()
        self.timer=1000
        self.dtimer=0.1
        if pressed_key[K_r]:
            if self.ammo<self.maxammo:
                if self.timer==0:
                    self.ammo+=1
                  
                    print("reloading!")
                self.timer-=self.dtimer
                if self.ammo==self.maxammo:
                    self.timer=1000
               
            

                


    def update(self):
        self.rotation()