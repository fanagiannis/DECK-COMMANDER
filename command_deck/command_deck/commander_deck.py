import pygame
import sys,random

pygame.init()    
    #IMPORTS
from spaceship import Spaceship, Player2
from enemy import Enemy
   
   
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

    #GAME CAPTION

caption = pygame.display.set_caption('Deck Commander')

    #GAME BACKGROUND

planet = pygame.image.load('command_deck/command_deck/planet.png').convert_alpha()

planet_ = pygame.transform.scale(planet,(500,500))

planet2 =pygame.image.load('command_deck/command_deck/planet2.png').convert_alpha()
   
planet_2 = pygame.transform.scale(planet2,(500,500))     
           
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
    
    #CALCULATE HEALTH RATIO 
        
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(0,700,1280, 10, 100)    

    #FPS
Clock = pygame.time.Clock()

    #SPACESHIP
   
    #1
spaceship = Spaceship(x,y,screen_width,screen_height,speed,1) #spaceship obj
spaceship_group = pygame.sprite.GroupSingle() #Contains the sprite of the obj
spaceship_group.add(spaceship)
    
    #2
player2 = Spaceship(x,y,screen_width,screen_height,speed,2)#:::::Player2(x,y,screen_width,screen_height,speed):::::
player2_group  = pygame.sprite.GroupSingle() 
player2_group.add(player2)

    #ENEMY
enemy_ = Enemy(600,100)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy_)
print(enemy_group)        
    #GAME RUNNING
running  = True
direction = 'down'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        #UPDATING   
    spaceship_group.update()   

    enemy_group.update()

    player2_group.update()
        
        #DRAWING IN SCREEN
    
    screen.fill((0,0,0))   
    
    screen.blit(planet_,(1000,-50))
    
    screen.blit(planet_2,(-50,500))
    
    health_bar.draw(screen)

    spaceship_group.draw(screen,(screen_width,screen_height)) #draws the sprite
    
    player2_group.draw(screen,(screen_width,screen_height)) #draws the sprite

    spaceship_group.sprite.lazer_group.draw(screen)
        
    player2_group.sprite.lazer_group.draw(screen)
    
    enemy_group.draw(screen)
  
    pygame.display.update()
    
    #FPS
    Clock.tick(60)