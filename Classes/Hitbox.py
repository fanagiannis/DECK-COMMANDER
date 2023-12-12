import pygame

from pygame.locals import *

from Var.Constants import DISPLAY_WINDOW,COLOR_RED

class Hitbox():
    def __init__(self,a,b):
        self.rect=pygame.Rect(0,a-100,b,100)
        self.base_hp=1000
        self.hp=self.base_hp
        self.IsRepairing=False
        self.dead=False
        self.repair_time=3000

    def repair(self):
        pressed_key=pygame.key.get_pressed()

        if self.dead==False:
            if pressed_key[K_f]:
                if self.repair_time>0:
                    if self.hp<self.base_hp:
                        self.IsRepairing=True
                    else:
                        self.IsRepairing=False
                    if self.IsRepairing:
                        self.hp+=1
                        self.repair_time-=1 
                else:
                    self.repair_time=3000
            else:
                self.IsRepairing=False

    def check_if_dead(self):
        if self.hp>0:
            self.dead=False
        else:
            self.dead=True

    def reset(self):
        self.base_hp=1000
        self.hp=self.base_hp
        self.IsRepairing=False
        self.dead=False
        self.repair_time=3000

    def update(self):
        self.check_if_dead()
        self.repair()
        #pygame.draw.rect(DISPLAY_WINDOW,COLOR_RED,self.rect,2)
        #pygame.display.flip()