import pygame

from Var.Constants import DISPLAY_HEIGHT,DISPLAY_WIDTH
from Classes.Player import Player
from Classes.Scope import Aim 
from Classes.Spawner_Targets import Spawner
from Classes.Hitbox import Hitbox
from Classes.Gamemode import Gamemode

ADS=Aim()                                                       #SCOPE OBJECT DECLARATION

global P,gm,Target_spawn
P=Player(1)
global P2
P2=Player(2)                                                    #PLAYER OBJECT DECLARATION

gunpos=P.pos                                                    # GUN POSITION SET
gunpos_2=P2.pos                                                 # GUN 2 POSITION SET

gm=Gamemode()                                                   #GAMEMODE OBJECT DECLARATION  
Target_spawn=Spawner(gm.t_spawn_time,gm.t_Damage,gm.t_speed)    #ENEMY SPAWNER DECLARATION

projectiles_group=pygame.sprite.Group()                         #SET PROJECTILE GROUP     
hit=False                                                       #//CUT//

global run_game,run_main_game,run_main_menu,game_over,multiplayer           #BASIC BOOLEANS TO RUN THE GAME
run_main_menu=True                                              
run_main_game=True
run_game=False
game_over=False
multiplayer=False

global score_live,gameround_live

#HITBOX

hitbox = Hitbox(DISPLAY_HEIGHT,DISPLAY_WIDTH)                   #ALLY OBJECT DECLARATION (REVERSE!)

#UI

    #UI POSITIONS
ui_left_posx=30
ui_posy=15
ui_right_posx=DISPLAY_WIDTH-220

    #UI LEFT
score_message_pos=(ui_left_posx,ui_posy*2)
gameround_pos=(ui_left_posx,ui_posy*3)
multiplayer_gameround_pos=(ui_left_posx,ui_posy*5)

P2_score_message_pos=(ui_left_posx,ui_posy*4)
P2_energy_message_pos=(ui_right_posx,ui_posy*3)

    #UI RIGHT
hp_message_pos=(ui_right_posx,ui_posy)
energy_message_pos=(ui_right_posx,ui_posy*2)

energy_no_message_pos=(ui_right_posx,100)
energy_no_message_pos2=(ui_right_posx,130)
username_pos=(ui_left_posx,ui_posy)

    #GAME OVER POS
game_over_message_pos=(DISPLAY_WIDTH/2-125,DISPLAY_HEIGHT/2-75)
game_over_message_stats_pos=(DISPLAY_WIDTH/2-275,DISPLAY_HEIGHT/2)
game_over_message_stats_pos2=(DISPLAY_WIDTH/2-275,DISPLAY_HEIGHT/2+100)
game_over_return_mes_pos=(DISPLAY_WIDTH/2-200,ui_posy)

    #SCREEN POS
screen1_pos=(DISPLAY_WIDTH-200,0)
screen2_pos=(0,0)

score_value=100


