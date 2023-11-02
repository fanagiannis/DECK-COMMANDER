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
            if self.hp<100:
                self.IsRepairing=True
                print(self.IsRepairing)
            else:
                self.IsRepairing=False
            if self.IsRepairing:
                self.hp+=0.1
            print(self.IsRepairing)
            pass
       
    def update(self):
        self.repair()
        pygame.draw.rect(DISPLAY_WINDOW,COLOR_RED,self.rect,2)
        pygame.display.flip()