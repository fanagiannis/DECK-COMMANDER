import pygame
import sys
import random
import math
from pygame.locals import *
from pygame.sprite import *

pygame.init()

pygame.display.set_caption("GAME V0.0")

game_clock=pygame.time.Clock()
FPS=60

    #+++++DISPLAY+++++

display_width=640
display_height=360
display_window=pygame.display.set_mode((display_width,display_height))

    #+++++LINKS+++++

link_assets_base_pc="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
link_assets_base_laptop="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
link_assets_base=link_assets_base_laptop
link_assets_player=link_assets_base+"\\Player.png"
link_assets_cursor=link_assets_base+"\\Aim.png"
link_assets_aimcursor=link_assets_base+"\\AimBig.png"
link_assets_bullets=link_assets_base+"\\Bullet.png"
link_assets_target=link_assets_base+"\\Enemy.png"

    #+++++COLORS+++++

color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)
color_yellow=pygame.Color(255,255,0)


class Aim(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image=pygame.image.load(link_assets_aimcursor)
        self.rect=self.image.get_rect()
        self.Fired=False
    
    def fire(self):
        if self.Fired==False:
            self.Fired=True
            self.pos = self.rect.center
            #print(self.pos)
            print("1 ",self.Fired)
            print("BANG")
            screen_effect(color_yellow)
            if self.rect.colliderect(t.rect):
                print("HIT")
            self.Fired=False
            print("2 ",self.Fired)

           

    def update (self):
        #self.fire()
        self.rect.center=get_mousepos()
    
class Target (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(link_assets_target)
        self.rect=self.image.get_rect()
    
    def get_random_pos(self):
        self.posx=random.randint(40,display_width)
        self.posy=random.randint(40,display_height)
        self.pos=(self.posx,self.posy)

    def update(self):
        self.get_random_pos()
        self.rect.center=self.pos
        print(self.pos)
        #self.rect.center=(self.posx,self.posy)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(link_assets_player)
        self.image_rotated=self.image
        self.rect=self.image.get_rect()
        self.rect_rotated=self.rect
        self.posx=display_width/2
        self.posy=display_height-30
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
        

    def rotation(self):
        self.mouseposx,self.mouseposy=get_mousepos()
        self.angle=math.degrees(math.atan2(self.posy-self.mouseposy,self.posx-self.mouseposx))
        self.image_rotated=pygame.transform.rotate(self.image,-self.angle)
        self.rect_rotated=self.image_rotated.get_rect(center=self.rect.center)
        print(self.angle)
    
    def update(self):
        self.rotation()
        pass

#+++++FUNSTIONS++++++
def get_mousepos():
    return pygame.mouse.get_pos()

def mouse_pos_check():
    print(get_mousepos())

def screen_effect(color):
    display_window.fill(color)

def game_init():
    pygame.mouse.set_visible(False)

    global ads 
    ads=Aim()

    global t
    t=Target() 

    global P
    P=Player()

def spawner():
    display_window.blit(t.image,t.rect) #Target Spawn
    display_window.blit(ads.image,ads.rect) #Aim Spawn
    display_window.blit(P.image_rotated,P.rect_rotated)
    ads.update()
    P.update()

def eventhandler():
    if event.type==QUIT :
            pygame.quit()
            sys.exit(0)
    if event.type == MOUSEBUTTONUP:
        if event.button == 1:       #LEFT CLICK
            ads.fire()
            t.update()

game_init()

while True:

    display_window.fill(color_white)
    
    for event in pygame.event.get():
        eventhandler()

    spawner()
    pygame.display.update()
    game_clock.tick(FPS)