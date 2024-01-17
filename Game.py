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

print(P.playerID,P2.playerID)

#SPAWNS SPRITES/EVENTS  
def set_game_solo():
    background(LINK_ASSETS_BACKGROUND)          #BACKGROUND SET
    hp()                                        #POWER FEEDBACK
    messages()                                  #MESSAGES 

    if hitbox.dead==False:
        Target_spawn.group.draw(DISPLAY_WINDOW)  #SET TARGET SPAWNER SPAWN
    else:
        event_game_over()                        #IF GAME OVER --> DISABLE SPAWNER 

    #SPAWN MESSAGES

    message(score_message_text,COLOR_GREEN,score_message_pos,FONT_BASIC)
    message(hp_message_text,COLOR_GREEN,hp_message_pos,FONT_BASIC)
    message(energy_message_text,COLOR_GREEN,energy_message_pos,FONT_BASIC)
    message(username,COLOR_GREEN,username_pos,FONT_BASIC)
    message(gameround_message_text,COLOR_GREEN,gameround_pos,FONT_BASIC)
    message(exit_game_message_text,COLOR_GREEN,game_over_return_mes_pos,FONT_BASIC)

    if P.ammo<1:
        message(energy_no_message_text,COLOR_GREEN,energy_no_message_pos,FONT_BASIC)   #SPAWN NO AMMO MESSAGE (IF NO AMMO)
    
    #EVENTS
        
    event_ally_hit()                            #ALLY HIT
    event_repair()                              #REPAIR

    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PLAYER SPAWN

    #UPDATES
    P.reload()              #UPDATE PLAYER
    ADS.update()            #UPDATE AIM
    Target_spawn.update()   #UPDATE TARGET SPAWNER
    hitbox.update()         #UPDATE HITBOX

    #ROUND MANIPULATION
    rounds()           

    for projectile in projectiles_group:    #DRAW PROJECTILES
        projectile.draw()   
def set_game_multiplayer():
    background(LINK_ASSETS_BACKGROUND)          #BACKGROUND SET
    hp()                                        #POWER FEEDBACK
    messages()                                  #MESSAGES 
    messages_multiplayer()                      #MULTIPLAYER MESSAGES 
    
    if hitbox.dead==False:
        Target_spawn.group.draw(DISPLAY_WINDOW)  #SET TARGET SPAWNER SPAWN
    else:
        event_game_over_multiplayer()                        #IF GAME OVER --> DISABLE SPAWNER 

    #SPAWN MESSAGES

    message(score_message_text,COLOR_GREEN,score_message_pos,FONT_BASIC)         #P1 SCORE MESSAGE
    message(p2_score_message_text,COLOR_GREEN,P2_score_message_pos,FONT_BASIC)      #P2 SCORE MESSAGE

    message(hp_message_text,COLOR_GREEN,hp_message_pos,FONT_BASIC)

    message(energy_message_text,COLOR_GREEN,energy_message_pos,FONT_BASIC)       #P1 AMMO
    message(p2_energy_message_text,COLOR_GREEN,P2_energy_message_pos,FONT_BASIC)    #P2 AMMO

    message(username,COLOR_GREEN,username_pos,FONT_BASIC)                      #HOST USERNAME
    message(gameround_message_text,COLOR_GREEN,multiplayer_gameround_pos,FONT_BASIC)    #GANEROUND MESSAGE
    message(exit_game_message_text,COLOR_GREEN,game_over_return_mes_pos,FONT_BASIC)     #GAME OVER MESSAGE

    if P.ammo<1:
        message(energy_no_message_text,COLOR_GREEN,energy_no_message_pos,FONT_BASIC)   #SPAWN NO AMMO MESSAGE (IF NO AMMO)
    if P2.ammo<1:
        message(energy_no_message_text2,COLOR_GREEN,energy_no_message_pos2,FONT_BASIC)
    
    #EVENTS
        
    event_ally_hit()                            #ALLY HIT
    event_repair()                              #REPAIR

    DISPLAY_WINDOW.blit(P.image_rotated,P.rect_rotated) #PLAYER SPAWN
    DISPLAY_WINDOW.blit(P2.image_rotated,P2.rect_rotated) #PLAYER 2 SPAWN

    #UPDATES
    P.reload()              #UPDATE PLAYER
    P2.reload()             #UPDATE PLAYER 2
    P2.update()
    ADS.update()            #UPDATE AIM
    Target_spawn.update()   #UPDATE TARGET SPAWNER
    hitbox.update()         #UPDATE HITBOX

    #ROUND MANIPULATION
    rounds_multiplayer()           

    for projectile in projectiles_group:    #DRAW PROJECTILES
        projectile.draw()                   
