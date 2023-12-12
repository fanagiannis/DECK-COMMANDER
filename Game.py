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

from Database.Leaderboard import *
from Var.Variables import * 
from Var.Constants import *
from assets.Sound_effects import shooting_sound,explosion_sound,game_over_sound
from assets.Sprites import *

pygame.init()
pygame.display.set_caption("DECK COMMANDER V0.7B")
pygame.mouse.set_visible(False)
    
def spawner():

    #print(gm.t_speed,gm.t_Damage,gm.t_spawn_time)
    background(LINK_ASSETS_BACKGROUND)  #BACKGROUND SET
    hp()                                #POWER FEEDBACK
    messages()                          #MESSAGES 
    #screens()                          #SCREENS SPAWN

    #TARGET SPAWN

    if hitbox.dead==False:
        Target_spawn.group.draw(DISPLAY_WINDOW)
    else:
        event_game_over()

    #MESSAGES SPAWN

    message(score_message_text,COLOR_GREEN,score_message_pos,FONT_BASIC)
    message(hp_message_text,COLOR_GREEN,hp_message_pos,FONT_BASIC)
    message(energy_message_text,COLOR_GREEN,energy_message_pos,FONT_BASIC)
    message(username,COLOR_GREEN,username_pos,FONT_BASIC)
    message(gameround_message_text,COLOR_GREEN,gameround_pos,FONT_BASIC)
    message(exit_game_message_text,COLOR_GREEN,game_over_return_mes_pos,FONT_BASIC)

    if P.ammo<1:
        message(energy_no_message_text,COLOR_GREEN,energy_no_message_pos,FONT_BASIC)
    
    event_ally_hit()                    #ALLY HIT
    event_repair()                      #REPAIR

    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PLAYER SPAWN

    #UPDATES
    P.reload()
    ADS.update()
    Target_spawn.update()
    hitbox.update()
    rounds()
    for projectile in projectiles_group:
        projectile.draw()

def messages():
    global hp_live,score_message_text,hp_message_text,game_over_message_text,game_over_message_stats,energy_message_text,energy_no_message_text,gameround_message_text,exit_game_message_text
    score_live="%06d" % P.score
    ammo_live="%02d" % int(P.ammo)
    hp_live="%04d" % int(hitbox.hp)
    gameround_live="%02d" % gm.round
    score_message_text = f"Score : {score_live}" #ADD ZEROES BEFORE SCORE
    hp_message_text = "HP " 
    game_over_message_text = "GAME OVER ! "
    game_over_message_stats =f" Round :"f"{gameround_live}"+" "+f"Score : "f"{score_live}"
    energy_message_text = f"Energy : {ammo_live}"
    energy_no_message_text = "OUT OF AMMO! "
    gameround_message_text=f"Round : {gameround_live}"
    exit_game_message_text="PRESS TAB TO RETURN TO THE MAIN MENU"

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

def event_ally_hit():
    if hitbox.dead==False:
        Ally_Hit=pygame.sprite.spritecollide(hitbox,Target_spawn.group,True)
        if Ally_Hit:
            screen_effect(COLOR_RED)
            explosion_sound.play()
            hitbox.hp-=gm.t_Damage
            if P.score>0:
                P.score-=10
            if hitbox.hp<0:
                hitbox.hp=0

def event_repair():
    if hitbox.IsRepairing==False:
        
        ADS.icon_reset()
        if hitbox.dead==False:
            P.update()
    else:
        DISPLAY_WINDOW.blit(ADS.image,ADS.rect)
        ADS.repair()
        P.ammo_supplies-=0.1

def event_game_over():
    Target_spawn.group.empty()
    #game_over_sound.play(0)
    message(game_over_message_text,COLOR_GREEN,game_over_message_pos,FONT_GAME_OVER)
    message(game_over_message_stats,COLOR_GREEN,game_over_message_stats_pos,FONT_STATS)
    run_main_game=False
    gm.game_over=True

def game_over_stats():
        game_over_add_leaderboard(username,P.score,gm.round)
        print("GAME OVER")       

def reset_game():
    P.reset()
    Target_spawn.reset()
    gm.reset()
    hitbox.reset()
    projectiles_group.empty()

def game():        
    def maingame_solo():
        reset_game()
        pygame.mouse.set_visible(False)
        global username
        username=button_username.get_value()
        run_main_game=True
        while run_main_game:
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
                        print("GAME EXITED!")
                        if gm.game_over:
                            game_over_stats()
                        run_main_game=False
            for Projectile in projectiles_group:
                Projectile.update()
            spawner()
            pygame.display.flip()
            GAME_CLOCK.tick(FPS)
        
        #button_enterusername=menu.add.button(" Enter ",mainmenu)       
    def leaderboards():
        leaderboard=menu.add.table(table_id="leaderboards")#,bordercolor=COLOR_GREEN,)
        leaderboard.set_border(1450,None,inflate=(0,0))#,position=(300,500,1000,1200))
        leaderboard.add_row(cells=['  TOP PLAYERS '],cell_border_color=COLOR_GREEN,cell_border_width=2)  
        leaderboard.add_row(cells=['    PLAYER ','SCORE','ROUND'],cell_border_color=COLOR_GREEN,cell_border_width=2)  
        table_query="""
        SELECT username,score,round FROM players ORDER BY score DESC;
        """
        columns,players=read_leaderboard(table_query)
        for player in players:
            leaderboard.add_row(cells=[ player[0] ,player[1], player[2]],cell_border_color=COLOR_GREEN,cell_border_width=2)
        leaderboard.set_float(float_status=True)    
        pass

    def mainmenu():
        menu_theme.widget_margin=(-600,0)
        global button_username
        if gm.game_over:
            game_over_stats(game_over)
        button_username=menu.add.text_input(" Enter Username : ",default="Player",maxchar=12)
        leaderboards()
        button_startgame=menu.add.button(" Singleplayer ",maingame_solo)
        button_leaderboards=menu.add.button(" Multiplayer ",leaderboards)
        menu.add.button(" Quit ",exit)

    def exit():
        pygame.quit()
        sys.exit(0)    

    pygame.mouse.set_visible(False)
    menu_theme=pygame_menu.themes.THEME_DARK
    menu_theme.background_color=pygame_menu.BaseImage(LINK_ASSETS_BACKGROUND)
    menu_theme.title_font=FONT_MENU_TITLE
    menu_theme.title_font_color=COLOR_GREEN
    menu_theme.title_background_color=(0,0,0,0)
    menu_theme.widget_font=FONT_LCD
    menu_theme.widget_font_color=COLOR_GREEN
    menu_title="    -----DECK COMMANDER-----"
    menu=pygame_menu.Menu(menu_title,DISPLAY_WIDTH,DISPLAY_HEIGHT,theme=menu_theme)
    mainmenu() 
    mainmenuloop=menu.mainloop(DISPLAY_WINDOW)
    
    print("QUIT!")
    game_over_stats(game_over)

game()