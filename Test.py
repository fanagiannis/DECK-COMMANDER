import pygame 
import sys,time

from assets.Sprites import *

from Var.Constants import *

def introtext():
    background(LINK_ASSETS_BACKGROUND)
    GAME_CLOCK.tick(60)
    message="""
                     Zone of Ender : Summer day 65 of the year 2876

    MotherShip report to Squadron 43: Multiple Targets are approaching your position!
    Dispatch your fighters immediately to repel the attack! Defend the cargo at all costs!

    """

    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

introtext()