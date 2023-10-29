import pygame

pygame.init()

pygame.display.set_caption("Pygame 2D Shooter")

clock=pygame.time.Clock()


    #+++++LINKS+++++

link_assets_base="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
link_assets_player=link_assets_base+"\\Player.png"
link_assets_cursor=link_assets_base+"\\Aim.png"
link_assets_aimcursor=link_assets_base+"\\AimBig.png"
link_assets_bullets=link_assets_base+"\\Bullet.png"

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