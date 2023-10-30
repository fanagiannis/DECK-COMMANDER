import pygame
import sys
from pygame.locals import *
from pygame.sprite import *

pygame.init()

pygame.display.set_caption("GAME V0.0")

game_clock=pygame.time.Clock()
FPS=60

    #+++++DISPLAY+++++

display_width=1280
display_height=720
display_window=pygame.display.set_mode((display_width,display_height))

    #+++++LINKS+++++

link_assets_base_pc="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
link_assets_base_laptop="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
link_assets_base=link_assets_base_laptop
link_assets_player=link_assets_base+"\\Player.png"
link_assets_cursor=link_assets_base+"\\Aim.png"
link_assets_aimcursor=link_assets_base+"\\AimBig.png"
link_assets_bullets=link_assets_base+"\\Bullet.png"

    #+++++COLORS+++++

color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

while True:

    display_window.fill(color_white)

    for event in pygame.event.get():
        if event.type==QUIT :
            pygame.exit()
            sys.exit(0)
    
    pygame.display.update()
    game_clock.tick(FPS)