#SET MESSAGES
def messages():
    global hp_live,score_message_text,hp_message_text,game_over_message_text,game_over_message_stats,energy_message_text,energy_no_message_text,gameround_message_text,exit_game_message_text,gameround_live,score_live
    #STATS MESSAGES
    score_live="%06d" % P.score                  #SCORE MESSAGE

    #score2_live="%06d" % P2.score    

    ammo_live="%02d" % int(P.ammo)               #PLAYER AMMO MESSAGE
    hp_live="%04d" % int(hitbox.hp)              #PLAYER HP MESSAGE
    gameround_live="%02d" % gm.round             #GAME ROUND MESSAGE
    #STATIC MESSAGES
    score_message_text = f"Score : {score_live}" #STATIC SCORE MESSAGE

    #score2_message_text=f"Score : {score2_live}"

    hp_message_text = "HP "                      #STATIC HP MESSAGE
    game_over_message_text = "GAME OVER ! "      #STATIC GAME OVER MESSAGE
    game_over_message_stats =f" Round :"f"{gameround_live}"+" "+f"Player 1 Score : "f"{score_live}"  #STATIC GAME OVER MESSAGE WITH STATS
    energy_message_text = f"Energy : {ammo_live}"        #STATIC ENERGY MESSAGE
    energy_no_message_text = "OUT OF AMMO! "             #STATIC NO ENERGY MESSAGE
    gameround_message_text=f"Round : {gameround_live}"   #STATIC ROUND MESSAGE
    exit_game_message_text="PRESS TAB TO RETURN TO THE MAIN MENU"     #EXIT GAME MESSAGE  
def messages_multiplayer():
    global p2_score_live,p2_ammo_live,p2_energy_message_text,p2_score_message_text,energy_no_message_text,energy_no_message_text2,game_over_message_stats2
    #STATS MESSAGES
    p2_score_live="%06d" % P2.score                          #SCORE MESSAGE
    p2_ammo_live="%02d" % int(P2.ammo)                       #PLAYER AMMO MESSAGE
    p2_energy_message_text = f"Energy 2: {p2_ammo_live}"      #STATIC ENERGY MESSAGE
    p2_score_message_text = f"Score 2: {p2_score_live}"       #STATIC SCORE MESSAGE
    energy_no_message_text = "PLAYER 1 OUT OF AMMO! "             #STATIC NO ENERGY MESSAGE
    energy_no_message_text2 = "PLAYER 2 OUT OF AMMO! "             #STATIC NO ENERGY MESSAGE
    game_over_message_stats2 =f" Round :"f"{gameround_live}"+" "+f"Player 2 Score : "f"{p2_score_live}"  #STATIC GAME OVER MESSAGE WITH STATS
#ROUND MANIPULATION
def rounds():
    if P.score>=gm.game_round_change_score:         #IF PLAYER SCORE EQUALS SCORE-CHANGING ROUND
        gm.round_inc()                              #CALL FUNCTION FOR ROUND INCREASE FROM GAMEMODE CLASS    
    if gm.round>=gm.round_change:                   #IF ROUND REACHES A THRESHHOLD INCREASE DIFFICULTY
        gm.round_difficulty_inc()                   #CALL FUNCTION FOR DIFFICULTY INCREASE FROM GAMEMODE CLASS (INCREASES TARGET DAMAGE,SPEED AND DECREASES SPAWNTIME)   
        Target_spawn.time_set=gm.t_spawn_time       #SET NEW TARGET SPAWNTIME PARAMETER
        Target_spawn.targetdmg=gm.t_Damage          #SET NEW TARGET DAMAGE PARAMETER
        Target_spawn.targetspeed=gm.t_speed         #SET NEW TARGET SPEED PARAMETER
def rounds_multiplayer():
    if P.score+P2.score>=gm.game_round_change_score:         #IF PLAYER SCORE EQUALS SCORE-CHANGING ROUND
        gm.round_inc()                              #CALL FUNCTION FOR ROUND INCREASE FROM GAMEMODE CLASS    
    if gm.round>=gm.round_change:                   #IF ROUND REACHES A THRESHHOLD INCREASE DIFFICULTY
        gm.round_difficulty_inc()                   #CALL FUNCTION FOR DIFFICULTY INCREASE FROM GAMEMODE CLASS (INCREASES TARGET DAMAGE,SPEED AND DECREASES SPAWNTIME)   
        Target_spawn.time_set=gm.t_spawn_time       #SET NEW TARGET SPAWNTIME PARAMETER
        Target_spawn.targetdmg=gm.t_Damage          #SET NEW TARGET DAMAGE PARAMETER
        Target_spawn.targetspeed=gm.t_speed         #SET NEW TARGET SPEED PARAMETER
