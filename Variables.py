import pygame

from Constants import DISPLAY_HEIGHT,DISPLAY_WIDTH
from Player import Player
from Scope import Aim 
from Spawner_Targets import Spawner
from Hitbox import Hitbox
from Projectiles import Projectile

ADS=Aim()

#T=Target() 
#Target_Group=pygame.sprite.Group()
#Target_Group.add(T)

P=Player()

Proj=Projectile(P.posx,P.posy)

hitbox = Hitbox(DISPLAY_HEIGHT,DISPLAY_WIDTH)

spawn_time=60
Target_spawn=Spawner(60)
Target_Damage=250

#global score_message_pos,lives_message_pos,game_over_message_pos,ammo_message_pos, ammo_no_message_pos
score_message_pos=(30,DISPLAY_HEIGHT-50)
lives_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-50)
game_over_message_pos=(DISPLAY_WIDTH/2-75,DISPLAY_HEIGHT/2-75)
ammo_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-100)
ammo_no_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-150)

score_value=100