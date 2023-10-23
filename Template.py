import pygame
import sys
import random
from pygame.locals import *
from pygame.sprite import _Group 

pygame.init()

#COLORS
color_black=pygame.color(0,0,0)
color_white=pygame.color(255,255,255)
color_grey=pygame.color(128,128,128)
color_red=pygame.color(255,0,0)

#DISPLAY WINDOW
display_width=400
display_height=600
display_window= pygame.display.set_mode((display_width,display_height))
display_window.fill(color_white)
pygame.display.set_caption("Test")

#FPS 
game_fps=pygame.time.clock()

#OBJECTS
object1=pygame.rect((20,50),(50,100))
object2=pygame.rect((10,10),(100,100))

#CLASSES

#ENEMY
class Enemy(pygame.sprite.Sprite):
    global enemy_speed
    enemy_speed=10
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:\ΦΩΤΟ\SHREKORLOS")
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
    player_speed=5
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:\ΦΩΤΟ\mqdefault__1_-removebg-preview")
        self.rect=self.image.get_rect()
        self.rect.center=(160,520)

    #PLAYER_MOVEMENT

    def movement(self):
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(player_speed,0) #movecmd
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-player_speed,0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-player_speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,player_speed)

    #PLAYER_SPAWN

    def spawn(self,surface):
        surface.blit(self.image,self.rect)

P=Player()
E=Enemy()
       

while True:
    for event in pygame.event.get():
        if event.type()==QUIT:
            pygame.quit()
            sys.exit()

    #INITIALIZE

    P.update()
    E.movement()
    
    #BACKGROUND

    display_window.fill(color_white)

    #SPAWN

    P.spawn(display_window)
    E.spawn(display_window)

    pygame.display.update()
    game_fps.tick(60)

    