#FIRE FUNCTION EVENTS
def fire():
    if hitbox.IsRepairing:             #IF PLAYER IS REPAIRING THEN FIRE IS DISABLED
        print("REPAIRING...")          #CONSOLE REPAIRING MESSAGE             
    else:
        if P.ammo>=1:                  #IF PLAYER IS AMMO BIGGER THAN 1 THEN CHECK IF HITBOX IS ALIVE 
            if hitbox.hp>0:            #CHECK IF HITBOX IS ALIVE 
                shooting_sound.play()                                                                   #PLAY FIRE SOUND
                P.ammo-=1                                                                               #DECREASE AMMO PER FIRE               
                projectiles_group.add(Projectile(P.pos,COLOR_RED))                                               #ADD PROJECTILE TO PROJECTILE GROUP (PROJECTILE CLASS)
def fire_2():
    if hitbox.IsRepairing:             #IF PLAYER IS REPAIRING THEN FIRE IS DISABLED
        print("REPAIRING...")          #CONSOLE REPAIRING MESSAGE             
    else:
        if P2.ammo>=1:                  #IF PLAYER IS AMMO BIGGER THAN 1 THEN CHECK IF HITBOX IS ALIVE 
            if hitbox.hp>0:            #CHECK IF HITBOX IS ALIVE 
                shooting_sound.play()                                                                   #PLAY FIRE SOUND
                P2.ammo-=1                                                                               #DECREASE AMMO PER FIRE                  
                projectiles_group.add(Projectile(P2.pos,COLOR_GREEN))                                               #ADD PROJECTILE TO PROJECTILE GROUP (PROJECTILE CLASS)
#DEFINES EVENT AFTER ALLY HIT
def event_ally_hit():
    if hitbox.dead==False:                                                          #CHECKS IF ALLY IS DEAD (FUNCTION RUNS ONLY IF ALLY IS ALIVE) 
        Ally_Hit=pygame.sprite.spritecollide(hitbox,Target_spawn.group,True)        #BOOL Ally_Hit CHECKS COLLISION OF ENEMY WITH ALLY
        if Ally_Hit:                                                                #IF THE ALLY IS HIT THEN ... 
            screen_effect(COLOR_RED)                                                #HIT SCREEN EFFECT 
            explosion_sound.play()                                                  #HIT SOUND EFFECT
            hitbox.hp-=gm.t_Damage                                                  #ALLY TAKE DAMAGE
            if P.score>0:                                                           #IF PLAYER SCORE IS GREATER THAN 0 
                P.score-=10                                                         #THEN SUBTRACT 10 FROM SCORE AFTER ALLY HIT
            if hitbox.hp<0:                                                         #DISPLAY HP ONLY GREATER THAN 0                            
                hitbox.hp=0
#DEFINES REPAIR EVENT
def event_repair():
    if hitbox.IsRepairing==False:                   #CHECKS IF ALLY IS NOT REPAIRING 
        ADS.icon_reset()                            #SET AIM ICON TO INVISIBLE 
        if hitbox.dead==False:                      #CHECKS IF ALLY IS ALIVE
            P.update()                              #IF ALLY IS ALIVE THEN KEEP UPDATING THE PLAYER
    else:                                           #IF ALLY IS REPAIRING                
        DISPLAY_WINDOW.blit(ADS.image,ADS.rect)     #SET REPAIR ICON TO VISIBLE
        ADS.repair()                                #RUNS REPAIR FUNCTION FROM AIM CLASS
        #P.ammo_supplies-=0.1                        #SUBTRACTS ENERGY SUPPLIES    
#DEFINES GAME OVER EVENT
def event_game_over():
    Target_spawn.group.empty()                                                              #DELETE ALL ENEMY INSTANCES FROM ENEMY GROUP
    #game_over_sound.play(0)                                                                #//CUT//GAME OVER SOUND
    message(game_over_message_text,COLOR_GREEN,game_over_message_pos,FONT_GAME_OVER)        #DISPLAY GAME OVER MESSAGES    
    message(game_over_message_stats,COLOR_GREEN,game_over_message_stats_pos,FONT_STATS)
    run_main_game=False                                                                     #SET RUN GAME BOOLEAN TO FALSE    
    gm.game_over=True                                                                       #SET GAME OVER BOOLEAN TO TRUE        
