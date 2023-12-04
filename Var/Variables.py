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

score_message_pos=(30,30)
hp_message_pos=(DISPLAY_WIDTH-175,30)
game_over_message_pos=(DISPLAY_WIDTH/2-75,DISPLAY_HEIGHT/2-75)
energy_message_pos=(DISPLAY_WIDTH-175,60)
energy_no_message_pos=(DISPLAY_WIDTH-150,150)
username_pos=(DISPLAY_WIDTH-180,DISPLAY_HEIGHT-60)
gameround_pos=(30,60)

score_value=100