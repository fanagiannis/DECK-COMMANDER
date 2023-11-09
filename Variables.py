import pygame

from Constants import DISPLAY_HEIGHT,DISPLAY_WIDTH
from Player import Player
from Scope import Aim 
from Spawner_Targets import Spawner
from Hitbox import Hitbox


ADS=Aim()

P=Player()

global run_game

run_main_game=True
run_game=False

hitbox = Hitbox(DISPLAY_HEIGHT,DISPLAY_WIDTH)

spawn_time=60
Target_spawn=Spawner(60)
Target_Damage=250

#global score_message_pos,lives_message_pos,game_over_message_pos,ammo_message_pos, ammo_no_message_pos
score_message_pos=(30,DISPLAY_HEIGHT-60)
lives_message_pos=(DISPLAY_WIDTH-175,DISPLAY_HEIGHT-35)
game_over_message_pos=(DISPLAY_WIDTH/2-75,DISPLAY_HEIGHT/2-75)
ammo_message_pos=(DISPLAY_WIDTH-175,DISPLAY_HEIGHT-75)
ammo_no_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-150)


score_value=100