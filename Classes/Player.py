import pygame
import math

from pygame.locals import *
from Var.Constants import *
from assets.Sound_effects import reload_sound


class Player(pygame.sprite.Sprite):
    def __init__(self,playernumber):
        super().__init__()
        if (playernumber==1):
            self.image=pygame.image.load(LINK_ASSETS_SPACESHIP)
        elif():
            self.image=pygame.image.load(LINK_ASSETS_SPACESHIP)
        #self.image=pygame.transform.scale(self.imageload,(100,100))
        self.body_image=pygame.image.load(LINK_ASSETS_SPACESHIP)
        self.image_rotated=self.image
        self.rect=self.body_image.get_rect()
        self.rect_rotated=self.rect
        self.offset=self.body_image.get_height()-30
        self.posx=DISPLAY_WIDTH/2
        self.posy=DISPLAY_HEIGHT-self.offset
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos  
        self.canfire=True
        self.ammo_supplies=15000
        self.maxammo=5
        self.score=0
        self.scoreinc=100
        self.ammo=self.maxammo
        self.IsReloading=False
        self.speed=10
        self.playernumber=playernumber

    def reset(self):
        self.posx=DISPLAY_WIDTH/2
        self.posy=DISPLAY_HEIGHT-self.offset
        self.pos=(self.posx,self.posy)
        self.ammo_supplies=15000
        self.maxammo=5
        self.score=0
        self.scoreinc=100
        self.ammo=self.maxammo
        self.IsReloading=False
        self.speed=10

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
                    self.ammo=5
                    reload_sound.play() 
            else:
                print("NO AMMO!")

    def movement(self):
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_d]:
            if self.posx<DISPLAY_WIDTH-self.offset:
                self.posx+=self.speed
        if pressed_key[K_a]:
            if self.posx>(self.offset/2-10):
                self.posx-=self.speed
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos                

    def update(self):
        self.movement()
        #DISPLAY_WINDOW.blit(self.body_image,self.pos)
        #self.rotation()
        pass