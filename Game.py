import pygame
import sys
import random
import time
import math
#from turtle import delay
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

pygame.display.set_caption("(Local) Two Player Collision Game")


    #+++++COLORS+++++

color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

    #+++++DISPLAY WINDOW+++++

display_width=1240
display_height=720
display_window= pygame.display.set_mode((display_width,display_height))
display_center=((display_width-(display_width/2)),(display_height-(display_height/2)))

    #+++++GAME OVER+++++
font=pygame.font.SysFont(None,30,bold=True)
    #game_over_screen=pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Game_Over.png")

    #+++++FPS+++++ 
game_fps=pygame.time.Clock()
FPS=60
