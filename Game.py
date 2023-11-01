import pygame
import sys
import random
import math
from pygame.locals import *
from pygame.sprite import *

pygame.init()

pygame.display.set_caption("GAME V0.0")

GAME_CLOCK=pygame.time.Clock()
FPS=60

    #+++++DISPLAY+++++

DISPLAY_WIDTH=1240
DISPLAY_HEIGHT=720
DISPLAY_WINDOW=pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

    #+++++LINKS+++++

LINK_ASSETS_BASE_PC="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
LINK_ASSETS_BASE_LAPTOP="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
LINK_ASSETS_BASE=LINK_ASSETS_BASE_PC
LINK_ASSETS_PLAYER=LINK_ASSETS_BASE+"\\Player.png"
LINK_ASSETS_CURSOR=LINK_ASSETS_BASE+"\\Aim.png"
LINK_ASSETS_AIMCURSOR=LINK_ASSETS_BASE+"\\AimBig.png"
LINK_ASSETS_BULLETS=LINK_ASSETS_BASE+"\\Bullet.png"
LINK_ASSETS_TARGET=LINK_ASSETS_BASE+"\\Enemy.png"

    #+++++COLORS+++++

COLOR_BLACK=pygame.Color(0,0,0)
COLOR_WHITE=pygame.Color(255,255,255)
COLOR_GREY=pygame.Color(128,128,128)
COLOR_RED=pygame.Color(255,0,0)
COLOR_YELLOW=pygame.Color(255,255,0)

    #+++++FONT+++++
FONT=pygame.font.SysFont(None,30,bold=True)

class Aim(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_AIMCURSOR)
        self.rect=self.image.get_rect()
        self.Fired=False
    
    def fire(self,Player):
        if self.Fired==False:
            self.Fired=True
            self.pos = self.rect.center
            if P.ammo>0:
                if P.lives>0:
                    screen_effect(COLOR_YELLOW)
                    if self.rect.colliderect(T.rect):
                        T.reset_position()
                        P.score+=score_value
                
                    P.ammo-=1
                    self.Fired=False
                    #print(P.ammo)

    def update (self):
        #self.fire()
        self.rect.center=get_mousepos()
    
class Target ():
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
        #print(self.pos)
    
    def reset_position(self):
        self.posx=random.randint(40,DISPLAY_WIDTH-40)
        self.posy=-100
        self.pos=(self.posx,self.posy)
        self.speed+=1   

    def gravity(self):
        #self.posy+=random.randint(40,DISPLAY_HEIGHT-self.offset)
        if P.lives>0:
            if self.posy<DISPLAY_HEIGHT:
                self.posy+=self.speed
                self.pos = (self.posx,self.posy)
            else:
                self.reset_position()
                P.lives-=1
                  
    def move(self):
       # self.posx=self.rect.centerx
       # self.posy=self.rect.centery
       # self.final_posx=random.randint(100,DISPLAY_WIDTH)
       # self.final_posy=-100
        #self.angle=math.degrees(math.atan2(self.posy-self.final_posx,self.posx-self.final_posy))

        #self.posx+= math.cos(self.angle)*self.speed
        #self.posy+= math.sin(self.angle)*self.speed
        #self.pos=(self.posx,self.posy)

        self.gravity()
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
        self.mouseposx,self.mouseposy=get_mousepos()
        self.angle=math.degrees(math.atan2(self.posy-self.mouseposy,self.posx-self.mouseposx))
        self.image_rotated=pygame.transform.rotate(self.image,-self.angle)
        self.rect_rotated=self.image_rotated.get_rect(center=self.rect.center)

    def update(self):
        self.rotation()

#+++++FUNCTIONS++++++
def get_mousepos():
    return pygame.mouse.get_pos()

def mouse_pos_check():
    print(get_mousepos())

def screen_effect(color):
    DISPLAY_WINDOW.fill(color)

def message(text,text_color,text_pos):
    display_text=FONT.render(text,True,text_color)
    DISPLAY_WINDOW.blit(display_text,text_pos)
    pass 

def game_init():
    pygame.mouse.set_visible(False)

    global ADS 
    ADS=Aim()

    global T
    T=Target() 

    global P
    P=Player()

    global score_message_pos,lives_message_pos,game_over_message_pos,ammo_message_pos, ammo_no_message_pos
    score_message_pos=(30,DISPLAY_HEIGHT-50)
    lives_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-50)
    game_over_message_pos=(DISPLAY_WIDTH/2-75,DISPLAY_HEIGHT/2-75)
    ammo_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-100)
    ammo_no_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-150)

    global score_value
    score_value=100
 
def spawner():
    score_live="%06d" % P.score
    ammo_live="%02d" % P.ammo
    score_message_text = "Score : "+ score_live #ADD ZEROES BEFORE SCORE
    lives_message_text = "Lives : "+ str(P.lives)
    game_over_message_text = "GAME OVER ! "
    ammo_message_text = "Ammo : " + ammo_live
    ammo_no_message_text = "OUT OF AMMO! "

    if P.lives>0:
        DISPLAY_WINDOW.blit(T.image,T.rect) #Target Spawn
    else:
        message(game_over_message_text,COLOR_BLACK,game_over_message_pos)
    DISPLAY_WINDOW.blit(ADS.image,ADS.rect) #Aim Spawn
    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PlayerSpawn

    message(score_message_text,COLOR_BLACK,score_message_pos)
    message(lives_message_text,COLOR_BLACK,lives_message_pos)
    message(ammo_message_text,COLOR_BLACK,ammo_message_pos)
    if P.ammo<=0:
        message(ammo_no_message_text,COLOR_BLACK,ammo_no_message_pos)

    ADS.update()
    P.update()
    T.update()

def eventhandler():
    if event.type==QUIT :
            pygame.quit()
            sys.exit(0)
    if event.type == MOUSEBUTTONUP:
        if event.button == 1:       #LEFT CLICK
            ADS.fire(P)
            #T.update()
    if event.type == KEYDOWN:
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_TAB]:
            pygame.quit()
            sys.exit(0) 

game_init()

while True:

    DISPLAY_WINDOW.fill(COLOR_WHITE)

    for event in pygame.event.get():
        eventhandler()

    spawner()
    #Conditions()
           
    pygame.display.update()
    GAME_CLOCK.tick(FPS)

