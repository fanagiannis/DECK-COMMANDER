import pygame

from Constants import *
from Player import Player
from Scope import Aim 
from Target import Target



ADS=Aim()


T=Target() 
Target_Group=pygame.sprite.Group()
Target_Group.add(T)


P=Player()

#global score_message_pos,lives_message_pos,game_over_message_pos,ammo_message_pos, ammo_no_message_pos
score_message_pos=(30,DISPLAY_HEIGHT-50)
lives_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-50)
game_over_message_pos=(DISPLAY_WIDTH/2-75,DISPLAY_HEIGHT/2-75)
ammo_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-100)
ammo_no_message_pos=(DISPLAY_WIDTH-150,DISPLAY_HEIGHT-150)

score_value=100