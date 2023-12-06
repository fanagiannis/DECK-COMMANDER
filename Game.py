import pygame
import pygame_menu
import sys

from pygame.locals import *
from pygame.sprite import *

from Classes.Scope import Aim
from Classes.Player import Player
from Classes.Target import Target
from Classes.Spawner_Targets import Spawner
from Classes.Hitbox import Hitbox
from Classes.Projectiles import Projectile
from Classes.Gamemode import Gamemode

from Var.Variables import * 
from Var.Constants import *
from assets.Sound_effects import shooting_sound,explosion_sound,game_over_sound
from assets.Sprites import *

pygame.init()
pygame.display.set_caption("DECK COMMANDER V0.6B")
pygame.mouse.set_visible(False)
    
#+++++FUNCTIONS++++++
    
def spawner():
    
    #BACKGROUND SET

    background(LINK_ASSETS_BACKGROUND)
    planets()

    #POWER FEEDBACK

    power()

    #MESSAGES
    
    score_live="%06d" % P.score
    ammo_live="%02d" % int(P.ammo)
    hp_live="%04d" % int(hitbox.hp)
    gameround_live="%02d" % gm.round
    score_message_text = f"Score : {score_live}" #ADD ZEROES BEFORE SCORE
    hp_message_text = f"HP : {hp_live}" 
    game_over_message_text = "GAME OVER ! "
    energy_message_text = f"Energy : {ammo_live}"
    energy_no_message_text = "OUT OF AMMO! "
    gameround_message_text=f"Round : {gameround_live}"

    #TARGET SPAWN

    if hitbox.dead==False:
        Target_spawn.group.draw(DISPLAY_WINDOW)
    else:
        Target_spawn.group.empty()
        #game_over_sound.play(0)
        message(game_over_message_text,COLOR_GREEN,game_over_message_pos,FONT_GAME_OVER)
    
    #AIM,PLAYER SPAWN

    DISPLAY_WINDOW.blit(ADS.image,ADS.rect) #Aim Spawn
    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PlayerSpawn

    #SCREENS SPAWN

    screens()

    #MESSAGES SPAWN

    message(score_message_text,COLOR_GREEN,score_message_pos,FONT_BASIC)
    message(hp_message_text,COLOR_GREEN,hp_message_pos,FONT_BASIC)
    message(energy_message_text,COLOR_GREEN,energy_message_pos,FONT_BASIC)
    message(username,COLOR_GREEN,username_pos,FONT_BASIC)
    message(gameround_message_text,COLOR_GREEN,gameround_pos,FONT_BASIC)

    #RELOAD

    if P.ammo<1:
        message(energy_no_message_text,COLOR_GREEN,energy_no_message_pos,FONT_BASIC)

    #PLAYER HP
    
    if hitbox.dead==False:
        Ally_Hit=pygame.sprite.spritecollide(hitbox,Target_spawn.group,True)
        if Ally_Hit:
            screen_effect(COLOR_RED)
            explosion_sound.play()
            hitbox.hp-=gm.t_Damage
            if hitbox.hp<0:
                hitbox.hp=0
    
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
    rounds()
    for projectile in projectiles_group:
        projectile.draw()

def rounds():
    if P.score==gm.game_round_change_score:
        gm.round_inc()
    if gm.round==gm.round_change:
        gm.round_difficulty_inc()
        if P.scoreinc<1000:
            P.scoreinc+=100
        Target_spawn.time_set=gm.t_spawn_time
        Target_spawn.targetdmg=gm.t_Damage
        Target_spawn.targetspeed=gm.t_speed

def fire():
    if hitbox.IsRepairing:
        print("REPAIRING...")
    else:
        if P.ammo>=1:
            if hitbox.hp>0:
                pygame.draw.line(DISPLAY_WINDOW,COLOR_RED,(P.posx,P.posy),pygame.mouse.get_pos())
                shooting_sound.play()
                P.ammo-=1
                ADS.Fired=False
                projectiles_group.add(Projectile(gunpos))
     
def eventhandler():
    for event in pygame.event.get():
        if event.type==QUIT :
                pygame.quit()
                sys.exit(0)
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:       #LEFT CLICK
                if hitbox.dead==False:
                    #ADS.fire()
                    fire()
                    
        if event.type == KEYDOWN:
            pressed_key=pygame.key.get_pressed()
            if pressed_key[K_TAB]:
                run_main_game=False
                game()     
    for Projectile in projectiles_group:
        Projectile.update()

def game():        
    def maingame_solo():
        pygame.mouse.set_visible(False)
        while run_main_game:
            eventhandler()
            spawner()
            pygame.display.flip()
            GAME_CLOCK.tick(FPS)
    def username():
        global button_enterusername,button_username
        button_username=menu.add.text_input(" Enter Username : ",default="Player",maxchar=12)
        button_enterusername=menu.add.button(" Enter ",mainmenu)
        
    def leaderboards():
        leaderboard=menu.add.table(table_id="leaderboards")#,bordercolor=COLOR_GREEN,)
        leaderboard.set_border(1700,None,inflate=(0,0))#,position=(300,500,1000,1200))  
        leaderboard.add_row(cells=['   TOP PLAYERS'],cell_border_color=COLOR_GREEN,cell_border_width=2)
        leaderboard.add_row(cells=['ID' '  PLAYER' '  SCORE'],cell_border_color=COLOR_GREEN,cell_border_width=2)
        leaderboard.set_float(float_status=True)    
        pass
    def mainmenu():
        menu_theme.widget_margin=(-600,0)
        global username
        username=button_username.get_value()
        menu.remove_widget(button_username)
        menu.remove_widget(button_enterusername)
        leaderboards()
        button_startgame=menu.add.button(" Singleplayer ",maingame_solo)
        button_leaderboards=menu.add.button(" Multiplayer ",leaderboards)
        
        #button_leaderboards=menu.add.button(" Leaderboards ",leaderboards)
        menu.add.button(" Quit ",pygame_menu.events.EXIT)

    pygame.mouse.set_visible(False)
    menu_theme=pygame_menu.themes.THEME_DARK
    menu_theme.background_color=pygame_menu.BaseImage(LINK_ASSETS_BACKGROUND)
    menu_theme.title_font=FONT_MENU_TITLE
    menu_theme.title_font_color=COLOR_GREEN
    menu_theme.title_background_color=(0,0,0,0)
    menu_theme.widget_font=FONT_LCD
    menu_theme.widget_font_color=COLOR_GREEN
    #menu_theme.title_color=COLOR_GREEN
    menu_title="    -----DECK COMMANDER-----"
    menu=pygame_menu.Menu(menu_title,DISPLAY_WIDTH,DISPLAY_HEIGHT,theme=menu_theme)
    username()  
    while True:
        for event in pygame.event.get():
            if event.type == QUIT :
                exit()

        menu.mainloop(DISPLAY_WINDOW)

game()