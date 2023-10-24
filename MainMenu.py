import pygame
import pygame_menu
import sys
import random
import time
#import subprocess 
from pygame.locals import *
#from CollisionGame import *

pygame.init()

#COLORS
color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

#DISPLAY WINDOW
display_width=1240
display_height=720
display_window=pygame.display.set_mode((display_width,display_height))

#FPS 
game_fps=pygame.time.Clock()
FPS=60

#FUNCTIONS

def set_difficulty(stage,difficulty):
  print("difficulty:1")

def game_start():
  #subprocess.Popen(py)
  print("Game Started ! ")

#DIFFICULTY 



#MENU

menu=pygame_menu.Menu("Main Menu",600,500,theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input(" Username : ",default="Uknown Player")
menu.add.selector(" Difficulty : ",[("Hard",1),("Easy",2)],onchange=set_difficulty)
menu.add.button(" Start Game ",game_start)
menu.add.button(" Quit ",pygame_menu.events.EXIT)

while True:
  for event in pygame.event.get():
    if event.type == QUIT :
      exit()

  menu.mainloop(display_window)