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
from Hitbox import Hitbox

from Variables import *
from Constants import *
from Sound_effects import reload_sound

pygame.init()

pygame.display.set_caption("GAME V0.0.8")

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
    lives_message_text = "HP : "+ str(hitbox.hp)
    game_over_message_text = "GAME OVER ! "
    ammo_message_text = "Ammo : " + ammo_live
    ammo_no_message_text = "OUT OF AMMO! "
    
    if hitbox.dead==False:
        Target_spawn.group.draw(DISPLAY_WINDOW)
    else:
        Target_spawn.group.empty()
        message(game_over_message_text,COLOR_BLACK,game_over_message_pos)
    
    DISPLAY_WINDOW.blit(ADS.image,ADS.rect) #Aim Spawn
    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PlayerSpawn


    message(score_message_text,COLOR_BLACK,score_message_pos)
    message(lives_message_text,COLOR_BLACK,lives_message_pos)
    message(ammo_message_text,COLOR_BLACK,ammo_message_pos)

    #RELOAD

    if P.ammo<=0:
        message(ammo_no_message_text,COLOR_BLACK,ammo_no_message_pos)

    #PLAYER HP
    
    if hitbox.dead==False:
        Ally_Hit=pygame.sprite.spritecollide(hitbox,Target_spawn.group,True)
        if Ally_Hit:
            hitbox.hp-=Target_Damage
        pass
    
    #UPDATE
    if hitbox.IsRepairing==False:
        ADS.icon_reset()
        if hitbox.dead==False:
            P.update()
    else:
        ADS.repair()
        print("IMMOBILIZED")
    ADS.update()
    Target_spawn.update()
    hitbox.update()

def fire():
    if hitbox.IsRepairing:
        print("REPAIRING...")
    else:
        if P.ammo>0:
            if hitbox.hp>0:
                DISPLAY_WINDOW.fill(COLOR_YELLOW)
                hit=pygame.sprite.spritecollide(ADS,Target_spawn.group,True)
                if hit:
                    P.score+=100
                    print("HIT")
                P.ammo-=1
                ADS.Fired=False

def reload():
    reload_sound.play()
    P.ammo=10


def eventhandler():
    if event.type==QUIT :
            pygame.quit()
            sys.exit(0)
    if event.type == MOUSEBUTTONUP:
        if event.button == 1:       #LEFT CLICK
            if hitbox.dead==False:
                ADS.fire()
                fire()
    if event.type == KEYDOWN:
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_TAB]:
            pygame.quit()
            sys.exit(0) 
        if pressed_key[K_r]:
            if hitbox.dead==False:
                reload()
        if pressed_key[K_f]:
            pass

game_init()

while True:

    DISPLAY_WINDOW.fill(COLOR_WHITE)

    for event in pygame.event.get():
        eventhandler()

    spawner()
    #Conditions()
           
    pygame.display.update()
    GAME_CLOCK.tick(FPS)

