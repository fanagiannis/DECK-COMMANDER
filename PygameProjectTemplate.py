import pygame
import pygame_menu
import sys
import random
import time
from pygame.locals import *

pygame.init()

#COLORS
color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

#DISPLAY WINDOW
display_width=600
display_height=400
display_window=pygame.display.set_mode((display_width,display_height))

#FPS 
game_fps=pygame.time.Clock()
FPS=60

while True:
  for event in pygame.event.get():
    if event.type == QUIT :
      exit()