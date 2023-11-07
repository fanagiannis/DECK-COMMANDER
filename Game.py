import pygame
import sys

from pygame.locals import *
from pygame.sprite import *

from Scope import Aim
from Player import Player
from Target import Target
from Spawner_Targets import Spawner
from Hitbox import Hitbox

from Variables import *
from Constants import *
from Sound_effects import reload_sound,shooting_sound,explosion_sound

pygame.init()

pygame.display.set_caption("DECK COMMANDER V0.2")

#+++++FONT+++++
FONT_LCD="Fonts\\pixel_lcd_7.ttf"
FONT_BASIC=pygame.font.Font(FONT_LCD,15)
FONT_GAME_OVER=pygame.font.Font(FONT_LCD,40)
    
#+++++FUNCTIONS++++++
def get_mousepos():
    return pygame.mouse.get_pos()

def mouse_pos_check():
    print(get_mousepos())

def screen_effect(color):
    DISPLAY_WINDOW.fill(color)

def message(text,text_color,text_pos,font):
    display_text=font.render(text,True,text_color)
    DISPLAY_WINDOW.blit(display_text,text_pos)
    pass   

def background(image):
    background=pygame.image.load(image)
    DISPLAY_WINDOW.blit(background,(0,0))

def game_init():
    pygame.mouse.set_visible(False)

def screens():
    #pygame.draw.rect(DISPLAY_WINDOW,COLOR_YELLOW,(DISPLAY_WIDTH-200,DISPLAY_HEIGHT-100,DISPLAY_WIDTH,DISPLAY_HEIGHT)) #AMMO/HP SCREEN
    SCREEN1=pygame.image.load(LINK_ASSETS_SCREEN)
    SCREEN2=pygame.image.load(LINK_ASSETS_SCREEN3)
    DISPLAY_WINDOW.blit(SCREEN2,(DISPLAY_WIDTH-200,DISPLAY_HEIGHT-100))
    #pygame.draw.rect(DISPLAY_WINDOW,COLOR_YELLOW,(0,DISPLAY_HEIGHT-100,200,DISPLAY_HEIGHT)) #SCORE SCREEN
    DISPLAY_WINDOW.blit(SCREEN2,(0,DISPLAY_HEIGHT-100))

def planets():
    PLANET=pygame.image.load(LINK_ASSETS_PLANET)
    PLANETSCALED=pygame.transform.scale(PLANET,(200,200))
    PLANET2=pygame.image.load(LINK_ASSETS_PLANET2)
    PLANET2SCALED=pygame.transform.scale(PLANET2,(100,100))
    PLANET3=pygame.image.load(LINK_ASSETS_PLANET3)
    PLANET3SCALED=pygame.transform.scale(PLANET3,(100,100))

    DISPLAY_WINDOW.blit(PLANETSCALED,(-75,DISPLAY_HEIGHT/2))
    DISPLAY_WINDOW.blit(PLANET2SCALED,(DISPLAY_WIDTH-250,0))
    DISPLAY_WINDOW.blit(PLANET3SCALED,(450,0))

def line_animation():
    pass
    
   
def spawner():

    background(LINK_ASSETS_BACKGROUND)
    planets()
    
    #MESSAGES
    
    score_live="%06d" % P.score
    ammo_live="%02d" % int(P.ammo)
    hp_live="%04d" % int(hitbox.hp)
    score_message_text = f"Score : {score_live}" #ADD ZEROES BEFORE SCORE
    lives_message_text = f"HP : {hp_live}" 
    game_over_message_text = "GAME OVER ! "
    ammo_message_text = f"Energy : {ammo_live}"
    ammo_no_message_text = "OUT OF AMMO! "

    if hitbox.dead==False:
        Target_spawn.group.draw(DISPLAY_WINDOW)
    else:
        Target_spawn.group.empty()
        message(game_over_message_text,COLOR_GREEN,game_over_message_pos,FONT_GAME_OVER)
    
    DISPLAY_WINDOW.blit(ADS.image,ADS.rect) #Aim Spawn
    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PlayerSpawn

    #SCREENS

    screens()

    message(score_message_text,COLOR_GREEN,score_message_pos,FONT_BASIC)
    message(lives_message_text,COLOR_GREEN,lives_message_pos,FONT_BASIC)
    message(ammo_message_text,COLOR_GREEN,ammo_message_pos,FONT_BASIC)

    #RELOAD

    if P.ammo<1:
        message(ammo_no_message_text,COLOR_GREEN,ammo_no_message_pos,FONT_BASIC)

    #PLAYER HP
    
    if hitbox.dead==False:
        Ally_Hit=pygame.sprite.spritecollide(hitbox,Target_spawn.group,True)
        if Ally_Hit:
            explosion_sound.play()
            hitbox.hp-=Target_Damage
        pass
    
    #UPDATE
    if hitbox.IsRepairing==False:
        ADS.icon_reset()
        if hitbox.dead==False:
            P.update()
    else:
        ADS.repair()

    P.reload()
  
    ADS.update()
    Target_spawn.update()
    hitbox.update()

def fire():
    if hitbox.IsRepairing:
        print("REPAIRING...")
    else:
        if P.ammo>=1:
            if hitbox.hp>0:
                DISPLAY_WINDOW.fill(COLOR_YELLOW)
                hit=pygame.sprite.spritecollide(ADS,Target_spawn.group,True)
                if hit:
                    P.score+=100
                shooting_sound.play()
                P.ammo-=1
                ADS.Fired=False

def reload():
    if P.ammo<P.maxammo :
        reload_sound.play()

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

game_init()

while True:

    #DISPLAY_WINDOW.fill(COLOR_BLACK)

    for event in pygame.event.get():
        eventhandler()

    spawner()
           
    pygame.display.flip()
    GAME_CLOCK.tick(FPS)

