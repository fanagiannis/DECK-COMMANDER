import pygame

from Var.Variables import P
from Var.Variables import Spawner

class Gamemode():
    def __init__(self):
        self.title="Defend the ship at all costs!"
        self.round=1
        self.game_round_change_score=1000
        self.spawn_time_inc=5
        self.damage_inc=50
        self.speed_inc=1
        self.t_spawn_time=60
        self.t_Damage=100
        self.t_speed=1
    
    def rounds(self):
        if P.score==self.game_round_change_score:
            self.round+=1
            self.game_round_change_score+=1000
        if self.round==5:
            self.t_spawn_time+=self.spawn_time_inc
            self.t_Damage+=self.damage_inc
            self.t_speed+=self.speed_inc
        Target_spawn=Spawner(self.t_spawn_time,self.t_Damage,self.t_speed)

    def update(self):
        pass