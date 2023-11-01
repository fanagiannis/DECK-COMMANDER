import pygame
import sys
import random
import math

from pygame.locals import *
from pygame.sprite import *

from Scope import Aim
from Player import Player
from Target import Target
from Spawner import Spawner
from Spawner import Target

from Variables import *

pygame.init()

pygame.display.set_caption("GAME V0.0.7.3")

#+++++LINKS+++++

LINK_ASSETS_BASE_PC="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
LINK_ASSETS_BASE_LAPTOP="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
LINK_ASSETS_BASE=LINK_ASSETS_BASE_PC
LINK_ASSETS_PLAYER=LINK_ASSETS_BASE+"\\Player.png"
LINK_ASSETS_CURSOR=LINK_ASSETS_BASE+"\\Aim.png"
LINK_ASSETS_AIMCURSOR=LINK_ASSETS_BASE+"\\AimBig.png"
LINK_ASSETS_BULLETS=LINK_ASSETS_BASE+"\\Bullet.png"
LINK_ASSETS_TARGET=LINK_ASSETS_BASE+"\\Enemy.png"

   #+++++DISPLAY+++++

DISPLAY_WIDTH=1240
DISPLAY_HEIGHT=720
DISPLAY_WINDOW=pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

    #+++++COLORS+++++

COLOR_BLACK=pygame.Color(0,0,0)
COLOR_WHITE=pygame.Color(255,255,255)
COLOR_GREY=pygame.Color(128,128,128)
COLOR_RED=pygame.Color(255,0,0)
COLOR_YELLOW=pygame.Color(255,255,0)

GAME_CLOCK=pygame.time.Clock()
FPS=60

#+++++FONT+++++
FONT=pygame.font.SysFont(None,30,bold=True)
    
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

def spawner():
    
    #MESSAGES
    
    score_live="%06d" % P.score
    ammo_live="%02d" % P.ammo
    score_message_text = "Score : "+ score_live #ADD ZEROES BEFORE SCORE
    lives_message_text = "Lives : "+ str(P.lives)
    game_over_message_text = "GAME OVER ! "
    ammo_message_text = "Ammo : " + ammo_live
    ammo_no_message_text = "OUT OF AMMO! "

    DISPLAY_WINDOW.blit(ADS.image,ADS.rect) #Aim Spawn
    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PlayerSpawn
    
    if P.lives>0:
        Target_spawn.group.draw(DISPLAY_WINDOW)
    else:
        message(game_over_message_text,COLOR_BLACK,game_over_message_pos)


    message(score_message_text,COLOR_BLACK,score_message_pos)
    message(lives_message_text,COLOR_BLACK,lives_message_pos)
    message(ammo_message_text,COLOR_BLACK,ammo_message_pos)

    #RELOAD

    if P.ammo<=0:
        message(ammo_no_message_text,COLOR_BLACK,ammo_no_message_pos)

    #PLAYER LIVES
    
    if P.lives>0:
        pass#Target.shot()
    
    #if Target.posy>DISPLAY_HEIGHT:
        #P.lives-=1

    #UPDATES

    ADS.update()
    P.update()
    Target_spawn.update()

def fire():
    if P.ammo>0:
        if P.lives>0:
            DISPLAY_WINDOW.fill(COLOR_YELLOW)
            if ADS.rect.colliderect(Target.rect):
                Target.reset_position()
                P.score+=score_value
            P.ammo-=1
            ADS.Fired=False

def eventhandler():
    if event.type==QUIT :
            pygame.quit()
            sys.exit(0)
    if event.type == MOUSEBUTTONUP:
        if event.button == 1:       #LEFT CLICK
            ADS.fire(P,Target)
            fire()
            #T.update()
    if event.type == KEYDOWN:
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_TAB]:
            pygame.quit()
            sys.exit(0) 
        if pressed_key[K_r]:
            P.ammo=10

game_init()

while True:

    DISPLAY_WINDOW.fill(COLOR_WHITE)

    for event in pygame.event.get():
        eventhandler()

    spawner()
    #Conditions()
           
    pygame.display.update()
    GAME_CLOCK.tick(FPS)

