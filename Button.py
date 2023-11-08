import pygame
import sys

from pygame.locals import *
from Variables import *
from Constants import *

pygame.init()

buttons=["Start Game","Multiplayer","Exit"]
index=0

while True:
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            pressed_keys=pygame.key.get_pressed()
            if pressed_keys[K_UP]:
                index-=1
                print(index)
            if pressed_keys[K_DOWN]:
                index+=1
                print(index)

    if index<0:
        index=2
    elif index>2:
        index=0
        
    print(buttons[index])
    pygame.display.flip()
    GAME_CLOCK.tick(FPS)
    
