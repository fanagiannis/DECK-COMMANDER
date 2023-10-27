import pygame
import sys
import random
import time
import math
#from turtle import delay
from pygame.locals import *
from pygame.sprite import _Group, Group 

pygame.init()

pygame.display.set_caption("GAME")

clock=pygame.time.Clock()

    #+++++COLORS+++++

color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

    #+++++DISPLAY WINDOW+++++

display_width=1240
display_height=720
display_window= pygame.display.set_mode((display_width,display_height))
#display_center=((display_width-(display_width/2)),(display_height-(display_height/2)))

    #+++++GAME OVER+++++
font=pygame.font.SysFont(None,30,bold=True)

    #+++++FPS+++++ 
game_fps=pygame.time.Clock()
FPS=60

    #+++++FUNCTIONS+++++
def game_init():
    global SpawnPoints
    SpawnPoints=[(160,220),(560,340)]
    pass

def spawner():
    pass

    #+++++CLASSES+++++
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.transform.ro
        self.pos=SpawnPoints[1]

while True:
    display_window.fill(color_white)   #SET BACKGROUND

    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit(0)

    print (SpawnPoints)

    pygame.display.update()
    game_fps.tick(FPS)