def event_game_over_multiplayer():
    Target_spawn.group.empty()                                                              #DELETE ALL ENEMY INSTANCES FROM ENEMY GROUP
    #game_over_sound.play(0)                                                                #//CUT//GAME OVER SOUND
    message(game_over_message_text,COLOR_GREEN,game_over_message_pos,FONT_GAME_OVER)        #DISPLAY GAME OVER MESSAGES    
    message(game_over_message_stats,COLOR_GREEN,game_over_message_stats_pos,FONT_STATS)
    message(game_over_message_stats2,COLOR_GREEN,game_over_message_stats_pos2,FONT_STATS)
    run_main_game=False                                                                     #SET RUN GAME BOOLEAN TO FALSE    
    gm.game_over=True 
#GAME OVER STATS LOAD
def game_over_stats():
    game_over_add_leaderboard(username,P.score,gm.round)                                #ADDS STATS TO LEADERBOARD AFTER GAME OVER
    print("GAME OVER")   
def game_over_stats_multiplayer():
    game_over_add_leaderboard(username,P.score,gm.round)                                #ADDS STATS TO LEADERBOARD AFTER GAME OVER
    game_over_add_leaderboard(username+"(P2)",P2.score,gm.round)                        #ADDS STATS TO LEADERBOARD AFTER GAME OVER
    print("GAME OVER")      
#GAME RESET TO DEFAULT
def reset_game():
    P.reset()                                      #RESET PLAYER TO DEFAULT 
    P2.reset()
    Target_spawn.reset()                           #RESET ENEMY SPAWNER TO DEFAULT 
    gm.reset()                                     #RESET GAMEMODE TO DEFAULT     
    hitbox.reset()                                 #RESET ALLY TO DEFAULT     
    projectiles_group.empty()                      #RESET PROJECTILES TO DEFAULT

#MAIN GAME
def game():   
    #SOLO PLAY     
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
            set_game_solo()
            pygame.display.flip()
            GAME_CLOCK.tick(FPS)
        
        #button_enterusername=menu.add.button(" Enter ",mainmenu)    
    #MULTIPLAYER
    def maingame_multiplayer():
        pygame.mouse.set_visible(False)
        global username
        username=button_username.get_value()
        run_main_game=True
        while run_main_game:
            for event in pygame.event.get():
                if event.type==QUIT :
                        pygame.quit()
                        sys.exit(0)
                if event.type == KEYUP:
                    if event.key == K_w:       
                        if hitbox.dead==False:
                            fire() 
                    if event.key == K_UP:      
                        if hitbox.dead==False:
                            fire_2() 
                    if event.key == K_TAB:
                        print("GAME EXITED!")
                        reset_game()
                        if gm.game_over:
                            game_over_stats_multiplayer()
                        run_main_game=False
            for Projectile in projectiles_group:
                Projectile.update()
            set_game_multiplayer()
            pygame.display.flip()
            GAME_CLOCK.tick(FPS)    
    #LEADERBOARDS  
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
    #MAIN MENU
    def mainmenu():
        menu_theme.widget_margin=(-600,0)
        global button_username
        if gm.game_over:
            game_over_stats(game_over)
        button_username=menu.add.text_input(" Enter Username : ",default="Player",maxchar=12)
        leaderboards()
        button_startgame=menu.add.button(" Singleplayer ",maingame_solo)
        button_leaderboards=menu.add.button(" Multiplayer ",maingame_multiplayer)
        menu.add.button(" Quit ",exit)
    #EXIT GAME
    def exit():
        pygame.quit()
        sys.exit(0)    

    #MAIN PROGRAM
        
    pygame.mouse.set_visible(False) #SET MOUSE VISIBILITY --> FALSE

    #MENU CUSTOMIZATION 
    menu_theme=pygame_menu.themes.THEME_DARK
    menu_theme.background_color=pygame_menu.BaseImage(LINK_ASSETS_BACKGROUND)
    menu_theme.title_font=FONT_MENU_TITLE
    menu_theme.title_font_color=COLOR_GREEN
    menu_theme.title_background_color=(0,0,0,0)
    menu_theme.widget_font=FONT_LCD
    menu_theme.widget_font_color=COLOR_GREEN
    menu_title="    -----DECK COMMANDER-----"
    menu=pygame_menu.Menu(menu_title,DISPLAY_WIDTH,DISPLAY_HEIGHT,theme=menu_theme)

    mainmenu()                                   #LOAD MAIN MENU
    mainmenuloop=menu.mainloop(DISPLAY_WINDOW)   #SET MAIN MENU LOOP
    
    print("QUIT!")
    game_over_stats(game_over)                   #DISPLAY GAME STATS

game() #CALL MAIN GAME