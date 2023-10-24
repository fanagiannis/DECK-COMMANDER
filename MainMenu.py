import pygame
import sys
import random
import time
#from turtle import delay
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

#FPS 
game_fps=pygame.time.Clock()
FPS=60

#COLORS
color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

#DISPLAY WINDOW
display_width=1240
display_height=720
display_window= pygame.display.set_mode((display_width,display_height))

display_center=((display_width-(display_width/2)),(display_height-(display_height/2)))

display_window.fill(color_white)
pygame.display.set_caption("Main Menu")

while True:

    for event in pygame.event.get():
        if event.type==QUIT or pygame.key.get_pressed()==[K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
    
    display_window.fill(color_grey)
    pygame.display.update()
    game_fps.tick(FPS)
