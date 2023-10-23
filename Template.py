import pygame
import sys
import random
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

#COLORS
color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

#DISPLAY WINDOW
display_width=400
display_height=600
display_window= pygame.display.set_mode((display_width,display_height))
display_window.fill(color_white)
pygame.display.set_caption("Test")

#FPS 
game_fps=pygame.time.Clock()

#OBJECTS
#object1=pygame.rect((20,50),(50,100))
#object2=pygame.rect((10,10),(100,100))

#CLASSES

#ENEMY
class Enemy(pygame.sprite.Sprite):
    global enemy_speed
    enemy_speed=10
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:\\ΦΩΤΟ\\SHREKORLOS.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,display_width-40),0) #randomiser
    def movement(self):
        self.rect.move_ip(0,enemy_speed)
        if(self.rect.top>600):
            self.rect.top=0
            self.rect.center = (random.randint(30,370),0)
    
    def spawn(self,surface):
        surface.blit(self.image,self.rect)

#PLAYER

class Player(pygame.sprite.Sprite):
    global player_speed
    global player_quit
    player_speed=50
    player_quit=False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:\\ΦΩΤΟ\\mqdefault__1_-removebg-preview.png")
        self.rect=self.image.get_rect()
        self.rect.center=(160,520)

    #PLAYER_MOVEMENT

    def movement(self):
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[K_w]:
            self.rect.move_ip(0,-player_speed)
        if pressed_keys[K_s]:
            self.rect.move_ip(0,player_speed)
        if self.rect.right< display_width:
            if pressed_keys[K_d]:
                self.rect.move_ip(player_speed,0) #movecmd
        if self.rect.left>0:
            if pressed_keys[K_a]:
                self.rect.move_ip(-player_speed,0)
        
        

    #PLAYER_SPAWN

    def spawn(self,surface):
        surface.blit(self.image,self.rect)

P=Player()
E=Enemy()
       

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit(0)

    #INITIALIZE

    P.movement()
    E.movement()
    
    #BACKGROUND

    display_window.fill(color_white)


    #SPAWN

    P.spawn(display_window)
    E.spawn(display_window)

    pygame.display.update()
    game_fps.tick(60)

    