import pygame
import random 

from Constants import LINK_ASSETS_TARGET,DISPLAY_WIDTH,DISPLAY_HEIGHT

class Target (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LINK_ASSETS_TARGET)
        self.rect=self.image.get_rect()
        self.offset=self.image.get_height()
        self.speed=1
        self.posx=random.randint(40,DISPLAY_WIDTH-40)
        self.posy=-100
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
        self.types=["Bomb","Missile"]
        self.target_type=self.types[0]
        #print(self.pos)
    
    def reset_position(self):
        if self.target_type=="Missile":
            self.posx=random.randint(-DISPLAY_WIDTH+500,0)
        else:
            self.posx=random.randint(40,DISPLAY_WIDTH-40)
        self.posy=-100
        self.pos=(self.posx,self.posy)
        self.target_type=self.types[0]
        self.speed+=0.1   

    def shot(self):
        if self.posy<DISPLAY_HEIGHT:
            if self.target_type=="Missile":
                self.posx+=self.speed
            self.posy+=self.speed
            self.pos = (self.posx,self.posy)
        else:
            self.reset_position()

    def missile_shot(self):
        self.posx=self.rect.centerx
        self.posy=self.rect.centery
        self.posy+=self.speed
        self.posx+=self.speed
        if self.posx>0 and self.posx<DISPLAY_WIDTH/2:
             self.pos=(self.posx,self.posy)
        elif self.posx<DISPLAY_WIDTH/2 and self.posx>DISPLAY_WIDTH:
            self.pos=(self.posx,-self.posy)
        self.pos=(self.posx,self.posy)
        pass

    def move(self):
        self.rect.center=self.pos

    def update(self):
        self.move()
        pass