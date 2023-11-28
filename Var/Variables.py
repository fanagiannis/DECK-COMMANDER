import pygame

from Var.Constants import DISPLAY_HEIGHT,DISPLAY_WIDTH
from Classes.Player import Player
from Classes.Scope import Aim 
from Classes.Spawner_Targets import Spawner
from Classes.Hitbox import Hitbox

ADS=Aim()

global P
P=Player()
playerpositionx,playerpositiony = P.posx,P.posy
gunpos=P.pos

projectiles_group=pygame.sprite.Group()
hit=False
global run_game

run_main_game=True
run_game=False

hitbox = Hitbox(DISPLAY_HEIGHT,DISPLAY_WIDTH)

global difficulty,difficulty_index,game_difficulty,username
difficulty=[("Easy",0),("Normal",1),("Hard",2)]
difficulty_index=2

username="Uknown Player"

if difficulty[difficulty_index]==("Easy",0): 
    spawn_time=60
    Damage=100
elif difficulty[difficulty_index]==("Medium",1): 
    spawn_time=35
    Damage=250
elif difficulty[difficulty_index]==("Hard",2): 
    spawn_time=25
    Damage=350


Target_spawn=Spawner(spawn_time)
Target_Damage=Damage

#global score_message_pos,lives_message_pos,game_over_message_pos,ammo_message_pos, ammo_no_message_pos
score_message_pos=(30,DISPLAY_HEIGHT-30)
lives_message_pos=(DISPLAY_WIDTH-175,DISPLAY_HEIGHT-35)
game_over_message_pos=(DISPLAY_WIDTH/2-75,DISPLAY_HEIGHT/2-75)
ammo_message_pos=(DISPLAY_WIDTH-175,DISPLAY_HEIGHT-75)
ammo_no_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-150)
username_pos=(30,DISPLAY_HEIGHT-90)
difficulty_pos=(30,DISPLAY_HEIGHT-60)


score_value=100