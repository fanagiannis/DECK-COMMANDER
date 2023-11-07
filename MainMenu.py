import pygame
import pygame_menu
import sys
from pygame.locals import *

from Variables import *
from Constants import *

pygame.init()


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

    pygame.display.flip()
    GAME_CLOCK.tick(FPS_MENU)

print("Game Exit Successful!")
pygame.quit()
sys.exit()

