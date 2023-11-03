import pygame
import sys
import random
import time
import math
#from turtle import delay
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

pygame.display.set_caption("TOP DOWN GAME")

clock=pygame.time.Clock()

    #+++++LINKS+++++

link_assets_base_pc="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
link_assets_base_laptop="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
link_assets_base=link_assets_base_pc
link_assets_player=link_assets_base+"\\Player.png"
link_assets_cursor=link_assets_base+"\\Aim.png"
link_assets_aimcursor=link_assets_base+"\\AimBig.png"
link_assets_bullets=link_assets_base+"\\Bullet.png"

    #+++++COLORS+++++

color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

    #+++++DISPLAY WINDOW+++++

display_width=1920
display_height=1080
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

    global bullet
    bullet=Projectile()

def get_mouse_pos():
    mouse_pos= pygame.mouse.get_pos()
    return mouse_pos

def spawner():
    display_window.blit(cursor.image,cursor.pos)   #CURSOR SPAWN
    cursor.update()
    display_window.blit(P.image,P.hitbox)          #PLAYER SPAWN
    P.update()
    display_window.blit(bullet.image,bullet.rect)  #BULLET SPAWN
    bullet.update()

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
        self.angle=math.degrees(math.atan2(self.posy-self.mouse_posy,self.posx-self.mouse_posx))
        self.image=pygame.transform.rotate(self.base_image,-self.angle)
        self.hitbox=self.image.get_rect(center=self.rect.center)
    
    def movement(self):
        self.pos+=pygame.math.Vector2(self.velocity_x,self.velocity_y)
        self.rect.center=self.pos
        self.hitbox.center=self.rect.center
  
    def update(self):
        self.input()
        self.movement()
        self.rotation()

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

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(link_assets_bullets)
        #self.image_resized = pygame.transform.scale(self.image,10)
        self.rect=self.image.get_rect()
        self.IsFired=False
        self.pos=P.pos
        self.posx=self.rect.centerx
        self.posy=self.rect.centery
        self.speed=15
    
    def fire(self,Player):
        if self.IsFired==False:
            print("FIRE")
            self.rect.center=self.pos
            self.angle=math.degrees(math.atan2(cursor.rect.centery-self.posy,cursor.rect.centerx-self.posx))
            self.IsFired=True
        
    
    def movement(self):
        if self.IsFired:
            self.velocity_x=self.speed
            self.velocity_y=-self.speed
            self.pos+=pygame.math.Vector2(self.velocity_x,self.velocity_y)
            self.posx=self.rect.centerx
            self.posy=self.rect.centery
            self.rect.center=self.pos
            print(self.posy)
            if self.posy<6 :
                self.kill()
                self.IsFired=False
                print(self.IsFired)
    
    def reset(self):
        pass

    def update(self):
        self.movement()
        
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
        if event.type == MOUSEBUTTONUP:
            if event.button==1:
                bullet.fire(P)
       
    spawner()
    pygame.display.update()
    game_fps.tick(FPS)