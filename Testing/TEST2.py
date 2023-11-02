import pygame
import math
import sys

from pygame.locals import *

pygame.init()

#COLORS
color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

LINK_ASSETS_BASE="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\assets"
LINK_ASSETS_ROCKET=LINK_ASSETS_BASE+"\\Rocket.png"
LINK_ASSETS_PLAYER=LINK_ASSETS_BASE+"\\Player.png"

#DISPLAY WINDOW
display_width=1240
display_height=720
display_window= pygame.display.set_mode((display_width,display_height))

display_center=((display_width-(display_width/2)),(display_height-(display_height/2)))

display_window.fill(color_white)
pygame.display.set_caption("Test")

#GAME OVER
font=pygame.font.SysFont(None,30,bold=True)
#game_over_screen=pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Game_Over.png")

#FPS 
game_fps=pygame.time.Clock()
FPS=60


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(LINK_ASSETS_PLAYER)
        self.rect=self.image.get_rect()
        self.posx=10
        self.posy=10
        self.mouse_posx,self.mouse_posy=pygame.mouse.get_pos()
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
        self.speed=10
        self.shoot=False
        self.trajectory=0
    
    def movement(self):
        
        m=pygame.mouse.get_pressed()
        if m[0] and not self.trajectory:
            self.angle = math.atan2(self.mouse_posy-self.posy,self.mouse_posx-self.posx)
            
            self.trajectory=math.hypot(self.mouse_posy-self.posy,self.mouse_posx-self.posx)
            self.trajectory=int(self.trajectory)

            self.dx=math.cos(self.angle)*self.speed
            self.dy=math.sin(self.angle)*self.speed

            self.image_rotated=pygame.transform.rotate(self.image,self.angle)
            self.rect_rotated=self.image_rotated.get_rect()

            #self.image=self.image_rotated
            #self.rect=self.rect_rotated

            #self.posx=self.mouse_posx
            #self.posy=self.mouse_posy
        if self.trajectory:
            self.trajectory-=1
            self.posx+=self.dx
            self.posy+=self.dy
        self.rect.center=self.pos
        if self.posx>display_width or self.posy>display_height or self.posy<0 or self.posx<0:
            self.shoot=False

    def update(self):
        
        if event.type==MOUSEBUTTONUP:
            if event.button==1:
                self.shoot=True
        if self.shoot:
            self.movement()
        print(self.shoot)


Proj=Projectile()

while True:

    display_window.fill(color_white)

    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit(0)

    Proj.update()

    display_window.blit(Proj.image,Proj.rect)
     
 
    pygame.display.update()
    game_fps.tick(FPS)