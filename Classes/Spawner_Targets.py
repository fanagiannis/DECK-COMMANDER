import pygame

from Classes.Target import Target

class Spawner():
    def __init__(self,time,damage,speed):
        print("Spawner Created!") 
        self.group=pygame.sprite.Group()
        self.time_set=time
        self.spawn_time=self.time_set
        self.difficulty=[0,1,2]
        self.index=0
        self.targetdmg=damage 
        self.targetspeed=speed  

    def spawn(self):
        T = Target()
        T.damage=self.targetdmg
        T.speed=self.targetspeed
        self.group.add(T)
    
    def reset_timer(self):
        self.spawn_time=self.time_set
        
    def update(self):
        self.group.update()
        if self.spawn_time==0:
            self.spawn()
            self.reset_timer()
        self.spawn_time-=1

