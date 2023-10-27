import pygame
import sys
import random
import time
#from turtle import delay
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

 #+++++PATHS+++++

link_pc="H:\\My Drive\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON"
link_laptop="G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON"
link_op=link_pc

pygame.display.set_caption("(Local) Two Player Collision Game")


#+++++FUNCTIONS+++++



    #+++++COLORS+++++

color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

    #+++++DISPLAY WINDOW+++++

display_width=1240
display_height=720
display_window= pygame.display.set_mode((display_width,display_height))

display_center=((display_width-(display_width/2)),(display_height-(display_height/2)))



    #+++++COUNTERS+++++

Players=[]
SpawnPoints=[(160,220),(1060,220),(1060,520)]
ObjSpawnPoints=[(620,360),(390,50),(550,680),(460,360),(),(),(),(),()]
MaxPlayers=2
Multiplayer=True

    #+++++GAME OVER+++++
font=pygame.font.SysFont(None,30,bold=True)
    #game_over_screen=pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Game_Over.png")

    #+++++FPS+++++ 
game_fps=pygame.time.Clock()
FPS=60

    #+++++SCALES+++++

player_scale=10
enemy_scale=5


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

    
    

#+++++CLASSES+++++

#PROJECTILE

class Projectile(pygame.sprite.Sprite):
    def __init__(self,posx,posy,width,height,speed):
        super().__init__()
        self.image = pygame.image.load(link_op+"\\Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center=(posx,posy)
        self.x=posx
        self.y=posy
        self.width=width
        self.height=height
        self.speed=speed
        self.fired=False

    def fire(self):
        if self.fired:
            display_window.blit(self.image,(self.x,self.y))
    def get_proj_rect(self):
        return self.rect

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
        self.rect.center=(random.randrange(320,display_width-320),random.randrange(40,display_height-40)) #randomise
        self.speed=5

    def teleport(self):
        enemy_speed=10
        oldposx,oldposy=self.rect.center
        randpos=[(random.randrange(320,display_width-320)-oldposx),(random.randrange(40,display_height-40)-oldposy)]

        if(self.rect.top>600):
            self.rect.top= 0
            
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
        self.Fire=False

    #PLAYER_MOVEMENT
    
    def movement(self):
       
        pressed_keys=pygame.key.get_pressed()

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
        
    def shoot(self):
       mouse_pos=find_mouse_pos()

    def stop(self):
        self.speed = 0  
    
    def sprint(self):
        if self.speed>0 :
            self.speed = self.maxspeed
        
    def find_pos(self):
        x=self.rect.centerx
        y=self.rect.centery
        return x , y

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
        if abs(rect.top - self.rect.bottom) < 10:
            self.stop()
            P2.stop()
            return True
        if abs(rect.bottom - self.rect.top) < 10:
            self.stop()
            P2.stop()
            return True
        if abs(rect.right - self.rect.left) < 10:
            self.stop()
            P2.stop()
            return True
        if abs(rect.left - self.rect.right) < 10:
            self.stop()
            P2.stop()
            return True

       
    def spawn(self,surface):
        surface.blit(self.image,self.rect)

#init_game()

map1="D:\\ΦΩΤΟ\\darksouls.jpg"
map2="D:\\ΦΩΤΟ\\Rodos.jpg"

P=Player()

set_players(P)
if Multiplayer:
    P2=Player()
    set_players(P2)

bullet_width=32
bullet_height=32
bullet_posx=P.rect.centerx
bullet_posy=P.rect.centery
bullet_speed=15


bullet = Projectile(bullet_width,bullet_height,bullet_posx,bullet_posy,bullet_speed)
bullet2 = Projectile(bullet_width,bullet_height,bullet_posx,bullet_posy,bullet_speed)


HUD_AIM=Aim()

pygame.mouse.set_visible(False)


while True:

#BACKGROUND

    display_window.fill(color_white)

    for event in pygame.event.get():
        if event.type==QUIT or pygame.key.get_pressed()==[K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x,y=P.find_pos()
                #Bullet=Projectile(x,y)
                #Bullet.fire(display_window,x,y)
                bullet.fired=True
                bullet.x=x - bullet.width/2
                bullet.y=y 
            if Multiplayer:
                if event.key == pygame.K_RSHIFT:
                    x2,y2=P2.find_pos()
                    #Bullet=Projectile(x,y)
                    #Bullet.fire(display_window,x,y)
                    bullet2.fired=True
                    bullet2.x=x2 - bullet2.width/2
                    bullet2.y=y2 
                    pygame.time.set_timer(pygame.K_RSHIFT,2000)

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
    
    # map(map2)
    P.movement()
    if Multiplayer:
        P2.movement()
    if bullet.fired:
        bullet.x+=bullet.speed
    if bullet2.fired:
        bullet2.x-=bullet.speed
   
    #GAME OVER

    if Multiplayer:
        if P.check_collision_Object(bullet2.rect):
            message("GAME OVER ! ",color_black,220,150)
            print ("hit")
    
    
    #SPAWN

    P.spawn(display_window)
 
    if Multiplayer:
        P2.spawn(display_window)

    HUD_AIM.spawn(display_window)
    bullet.fire()
    #if Multiplayer:
    bullet2.fire()

    pygame.display.update()
    
    game_fps.tick(FPS)

    

    