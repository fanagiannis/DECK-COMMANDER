import pygame
import sys
import random
import time
#from turtle import delay
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

#PATHS
link_pc="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON"
link_laptop="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON"
link_op=link_laptop

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

#display_window.fill(color_white)
pygame.display.set_caption("(Local) Two Player Collision Game")

Players=[]
SpawnPoints=[(160,220),(1060,220),(1060,520)]
MaxPlayers=2
Multiplayer=True

#GAME OVER
font=pygame.font.SysFont(None,30,bold=True)
#game_over_screen=pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Game_Over.png")

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

def find_mouse_pos():
    mouse_pos=pygame.mouse.get_pos()
    #print(mouse_pos)
    return mouse_pos

def destroy(Actor):
    Actor.rect.move_ip(display_width+500,display_height+500)
    Actor.kill()

def message(txt,txt_color,pos_x,pos_y):
    display_text=font.render(txt,True,txt_color)
    display_window.blit(display_text,(pos_x,pos_y))


def map(image):
    background=pygame.image.load(image)
    display_width,display_height=background.get_size()
    #display_window= pygame.display.set_mode((display_width,display_height))
    display_window.blit(background,(0,0))

def set_players(Player):
    Player.player_count()

    
    

#CLASSES

#AIM

class Aim(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(link_op+"\\Aim.png")
        self.rect=self.image.get_rect()
        self.rect.center=find_mouse_pos()
        self.IsAiming=False
    def spawn(self,surface):
        surface.blit(self.image,self.rect)
    def move(self):
        if event.type==MOUSEMOTION :
            self.rect.center=find_mouse_pos()
    def aiming(self,surface,Player):
        if self.IsAiming==False:
            print("AIM")
            self.image = pygame.image.load(link_op+"\\Aim2.png")
            Player.speed=1
            self.IsAiming=True
            surface.blit(self.image,self.rect)
        elif self.IsAiming== True:
            print("NO AIM")
            self.image = pygame.image.load(link_op+"\\Aim.png")
            Player.speed=5
            self.IsAiming=False
            surface.blit(self.image,self.rect)
        
        


#ENEMY

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(link_op+"\\Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randrange(40,display_width-40),random.randrange(40,display_height-40)) #randomise
        self.speed=5

    def teleport(self):
        enemy_speed=10
        oldposx,oldposy=self.rect.center
        randpos=(random.randrange(40,display_width-100)-oldposx,random.randrange(40,display_height-100)-oldposy)
        print(randpos)
        self.rect.center(randpos)
        if(self.rect.top>600):
            self.rect.top= 0
        #if self.rect.
    
    def spawn(self,surface):
        surface.blit(self.image,self.rect)

    

#PLAYER

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(link_op+"\\Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=SpawnPoints[len(Players)]
        self.name="Player"
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
        if self.name==Players[0]:

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
        
        else:
            if self.rect.top>0:
                if pressed_keys[K_UP]:
                    self.rect.move_ip(0,-self.speed) #movecmd
            if self.rect.bottom<display_height:
                if pressed_keys[K_DOWN]:
                    self.rect.move_ip(0,self.speed)
            if self.rect.right < display_width:
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(self.speed,0) 
            if self.rect.left > 0:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-self.speed,0)
        

        #if pressed_keys[K_SPACE]:
        #    time.sleep(0.1)
        #    print("FIRE")
    def shoot(self):
        mousepos=pygame.mouse.get_pos()
        rand_string=["BANG","BING","BONG"]
        print(rand_string[random.randint(0,2)],mousepos)


    def stop(self):
        self.speed = 0  
    
    def sprint(self):
        if self.speed>0 :
            self.speed = self.maxspeed

    def destroy(self):
        self.remove()

    #PLAYER_SPAWN

    def player_count(self):
        if len(Players)==1:
            Players.append(self.name)
        else:
            self.name="Player"+str(len(Players)+1)
            Players.append(self.name)
        print(Players)

    def check_collision_Object(self,rect):
        if self.rect.colliderect(rect):
            self.stop()
            return True

       
    def spawn(self,surface):
        surface.blit(self.image,self.rect)

map1="D:\\ΦΩΤΟ\\darksouls.jpg"
map2="D:\\ΦΩΤΟ\\Rodos.jpg"
P=Player()
set_players(P)
if Multiplayer:
    P2=Player()
    set_players(P2)

HUD_AIM=Aim()
E=Enemy()

pygame.mouse.set_visible(False)

while True:

#BACKGROUND

    display_window.fill(color_white)
    for event in pygame.event.get():
        if event.type==QUIT or pygame.key.get_pressed()==[K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
        #if event.type==pygame.KEYDOWN:
            #key_down=pygame.key.get_pressed()
            #if key_down[K_SPACE]:
               # P.shoot()
        if event.type==pygame.MOUSEBUTTONUP:
             if event.button == 1: #RIGHT KEY
                P.shoot()
        if event.type==pygame.MOUSEMOTION:
            find_mouse_pos()
            HUD_AIM.move()
        if event.type==MOUSEBUTTONDOWN:
            if event.button == 3: #RIGHT KEY
                print("Right")
                HUD_AIM.aiming(display_window,P)

    #INITIALIZE

    #map(map2)
    P.movement()
    if Multiplayer:
        P2.movement()
    HUD_AIM.spawn(display_window)
    #print(find_mouse_pos())
   
    #GAME OVER

    if P.check_collision_Object(E.rect):
        message("PLAYER 1 WINS ! ",color_black,220,150)
        if Multiplayer:
            P2.stop()
    if P2.check_collision_Object(E.rect):
        message("PLAYER 2 WINS ! ",color_black,220,150)
        P.stop()
    if P.check_collision_Object(P2.rect):
        if Multiplayer:
            P2.stop()
        message("GAME OVER ! ",color_black,220,150)

    #SPAWN

    P.spawn(display_window)
    E.spawn(display_window)
    if Multiplayer:
        P2.spawn(display_window)
    pygame.display.update()
    game_fps.tick(FPS)


    