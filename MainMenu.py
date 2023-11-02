import pygame
import pygame_menu

from pygame.locals import *
from Constants import *

pygame.init()

#FUNCTIONS

def set_difficulty(stage,difficulty):
  print("difficulty:1")

def game_start():
  pass
  #subprocess.Popen()

menu=pygame_menu.Menu("Main Menu",600,500,theme=pygame_menu.themes.THEME_BLUE)

#menu.add.text_input(" Username : ",default="Uknown Player")
#menu.add.selector(" Difficulty : ",[("Hard",1),("Easy",2)],onchange=set_difficulty)
menu.add.button(" Start Game ",game_start)
menu.add.button(" Quit ",pygame_menu.events.EXIT)

while True:
  for event in pygame.event.get():
    if event.type == QUIT :
      exit()

  menu.mainloop(DISPLAY_WINDOW)