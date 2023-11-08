import pygame
import pygame_menu
import sys
from pygame.locals import *

from Variables import *
from Constants import *

pygame.init()

def set_difficulty(stage,difficulty):
  print("difficulty:1")

def game_start():
  #subprocess.Popen()
  print("Game Started ! ")

pygame.mouse.set_visible(False)

menu_theme=pygame_menu.themes.THEME_DARK
menu_theme.background_color=pygame_menu.BaseImage(LINK_ASSETS_BACKGROUND)
menu_theme.title_font=FONT_MENU_TITLE
menu_theme.title_font_color=COLOR_GREEN
menu_theme.title_background_color=(0,0,0,0)
menu_theme.widget_font=FONT_LCD
menu_theme.widget_font_color=COLOR_GREEN
#menu_theme.widget_margin=(-600,0)
#menu_theme.title_color=COLOR_GREEN
menu_title="    -----DECK COMMANDER-----"
menu=pygame_menu.Menu(menu_title,DISPLAY_WIDTH,DISPLAY_HEIGHT,theme=menu_theme)



button_startgame=menu.add.button(" Start Game ",game_start)

menu.add.text_input(" Username : ",default="Uknown Player")
menu.add.selector(" Difficulty : ",[("Hard",1),("Easy",2)],onchange=set_difficulty)

menu.add.button(" Quit ",pygame_menu.events.EXIT)

while True:
  for event in pygame.event.get():
    if event.type == QUIT :
      exit()

  menu.mainloop(DISPLAY_WINDOW)

run_menu=True
while run_menu:
    
    background=pygame.image.load(LINK_ASSETS_BACKGROUND)
    DISPLAY_WINDOW.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type==QUIT :
                pygame.quit()
                sys.exit(0)
        if event.type==KEYDOWN:
             pressed_key=pygame.key.get_pressed()
             if pressed_key[K_TAB]:
                  run_menu=False

    main_menu_title_text=FONT_MENU_TITLE.render(GAME_TITLE,True,COLOR_GREEN)
    main_menu_subtext=FONT_MENU_TITLE.render("----------------------------",True,COLOR_GREEN)
    main_menu_exit_text=FONT_BASIC.render(GAME_EXIT,True,COLOR_GREEN)

    text_sizex,text_sizey=main_menu_title_text.get_size()

    DISPLAY_WINDOW.blit(main_menu_title_text,(DISPLAY_WIDTH/2-text_sizex/2,DISPLAY_HEIGHT/2-300))
    DISPLAY_WINDOW.blit(main_menu_subtext,(DISPLAY_WIDTH/2-text_sizex/2,DISPLAY_HEIGHT/2-250))
    DISPLAY_WINDOW.blit(main_menu_subtext,(DISPLAY_WIDTH/2-text_sizex/2,DISPLAY_HEIGHT/2-350))
    DISPLAY_WINDOW.blit(main_menu_exit_text,(DISPLAY_WIDTH-200,DISPLAY_HEIGHT-30))
    pygame.draw.rect(DISPLAY_WINDOW,COLOR_GREEN,(500,500,200,100),1)

    pygame.display.flip()
    GAME_CLOCK.tick(FPS_MENU)

print("Game Exit Successful!")
pygame.quit()
sys.exit()

