import pygame
import random 

from Constants import LINK_ASSETS_TARGET,DISPLAY_WIDTH,DISPLAY_HEIGHT

random.seed()

class Target (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LINK_ASSETS_TARGET)
        self.rect=self.image.get_rect()
        self.offset=self.image.get_height()
        self.speed=5
        self.posx=random.randint(40,DISPLAY_WIDTH-40)
        self.posy=-100
        self.pos=(self.posx,self.posy)
        self.rect.center=self.pos
        self.direction_vector=[-1,1]
        self.direction_index=random.randint(0,1)
        self.direction=self.direction_vector[self.direction_index]
        self.direction=-1

    def movement(self):
        #if self.posx<=DISPLAY_WIDTH/2:
        #    self.direction=1
        #else:
        #    self.direction=-1
        
        if self.posy<DISPLAY_HEIGHT:
            self.posy+=self.speed*self.direction
            self.posx+=self.speed*self.direction
            self.pos = (self.posx,self.posy)
        else:
            self.kill()
        pass

    def move(self):
        self.movement()
        self.rect.center=self.pos

    def update(self):
        self.move()
        pass