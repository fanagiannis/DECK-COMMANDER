import pygame
import sys
import random
import time
#from turtle import delay
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

#COLORS
color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

#DISPLAY WINDOW
display_width=1240
display_height=720
display_window= pygame.display.set_mode((display_width,display_height))

display_center=((display_width-(display_width/2)),(display_height-(display_height/2)))

display_window.fill(color_white)
pygame.display.set_caption("Test")

#GAME OVER
font=pygame.font.SysFont("Arial",30)
game_over_screen=pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Game_Over.png")

#FPS 
game_fps=pygame.time.Clock()
FPS=60

#SCALES
player_scale=10
enemy_scale=5

#FUNCTIONS

#def get_display_center(display):
#    x,y=pygame.display.get_window_size()
#    center=(x//2 - display.get_width()//2,)
#    display_center=(display_width-(display_width/2),display_height-(display_height/2))

def destroy(Actor):
    Actor.rect.move_ip(display_width+500,display_height+500)
    Actor.kill()

def message(txt,font,txt_color,pos_x,pos_y):
    display_text=font.render(txt,True,txt_color)
    display_window.blit(display_text,(pos_x,pos_y))
    

#CLASSES

#ENEMY
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,display_width-40),0) #randomise
        self.speed=5
    
    def spawn(self,surface):
        surface.blit(self.image,self.rect)

    

#PLAYER

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=(160,520)
        self.speed=5
        self.maxspeed=10
        self.stamina=100

    #PLAYER_MOVEMENT
    
    def movement(self):
       
        pressed_keys=pygame.key.get_pressed()

        #    self.speed = self.maxspeed
        #else:
        #    self.speed = 5

        #WALK

        if self.rect.top>0:
            if pressed_keys[K_w]:
                self.rect.move_ip(0,-self.speed) #movecmd
        if self.rect.bottom<display_height:
            if pressed_keys[K_s]:
                self.rect.move_ip(0,self.speed)
        if self.rect.right < display_width:
            if pressed_keys[K_d]:
                self.rect.move_ip(self.speed,0) 
        if self.rect.left > 0:
            if pressed_keys[K_a]:
                self.rect.move_ip(-self.speed,0)

        if pressed_keys[K_SPACE]:
            time.sleep(0.1)
            print("FIRE")

    def stop(self):
        self.speed = 0  
    
    def sprint(self):
        if self.speed>0 :
            self.speed = self.maxspeed

    def destroy(self):
        self.remove()

    #PLAYER_SPAWN

    def spawn(self,surface):
        surface.blit(self.image,self.rect)

P=Player()
E=Enemy()
       

while True:

    for event in pygame.event.get():
        if event.type==QUIT or pygame.key.get_pressed()==[K_ESCAPE]:
            pygame.quit()
            sys.exit(0)

    #INITIALIZE

    P.movement()
 #  E.movement()
    
    #BACKGROUND

    display_window.fill(color_white)

    #SPAWN

    P.spawn(display_window)
    E.spawn(display_window)

    pygame.display.update()
    game_fps.tick(FPS)

    #GAME OVER

    if P.rect.colliderect(E.rect):
         message("GAME OVER ! ",font,color_black,220,150)
         destroy(E)
         P.stop()
        
    #     game_over(P)
    #    print("GAME OVER")
    #    exit()
        

    