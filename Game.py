import pygame
import sys
import random
import time
import math
#from turtle import delay
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

pygame.display.set_caption("GAME")

clock=pygame.time.Clock()


    #+++++LINKS+++++

link_assets_base="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
link_assets_player=link_assets_base+"\\Player.png"
link_assets_cursor=link_assets_base+"\\Aim.png"
link_assets_aimcursor=link_assets_base+"\\AimBig.png"

    #+++++COLORS+++++

color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

    #+++++DISPLAY WINDOW+++++

display_width=1240
display_height=720
display_window= pygame.display.set_mode((display_width,display_height))
#display_center=((display_width-(display_width/2)),(display_height-(display_height/2)))

    #+++++GAME OVER+++++
font=pygame.font.SysFont(None,30,bold=True)

    #+++++FPS+++++ 
game_fps=pygame.time.Clock()
FPS=60

    #+++++FUNCTIONS+++++
def game_init():
    pygame.mouse.set_visible(False)

    global SpawnPoints
    SpawnPoints=[(160,220),(560,340)]

    global P 
    P=Player()

    global cursor 
    cursor=HUD()



def get_mouse_pos():
    mouse_pos= pygame.mouse.get_pos()
    return mouse_pos

def spawner():
    display_window.blit(P.base_image,P.hitbox)
    P.update()
    display_window.blit(cursor.image,cursor.pos)
    cursor.update()


    #+++++CLASSES+++++
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_image=pygame.image.load(link_assets_player)
        self.image=self.base_image  
        self.pos=SpawnPoints[0]
        self.rect=self.base_image.get_rect(center=self.pos)
        self.hitbox=self.rect.copy()
        self.speed=5
    
    def input(self):
        self.velocity_x=0
        self.velocity_y=0
        pressed_keys=pygame.key.get_pressed()

        self.posx=self.rect.centerx
        self.posy=self.rect.centery
        self.offset=25
        #print(posx,posy)
        if self.posy-self.offset>0:
            if pressed_keys[K_w]:
                self.velocity_y=-self.speed
        if self.posy<display_height-self.offset:
            if pressed_keys[K_s]:
                self.velocity_y=self.speed
        if self.posx<display_width-self.offset:
            if pressed_keys[K_d]:
                self.velocity_x=self.speed
        if self.posx-self.offset>0:
            if pressed_keys[K_a]:
                self.velocity_x=-self.speed
    def rotation(self):
        
        self.mouse_posx,self.mouse_posy=get_mouse_pos()
        self.angle=math.degrees(math.atan2(self.mouse_posy,self.mouse_posx))
        self.image=pygame.transform.rotate(self.base_image,self.angle)
        self.hitbox=self.image.get_rect(center=self.rect.center)
        print(self.angle,self.hitbox.center,self.rect.center)
    
    def movement(self):
        self.pos+=pygame.math.Vector2(self.velocity_x,self.velocity_y)
        self.rect.center=self.pos
        self.hitbox.center=self.rect.center
  
    def update(self):
        self.input()
        self.movement()
        self.rotation()
        pygame.draw.rect(display_window,color_red,self.hitbox,width=2)
        pygame.draw.rect(display_window,color_black,self.rect,width=2)


class HUD (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(link_assets_cursor)
        self.rect=self.image.get_rect()
        self.pos=get_mouse_pos()
        self.IsAiming=False
    def motion(self):
        if event.type==MOUSEMOTION: 
            self.pos=get_mouse_pos()
    def aim(self,Player):
        if self.IsAiming==False:
            self.image=pygame.image.load(link_assets_aimcursor)
            Player.speed=1
            self.IsAiming=True  
        elif self.IsAiming==True:
            self.image=pygame.image.load(link_assets_cursor)
            Player.speed=5
            self.IsAiming=False 
            
    def update(self):
        self.motion()
        
game_init()
while True:
    display_window.fill(color_white)   #SET BACKGROUND

    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type==MOUSEBUTTONUP:
            if event.button==3:
                cursor.aim(P)
    spawner()
    pygame.display.update()
    game_fps.tick(FPS)