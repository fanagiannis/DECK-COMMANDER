import pygame

pygame.init()

try:
    GAME_TITLE="-------DECK COMMANDER-------"
    GAME_EXIT="Press TAB to exit"


    #+++++LINKS+++++

    LINK_ASSETS_BASE_PC="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\DECK COMMANDER\\assets"
    LINK_ASSETS_BASE_LAPTOP="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
    LINK_ASSETS_BASE=LINK_ASSETS_BASE_PC
    LINK_ASSETS_PLAYER="assets\\Player.png"
    LINK_ASSETS_CURSOR="assets\\Aim.png"
    LINK_ASSETS_AIMCURSOR="assets\\AimBig.png"
    LINK_ASSETS_BULLETS="assets\\Bullet.png"
    LINK_ASSETS_TARGET="assets\\Enemy.png"
    LINK_ASSETS_TARGETEXPLOSION="assets\\Explosion.png"
    LINK_ASSETS_REPAIR="assets\\Repair.png"
    LINK_ASSETS_ROCKET="assets\\Rocket.png"
    LINK_ASSETS_BACKGROUND="assets\\Space.png"
    LINK_ASSETS_SCREEN="assets\\Screen.png"
    LINK_ASSETS_SCREEN2="assets\\Screen2.png"
    LINK_ASSETS_SCREEN3="assets\\Screen3.png"
    LINK_ASSETS_PLANET="assets\\Planet4.png"#Planet_8bit.png"
    LINK_ASSETS_PLANET2="assets\\Planet2_8bit.png"
    LINK_ASSETS_PLANET3="assets\\Planet3_8bit.png"
    LINK_ASSETS_SPACESHIP="assets\\Spaceship.png"
    LINK_ASSETS_SPACESHIP2="assets\\Spaceship2.png"
    LINK_ASSETS_GUN="assets\\Gun.png"
    LINK_ASSETS_BASE="assets\\Base.png"
    #+++++FONT+++++
    FONT_LCD="Fonts\\pixel_lcd_7.ttf"
    FONT_BASIC=pygame.font.Font(FONT_LCD,15)
    FONT_STATS=pygame.font.Font(FONT_LCD,25)
    FONT_GAME_OVER=pygame.font.Font(FONT_LCD,40)
    FONT_MENU_TITLE=pygame.font.Font(FONT_LCD,60)

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
    FPS_MENU=30
    FPS=60

except pygame.error as e:   
    print(f"Error in assets loading : {e}")

