import pygame
import sys
from pygame.locals import * 

pygame.init()

#COLORS
color_black=pygame.color(0,0,0)
color_white=pygame.color(255,255,255)
color_grey=pygame.color(128,128,128)
color_red=pygame.color(255,0,0)

#DISPLAY WINDOW
window_size= pygame.display.set_mode((300,300))

#FPS 
game_fps=pygame.time.clock()
game_fps.tick(60)

#OBJECTS
object1=pygame.rect((20,50),(50,100))
object2=pygame.rect((10,10),(100,100))

while True:
    for event in pygame.event.get():
        if event.type()==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    