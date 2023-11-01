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

    def reset_position(self):
        self.posx=random.randint(40,DISPLAY_WIDTH-40)
        self.posy=-100
        self.pos=(self.posx,self.posy)
        self.target_type=self.types[0]
        self.speed+=0.1   

    def shot(self):
        if self.posy<DISPLAY_HEIGHT:
            self.posy+=self.speed
            self.pos = (self.posx,self.posy)
        else:
            self.reset_position()

    def move(self):
        self.rect.center=self.pos

    def update(self):
        self.move()
        pass