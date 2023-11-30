import pygame
import sys
import random
import math
pygame.init()    
    #IMPORTS
from spaceship import Spaceship
from aim import Aim

    #X,Y AND SPEED
speed = 9
x = 640
y = 360
    #COLORS
white = [255,255,255]
black = [0, 0, 0]

    #SCREEN PROPERTIES AND BASICS
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.mouse.set_visible(False) #we can't see the mouse
caption = pygame.display.set_caption('Deck Commander')

    #STARS
stars_list = []
for i in range(30):
    x = random.randrange(0,1280)
    y = random.randrange(0, 1280)
    stars_list.append([x, y])
    
    #HEALTH
class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
    
    def draw(self, surface):
    #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(10,10, 300, 20, 100)    
    

    #FPS
Clock = pygame.time.Clock()

    #SPACESHIP
spaceship = Spaceship(x,y,screen_width, screen_height,speed) #spaceship obj
spaceship_group = pygame.sprite.GroupSingle() #Contains the sprite of the obj
spaceship_group.add(spaceship)
spaceship = pygame.transform.rotate(screen,0)


    #AIM
aim = Aim(x,y,screen_width,screen_height,speed)
aim_group = pygame.sprite.Group()
aim_group.add(aim)

running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        #UPDATING   
    aim_group.update()
    spaceship_group.update()   
    
        #DRAWING
    screen.fill((0,0,0))
    
    for i in range(len(stars_list)):
        pygame.draw.circle(screen, white, stars_list[i], 2)
        stars_list[i][1] += 1
        if stars_list[i][1] > 700:
            y = random.randrange(-50, -10)
            stars_list[i][1] = y
            x = random.randrange(0, 1280)
            stars_list[i][0] = x
    
    health_bar.draw(screen)
    
    spaceship_group.draw(screen,(aim.x,aim.y)) #draws the sprite
    
    spaceship_group.sprite.lazer_group.draw(screen)
    
    aim_group.draw(screen)#draws Aim
    
    pygame.display.update()
    Clock.tick(60)