import pygame

#+++++LINKS+++++

LINK_ASSETS_BASE_PC="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\DECK COMMANDER\\assets"
LINK_ASSETS_BASE_LAPTOP="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
LINK_ASSETS_BASE=LINK_ASSETS_BASE_PC
LINK_ASSETS_PLAYER=LINK_ASSETS_BASE+"\\Player.png"
LINK_ASSETS_CURSOR=LINK_ASSETS_BASE+"\\Aim.png"
LINK_ASSETS_AIMCURSOR=LINK_ASSETS_BASE+"\\AimBig.png"
LINK_ASSETS_BULLETS=LINK_ASSETS_BASE+"\\Bullet.png"
LINK_ASSETS_TARGET=LINK_ASSETS_BASE+"\\Enemy.png"
LINK_ASSETS_REPAIR=LINK_ASSETS_BASE+"\\Repair.png"
LINK_ASSETS_ROCKET=LINK_ASSETS_BASE+"\\Rocket.png"
LINK_ASSETS_BACKGROUND="assets\\Space.png"
LINK_ASSETS_SCREEN="assets\\Screen.png"
LINK_ASSETS_SCREEN2="assets\\Screen2.png"
LINK_ASSETS_SCREEN3="assets\\Screen3.png"
LINK_ASSETS_PLANET="assets\\Planet_8bit.png"
LINK_ASSETS_PLANET2="assets\\Planet2_8bit.png"
LINK_ASSETS_PLANET3="assets\\Planet3_8bit.png"

   #+++++DISPLAY+++++

DISPLAY_WIDTH=1280
DISPLAY_HEIGHT=720
DISPLAY_WINDOW=pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

    #+++++COLORS+++++

COLOR_BLACK=pygame.Color(0,0,0)
COLOR_WHITE=pygame.Color(255,255,255)
COLOR_GREY=pygame.Color(128,128,128)
COLOR_RED=pygame.Color(255,0,0)
COLOR_YELLOW=pygame.Color(255,255,0)
COLOR_GREEN=pygame.Color(5, 242, 68)

GAME_CLOCK=pygame.time.Clock()
FPS=45
