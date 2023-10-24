import pygame
import sys
import random
import time
#from turtle import delay
from pygame.locals import *
from pygame.sprite import _Group, Group 

pygame.init()

#FPS 
game_fps=pygame.time.Clock()
FPS=60

#COLORS
color_black=pygame.Color(0,0,0)
color_white=pygame.Color(255,255,255)
color_grey=pygame.Color(128,128,128)
color_red=pygame.Color(255,0,0)

#DISPLAY WINDOW
display_width=620
display_height=360
display_window= pygame.display.set_mode((display_width,display_height))

display_center=((display_width-(display_width/2)),(display_height-(display_height/2)))

display_window.fill(color_white)
pygame.display.set_caption("Main Menu")



#CLASSES

class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Player.png")
        self.button_size=[(display_width/2 ,display_height/2),display_center]
        self.position=(160,220)
        self.rect=self.image.get_rect()
        self.rect.center=self.position
    pygame.draw.polygon(display_window,color_red,button_size,width=10)

    def spawn(self):
        pygame.draw.polygon(display_window,color_red,self.button_size,width=10)

while True:

    for event in pygame.event.get():
        if event.type==QUIT or pygame.key.get_pressed()==[K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
    
    display_window.fill(color_grey)
    pygame.draw.rect(display_window,color_red,button_size,width=50)
    pygame.display.update()
    game_fps.tick(FPS)
