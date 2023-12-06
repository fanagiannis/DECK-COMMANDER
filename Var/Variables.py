import pygame

from Var.Constants import DISPLAY_HEIGHT,DISPLAY_WIDTH
from Classes.Player import Player
from Classes.Scope import Aim 
from Classes.Spawner_Targets import Spawner
from Classes.Hitbox import Hitbox
from Classes.Gamemode import Gamemode

ADS=Aim()

global P,gm,Target_spawn
P=Player()
gunpos=P.pos
gm=Gamemode()
Target_spawn=Spawner(gm.t_spawn_time,gm.t_Damage,gm.t_speed)

projectiles_group=pygame.sprite.Group()
hit=False
global run_game

run_main_game=True
run_game=False

hitbox = Hitbox(DISPLAY_HEIGHT,DISPLAY_WIDTH)

#UI

    #UI POSITIONS
ui_left_posx=30
ui_posy=25
ui_right_posx=DISPLAY_WIDTH-175

    #UI LEFT
score_message_pos=(ui_left_posx,ui_posy)
gameround_pos=(ui_left_posx,ui_posy*2)

    #UI RIGHT
hp_message_pos=(ui_right_posx,ui_posy)
energy_message_pos=(ui_right_posx,ui_posy*2)

energy_no_message_pos=(DISPLAY_WIDTH-150,150)
username_pos=(DISPLAY_WIDTH-180,DISPLAY_HEIGHT-60)

    #GAME OVER POS
game_over_message_pos=(DISPLAY_WIDTH/2-125,DISPLAY_HEIGHT/2-75)
game_over_message_stats_pos=(DISPLAY_WIDTH/2-300,DISPLAY_HEIGHT/2)

    #SCREEN POS
screen1_pos=(DISPLAY_WIDTH-200,0)
screen2_pos=(0,0)

score_value=100