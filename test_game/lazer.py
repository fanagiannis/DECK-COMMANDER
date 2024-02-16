import pygame
pygame.init()

class Lazer(pygame.sprite.Sprite):
    def __init__(self,position,speed,screen_height):
        super().__init__()
        self.speed = speed        
        self.image = pygame.Surface((4,15))
        self.image.fill((39,222,31))
        self.rect = self.image.get_rect(center = position)
        self.screen_height = screen_height
    
    def update(self):
        self.rect.y -= self.speed   
        if self.rect.y > self.screen_height + 15 or self.rect.y < 0 :
            self.kill()