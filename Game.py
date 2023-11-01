import pygame
import sys
import random
import math


from pygame.locals import *
from pygame.sprite import *

from Classes import Aim
from Classes import Player
from Classes import Target

from Constants import *
from Variables import *


pygame.init()

pygame.display.set_caption("GAME V0.0")

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

