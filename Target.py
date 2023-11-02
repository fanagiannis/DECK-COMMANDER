import pygame
import random 

from Constants import LINK_ASSETS_TARGET,DISPLAY_WIDTH,DISPLAY_HEIGHT

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

    def gravity(self):
        if self.posy<DISPLAY_HEIGHT:
            self.posy+=self.speed
            self.pos = (self.posx,self.posy)
        else:
            self.kill()


    def move(self):
        self.gravity()
        self.rect.center=self.pos

    def update(self):
        self.move()
        pass