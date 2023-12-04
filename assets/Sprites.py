import pygame

from Var.Variables import *
from Var.Constants import *

def screens():
    #pygame.draw.rect(DISPLAY_WINDOW,COLOR_YELLOW,(DISPLAY_WIDTH-200,DISPLAY_HEIGHT-100,DISPLAY_WIDTH,DISPLAY_HEIGHT)) #AMMO/HP SCREEN
    SCREEN1=pygame.image.load(LINK_ASSETS_SCREEN)
    SCREEN2=pygame.image.load(LINK_ASSETS_SCREEN3)
    DISPLAY_WINDOW.blit(SCREEN2,(DISPLAY_WIDTH-200,DISPLAY_HEIGHT-100))
    #pygame.draw.rect(DISPLAY_WINDOW,COLOR_YELLOW,(0,DISPLAY_HEIGHT-100,200,DISPLAY_HEIGHT)) #SCORE SCREEN
    DISPLAY_WINDOW.blit(SCREEN2,(0,DISPLAY_HEIGHT-100))

def planets():
    PLANET=pygame.image.load(LINK_ASSETS_PLANET)
    PLANETSCALED=pygame.transform.scale(PLANET,(200,200))
    PLANET2=pygame.image.load(LINK_ASSETS_PLANET2)
    PLANET2SCALED=pygame.transform.scale(PLANET2,(100,100))
    PLANET3=pygame.image.load(LINK_ASSETS_PLANET3)
    PLANET3SCALED=pygame.transform.scale(PLANET3,(100,100))

    DISPLAY_WINDOW.blit(PLANETSCALED,(-75,DISPLAY_HEIGHT/2))
    DISPLAY_WINDOW.blit(PLANET2SCALED,(DISPLAY_WIDTH-250,0))
    DISPLAY_WINDOW.blit(PLANET3SCALED,(450,0))

def power():
    energy_supply_left=DISPLAY_WIDTH-180
    energy_supply_top=DISPLAY_HEIGHT-30
    energy_supply_width=P.ammo_supplies
    energy_supply_height=15
    energy_supply_pos=(energy_supply_left,energy_supply_top,energy_supply_width,energy_supply_height)
    pygame.draw.rect(DISPLAY_WINDOW,COLOR_GREEN,energy_supply_pos)

def screen_effect(color):
    DISPLAY_WINDOW.fill(color)

def message(text,text_color,text_pos,font):
    display_text=font.render(text,True,text_color)
    DISPLAY_WINDOW.blit(display_text,text_pos)
    pass   

def background(image):
    background=pygame.image.load(image)
    DISPLAY_WINDOW.blit(background,(0,0))