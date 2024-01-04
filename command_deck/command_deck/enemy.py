import pygame

pygame.init()


class Enemy (pygame.sprite.Sprite):
        
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)        
        self.x = x
        self.y = y
        
        #IMAGE
        self.image = pygame.image.load('command_deck/command_deck/enemyship.png')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    
    def update(self):
        self.rect.centery += 3
        if self.rect.y > 750:
            self.kill()
            print("killed")