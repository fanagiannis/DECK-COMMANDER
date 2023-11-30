import pygame 
pygame.init()

 #Κλάση AIM
class Aim(pygame.sprite.Sprite):
  
    def __init__(self,x,y,screen_width,screen_height,speed):
        super().__init__()
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height             
        self.image = pygame.image.load("aim.png") 
        self.image = pygame.transform.scale(self.image,(40,40))  
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2 ,self.screen_height/2 ))
        self.speed = speed # how quickly the aim moves --> velocity in other words

    def update(self): # updates the aim movement
        self.rect.center = pygame.mouse.get_pos()
        self.constrain_movement()

        
    def constrain_movement(self): #limit the aim movement within the game window
        if self.rect.right > self.screen_width: #bring it back to the window
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        if self.rect.y < 0:
            self.rect.y = 0 
