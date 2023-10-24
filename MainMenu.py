import pygame
import sys
import random
import time
#from turtle import delay
from pygame.locals import *
from pygame.sprite import Group 

pygame.init()

Button_main_pos=(160,220)
Button_2_pos=(50,220)



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

#SHOW TEXT
font=pygame.font.Font('freesansbold.ttf', 32)
text=font.render('HELLO',True,color_grey,color_red)
text_rect=text.get_rect()
text_rect.center = (display_width/2,display_height/2)


#CLASSES

class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("G:\\Το Drive μου\\Drive fanagiannis\\ΠΜΣ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\Player.png")
        self.button_size=[(display_width/2 ,display_height/2),display_center]
        self.position=(160,220)
        self.name="Default name"
        self.rect=self.image.get_rect()
        self.rect.center=self.position
        self.posx,self.posy=self.position
    def draw_button(self,surface):
        surface.blit(self.image,self.rect)
    def click(self):
        print("Click")

    #pygame.draw.polygon(display_window,color_red,button_size,width=10)

    def spawn(self):
        pygame.draw.polygon(display_window,color_red,self.button_size,width=10)

#FUNCTIONS

def button_click(Button):
    print(Button.name," Clicked!")


button_main=Button()
button_main.name="Button Main"

button_2=Button()
button_2.name="Button 2"
button_2.rect.move_ip(Button_2_pos)

display_window.fill(color_grey)

while True:
    
    #pygame.draw.rect(display_window,color_red,button_size,width=50)
    button_main.draw_button(display_window)
    button_2.draw_button(display_window)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            mouse_posx , mouse_posy=mouse_pos
            if button_main.rect.collidepoint(mouse_pos):
                button_click(button_main)
                display_window.blit(text,text_rect)
            print((mouse_posx,mouse_posy))

        if event.type==QUIT or pygame.key.get_pressed()==[K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
    
    pygame.display.update()
    game_fps.tick(FPS)
