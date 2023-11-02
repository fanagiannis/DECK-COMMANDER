import pygame

from pygame.locals import *

from Constants import DISPLAY_WINDOW,COLOR_RED

class Hitbox():
    def __init__(self,a,b):
        self.rect=pygame.Rect(0,a-100,b,100)
        self.hp=100
        self.IsRepairing=False

    def repair(self):
        pressed_key=pygame.key.get_pressed()

        if pressed_key[K_f]:
            self.IsRepairing=True
            if self.IsRepairing:
                if self.hp<100:
                    self.hp+=1
                self.IsRepairing=False
            pass

       

    def update(self):
        pygame.draw.rect(DISPLAY_WINDOW,COLOR_RED,self.rect,2)
        pygame.display.flip()