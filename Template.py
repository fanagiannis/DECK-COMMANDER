import pygame

from pygame.locals import * 
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1240,720))
clock=pygame.time.Clock()
running=True

while running:

    for event in pygame.event.get():
        if event.type == pygame.quit:
            running=False
    
    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)
    inp=input("Quit? ")
    if inp=="y":
        running=False 
pygame.quit()
    