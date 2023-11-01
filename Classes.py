import pygame
import random
import math

from Constants import *
from Variables import score_value,P


class Aim (pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_AIMCURSOR)
        self.rect=self.image.get_rect()
        self.Fired=False
    
    def fire(self,P,T):
        if self.Fired==False:
            self.Fired=True
            self.pos = self.rect.center
            if P.ammo>0:
                if P.lives>0:
                    DISPLAY_WINDOW.fill(COLOR_YELLOW)
                    if self.rect.colliderect(T.rect):
                        T.reset_position()
                        P.score+=score_value
                
                    P.ammo-=1
                    self.Fired=False
                    #print(P.ammo)

    def update (self):
        self.rect.center=pygame.mouse.get_pos()

class Target (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LINK_ASSETS_TARGET)
        self.rect=self.image.get_rect()
        self.offset=self.image.get_height()
        self.speed=1
        self.posx=random.randint(40,DISPLAY_WIDTH-40)
        self.posy=-100
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
        self.types=["Bomb","Missile"]
        self.target_type=self.types[0]
        #print(self.pos)
    
    def reset_position(self):
        if self.target_type=="Missile":
            self.posx=random.randint(-DISPLAY_WIDTH+500,0)
        else:
            self.posx=random.randint(40,DISPLAY_WIDTH-40)
        self.posy=-100
        self.pos=(self.posx,self.posy)
        self.target_type=self.types[0]
        self.speed+=0.1   

    def shot(self):
        #self.posy+=random.randint(40,DISPLAY_HEIGHT-self.offset)
        if P.lives>0:
            if self.posy<DISPLAY_HEIGHT:
                if self.target_type=="Missile":
                    self.posx+=self.speed
                self.posy+=self.speed
                self.pos = (self.posx,self.posy)
            else:
                self.reset_position()
                P.lives-=1

    def missile_shot(self):
        self.posx=self.rect.centerx
        self.posy=self.rect.centery
        self.posy+=self.speed
        self.posx+=self.speed
        if self.posx>0 and self.posx<DISPLAY_WIDTH/2:
             self.pos=(self.posx,self.posy)
        elif self.posx<DISPLAY_WIDTH/2 and self.posx>DISPLAY_WIDTH:
            self.pos=(self.posx,-self.posy)
        self.pos=(self.posx,self.posy)
        pass

    def move(self):
        self.shot()
        #if self.pos==(self.posx,200):
            #Target_Group.add(T)
            #print(Target_Group)
        self.rect.center=self.pos

    def update(self):
        self.move()
        pass

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
        self.score=0 
        self.lives=3
        self.ammo=10

    def rotation(self):
        self.mouseposx,self.mouseposy=pygame.mouse.get_pos()
        self.angle=math.degrees(math.atan2(self.posy-self.mouseposy,self.posx-self.mouseposx))
        self.image_rotated=pygame.transform.rotate(self.image,-self.angle)
        self.rect_rotated=self.image_rotated.get_rect(center=self.rect.center)

    def update(self):
        self.rotation()