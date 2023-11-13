import pygame
import pygame_menu
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
from Sound_effects import reload_sound,shooting_sound,explosion_sound,game_over_sound
from Sprites import *

pygame.init()

pygame.mouse.set_visible(False)
    
#+++++FUNCTIONS++++++

def set_difficulty(value,index):
    print(value,index)
    difficulty=value
    difficulty_index=index
    print(difficulty,difficulty_index)
   
def spawner():
    
    background(LINK_ASSETS_BACKGROUND)
    planets()
    power()
    

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
        #game_over_sound.play(0)
        message(game_over_message_text,COLOR_GREEN,game_over_message_pos,FONT_GAME_OVER)
    
    DISPLAY_WINDOW.blit(ADS.image,ADS.rect) #Aim Spawn
    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PlayerSpawn

    #SCREENS

    screens()

    message(score_message_text,COLOR_GREEN,score_message_pos,FONT_BASIC)
    message(lives_message_text,COLOR_GREEN,lives_message_pos,FONT_BASIC)
    message(ammo_message_text,COLOR_GREEN,ammo_message_pos,FONT_BASIC)
    message(username,COLOR_GREEN,username_pos,FONT_BASIC)
    message(str(difficulty[difficulty_index]),COLOR_GREEN,difficulty_pos,FONT_BASIC)

    #RELOAD

    if P.ammo<1:
        message(ammo_no_message_text,COLOR_GREEN,ammo_no_message_pos,FONT_BASIC)

    #PLAYER HP
    
    if hitbox.dead==False:
        Ally_Hit=pygame.sprite.spritecollide(hitbox,Target_spawn.group,True)
        if Ally_Hit:
            screen_effect(COLOR_RED)
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
        P.ammo_supplies-=0.1
        

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
                pygame.draw.line(DISPLAY_WINDOW,COLOR_RED,(P.posx,P.posy),pygame.mouse.get_pos())
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
    for event in pygame.event.get():
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
                run_main_game=False
                mainmenu()   
            if pressed_key[K_r]:
                if hitbox.dead==False:
                    reload()   

def mainmenu():
    def mainmenu2():
        button_enter.hide()
        button_username.hide()
        username=button_username.get_value()
        button_startgame=menu.add.button(" Start Game ",maingame)
        button_selector=menu.add.selector(" Difficulty : ",items=difficulty,selector_id="Difficulty Selection",onchange=set_difficulty)
        menu.add.button(" Quit ",pygame_menu.events.EXIT)       

    def maingame():
        pygame.display.set_caption("DECK COMMANDER V0.4")
        pygame.mouse.set_visible(False) 
        while run_main_game:
            eventhandler()
            spawner()
                
            pygame.display.flip()
            GAME_CLOCK.tick(FPS)

    pygame.mouse.set_visible(False)
    menu_theme=pygame_menu.themes.THEME_DARK
    menu_theme.background_color=pygame_menu.BaseImage(LINK_ASSETS_BACKGROUND)
    menu_theme.title_font=FONT_MENU_TITLE
    menu_theme.title_font_color=COLOR_GREEN
    menu_theme.title_background_color=(0,0,0,0)
    menu_theme.widget_font=FONT_LCD
    menu_theme.widget_font_color=COLOR_GREEN
    #menu_theme.widget_margin=(-600,0)
    #menu_theme.title_color=COLOR_GREEN
    menu_title="    -----DECK COMMANDER-----"
    menu=pygame_menu.Menu(menu_title,DISPLAY_WIDTH,DISPLAY_HEIGHT,theme=menu_theme)

    button_username=menu.add.text_input(" Username : ",default="Uknown Player",maxchar=15)
    button_enter=menu.add.button(" Enter ",mainmenu2)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT :
                exit()

        menu.mainloop(DISPLAY_WINDOW)

mainmenu()