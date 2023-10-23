import pygame
import sys
import random
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
display_window.fill(color_white)
pygame.display.set_caption("Test")

#FPS 
game_fps=pygame.time.Clock()
FPS=60

#SCALES
player_scale=10
enemy_scale=5

#CLASSES

#ENEMY
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:\\ΦΩΤΟ\\aaa.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,display_width-40),0) #randomise
    def movement(self):
        enemy_speed=10
        self.rect.move_ip(0,enemy_speed)
        if(self.rect.top>600):
            self.rect.top=0
            self.rect.center = (random.randint(30,370),0)
    
    def spawn(self,surface):
        surface.blit(self.image,self.rect)

    def destroy(self):
        self.kill()

#PLAYER

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:\\ΦΩΤΟ\\mqdefault__1_-removebg-preview.png")
        self.rect=self.image.get_rect()
        self.rect.center=(160,520)

    #PLAYER_MOVEMENT
    
    def movement(self):
        pressed_keys=pygame.key.get_pressed()

        #SPRINT 
    
        if pressed_keys[K_LSHIFT]:
            player_speed=10
        else:
            player_speed=5

        #WALK

        if self.rect.top>0:
            if pressed_keys[K_w]:
                self.rect.move_ip(0,-player_speed) #movecmd
        if self.rect.bottom<display_height:
            if pressed_keys[K_s]:
                self.rect.move_ip(0,player_speed)
        if self.rect.right < display_width:
            if pressed_keys[K_d]:
                self.rect.move_ip(player_speed,0) 
        if self.rect.left > 0:
            if pressed_keys[K_a]:
                self.rect.move_ip(-player_speed,0)

        if pressed_keys[K_SPACE]:
            print("FIRE")

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
    E.movement()
    
    #BACKGROUND

    display_window.fill(color_white)

    #SPAWN

    P.spawn(display_window)
    E.spawn(display_window)

    pygame.display.update()
    game_fps.tick(FPS)

    #GAME OVER

    if P.rect.colliderect(E.rect):
        #P.destroy()
        print("GAME OVER")
        exit()
        

    