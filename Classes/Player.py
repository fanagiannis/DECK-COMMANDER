import pygame
import math

from pygame.locals import *
from Var.Constants import *
from assets.Sound_effects import reload_sound


class Player(pygame.sprite.Sprite):
    def __init__(self,playerID):
        super().__init__()
        try:
            self.playerID=playerID
            if (self.playerID==1):
                self.image=pygame.image.load(LINK_ASSETS_SPACESHIP)
                self.body_image=pygame.image.load(LINK_ASSETS_SPACESHIP)
                self.posx=DISPLAY_WIDTH/2 + 50
            elif(self.playerID==2):
                self.image=pygame.image.load(LINK_ASSETS_SPACESHIP2)
                self.body_image=pygame.image.load(LINK_ASSETS_SPACESHIP2)
                self.posx=DISPLAY_WIDTH/2 - 50
            self.image=self.image.convert_alpha()
            self.body_image=self.body_image.convert_alpha()
        
        except pygame.error as e:
            print(f"Error in object iniialization : {e}")
        #self.image=pygame.transform.scale(self.imageload,(100,100))
        
        self.image_rotated=self.image
        self.rect=self.body_image.get_rect()
        self.rect_rotated=self.rect
        self.offset=self.body_image.get_height()-30
        
        self.posy=DISPLAY_HEIGHT-self.offset
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos  
        self.canfire=True
        self.ammo_supplies=15000
        self.maxammo=5
        self.score=0
        self.scoreinc=150
        self.ammo=self.maxammo
        self.IsReloading=False
        self.speed=10

    def reset(self):
        self.posx=DISPLAY_WIDTH/2
        self.posy=DISPLAY_HEIGHT-self.offset
        self.pos=(self.posx,self.posy)
        self.ammo_supplies=15000
        self.maxammo=5
        self.score=0
        self.scoreinc=150
        self.ammo=self.maxammo
        self.IsReloading=False
        self.speed=10

   # def rotation(self):
   #     self.mouseposx,self.mouseposy=pygame.mouse.get_pos()
   #     self.angle=math.degrees(math.atan2(self.posy-self.mouseposy,self.posx-self.mouseposx)) //CUT
   #     self.image_rotated=pygame.transform.rotate(self.image,-self.angle+90)
  #     self.rect_rotated=self.image_rotated.get_rect(center=self.rect.center)

    def reload(self):
        pressed_key=pygame.key.get_pressed()
        if(self.playerID==1):
            if pressed_key[K_s]:
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
        elif(self.playerID==2):
            if pressed_key[K_DOWN]:
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
        if(self.playerID==1):
            pressed_key=pygame.key.get_pressed()
            if pressed_key[K_d]:
                if self.posx<DISPLAY_WIDTH-self.offset:
                    self.posx+=self.speed
            if pressed_key[K_a]:
                if self.posx>(self.offset/2-10):
                    self.posx-=self.speed
        elif(self.playerID==2):
            pressed_key=pygame.key.get_pressed()
            if pressed_key[pygame.K_RIGHT]:
                if self.posx<DISPLAY_WIDTH-self.offset:
                    self.posx+=self.speed
            if pressed_key[pygame.K_LEFT]:
                if self.posx>(self.offset/2-10):
                    self.posx-=self.speed
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos                

    def update(self):
        self.movement()
        pass
    