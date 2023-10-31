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

    #+++++FONT+++++
font=pygame.font.SysFont(None,30,bold=True)

class Aim(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image=pygame.image.load(link_assets_aimcursor)
        self.rect=self.image.get_rect()
        self.Fired=False
    
    def fire(self,Player):
        if self.Fired==False:
            self.Fired=True
            self.pos = self.rect.center
            #print(self.pos)
            print("1 ",self.Fired)
            print("BANG")
            screen_effect(color_yellow)
            if self.rect.colliderect(t.rect):
                P.score+=1 
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
        self.offset=self.image.get_height()
    
    def get_random_pos(self):
        self.posx=random.randint(40,display_width)
        self.posy=random.randint(40,display_height-self.offset)
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
        self.offset=self.image.get_height()/2
        self.posx=display_width/2
        self.posy=display_height-self.offset
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos    
        self.score=0 


    
    def rotation(self):
        self.mouseposx,self.mouseposy=get_mousepos()
        self.angle=math.degrees(math.atan2(self.posy-self.mouseposy,self.posx-self.mouseposx))
        self.image_rotated=pygame.transform.rotate(self.image,-self.angle)
        self.rect_rotated=self.image_rotated.get_rect(center=self.rect.center)

    def update(self):
        self.rotation()

#+++++FUNSTIONS++++++
def get_mousepos():
    return pygame.mouse.get_pos()

def mouse_pos_check():
    print(get_mousepos())

def screen_effect(color):
    display_window.fill(color)

def message(text,text_color,text_pos):
    display_text=font.render(text,True,text_color)
    display_window.blit(display_text,text_pos)
    pass 

def game_init():
    pygame.mouse.set_visible(False)

    global ads 
    ads=Aim()

    global t
    t=Target() 

    global P
    P=Player()

    global score_message_template_pos
    score_message_template_pos=(30,display_height-50)
   

def spawner():
    display_window.blit(t.image,t.rect) #Target Spawn
    display_window.blit(ads.image,ads.rect) #Aim Spawn
    display_window.blit(P.image_rotated,P.rect_rotated) #PlayerSpawn

    score_message_text= "Score : "+ str(P.score)
    message(score_message_text,color_black,score_message_template_pos)
    
    ads.update()
    P.update()

def eventhandler():
    if event.type==QUIT :
            pygame.quit()
            sys.exit(0)
    if event.type == MOUSEBUTTONUP:
        if event.button == 1:       #LEFT CLICK
            ads.fire(P)
            t.update()

game_init()

while True:

    display_window.fill(color_white)
    
    for event in pygame.event.get():
        eventhandler()

    spawner()
    pygame.display.update()
    game_clock.tick(FPS)