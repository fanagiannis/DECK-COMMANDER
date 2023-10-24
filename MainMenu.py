import pygame
import pygame_menu
import sys
import random
import time
from pygame.locals import *

pygame.init()

while True:
  for event in pygame.event.get():
    if event.type == QUIT :
      exit()