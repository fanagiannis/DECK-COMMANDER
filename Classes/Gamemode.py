import pygame


class Gamemode():
    def __init__(self):
        try:
            self.title="Defend the ship at all costs!"
            self.round=1
            self.round_change=3
            self.game_round_change_score=1000
            self.spawn_time_inc=5
            self.damage_inc=50
            self.speed_inc=1
            self.t_spawn_time=60
            self.t_Damage=150
            self.t_speed=1
            self.game_over=False
        except pygame.error as e:
            print(f"Error in object iniialization : {e}")
    
    def reset(self):
        self.round=1
        self.round_change=3
        self.game_round_change_score=1000
        self.spawn_time_inc=5
        self.damage_inc=50
        self.speed_inc=1
        self.t_spawn_time=60
        self.t_Damage=150
        self.t_speed=1
        self.game_over=False
        
    def round_difficulty_inc(self):
        self.t_spawn_time-=self.spawn_time_inc
        self.t_Damage+=self.damage_inc
        self.t_speed+=self.speed_inc
        self.round_change+=3
        print("INC!")

    def round_inc(self):
        self.round+=1
        self.game_round_change_score+=1000