import pygame
import pygame_menu

from pygame.locals import *

pygame.init()

MAIN_MENU_DISPLAY_WIDTH=600
MAIN_MENU_DISPLAY_HEIGHT=500
MAIN_MENU_DISPLAY_WINDOW=pygame.display.set_mode((MAIN_MENU_DISPLAY_WIDTH,MAIN_MENU_DISPLAY_HEIGHT))

default_username="A"
default_password="11111"

#FUNCTIONS

def set_difficulty(stage,difficulty):
  print("difficulty:1")

def game_start():
  if Username==default_username :#and Password==default_password:
    print("Correct")
    menu.add.button(" Quit ",pygame_menu.events.EXIT)
  else :
    print("Wrong Credentials")
  pass
  #subprocess.Popen()

menu=pygame_menu.Menu("Main Menu",MAIN_MENU_DISPLAY_WIDTH,MAIN_MENU_DISPLAY_HEIGHT,theme=pygame_menu.themes.THEME_BLUE)
Username=menu.add.text_input("Username : ")
Password=menu.add.text_input("Password : ")
menu.add.button(" Start Game ",game_start)


while True:

  for event in pygame.event.get():
    if event.type == QUIT :
      exit()

  menu.mainloop(MAIN_MENU_DISPLAY_WINDOW)