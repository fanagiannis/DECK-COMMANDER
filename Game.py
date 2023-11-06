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

pygame.display.set_caption("DECK COMMANDER V0.1")

#+++++FONT+++++
FONT_BASIC=pygame.font.Font("C:\\Users\\GIANNIS\\OneDrive\\Υπολογιστής\\pixel_lcd_7.ttf",15)
FONT_GAME_OVER=pygame.font.Font("C:\\Users\\GIANNIS\\OneDrive\\Υπολογιστής\\pixel_lcd_7.ttf",40)
    
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
    
def spawner():
    
    #MESSAGES
    
    score_live="%06d" % P.score
    ammo_live="%02d" % int(P.ammo)
    score_message_text = "Score : "+ score_live #ADD ZEROES BEFORE SCORE
    lives_message_text = "HP : "+ str(hitbox.hp)
    game_over_message_text = "GAME OVER ! "
    ammo_message_text = "Ammo : " + ammo_live + f"/{int(P.ammo_supplies)}"
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

    DISPLAY_WINDOW.fill(COLOR_BLACK)

    for event in pygame.event.get():
        eventhandler()

    spawner()
           
    pygame.display.update()
    GAME_CLOCK.tick(FPS)

