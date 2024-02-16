import pygame
pygame.init()
from lazer import Lazer


class Spaceship (pygame.sprite.Sprite): #organises code and gives attributes to object    
    
    def __init__(self,x,y,screen_width,screen_height,speed): #initialise Spaceship        
        super().__init__() #inherites all attributes of Sprite Class                  
        
        #BASIC ATTRIBUTES
        self.x = x
        self.y = y
        self.speed = speed
        self.screen_width = screen_width 
        self.screen_height = screen_height                           

        
        #IMAGE OF SHIP 
        self.image = pygame.image.load("command_deck/spaceship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect(midbottom = (self.screen_width / 2 ,self.screen_height / 1.5 ))   # a rect with the dimensions of the image

        
        #LAZER ATTRIBUTES
        self.lazer_group = pygame.sprite.Group()
        self.lazer_ready = True
        self.lazer_time = 0
        self.lazer_delay = 300
        
    
    #SHIP'S MOVEMENT
    def get_user_input(self): # user input --> movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
    
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_SPACE] and self.lazer_ready:
            self.lazer_ready = False
            lazer = Lazer(self.rect.center,5,self.screen_height)
            self.lazer_group.add(lazer)
            self.lazer_time = pygame.time.get_ticks()

        #elif keys[pygame.K_w]:
            #self.rect.y -= self.speed
        
        #elif keys [pygame.K_s]:
            #self.rect.y += self.speed

    
    
    #REMAIN AT THE WINDOW
    def constrain_movement(self): #limit the aim movement within the game window
        if self.rect.right > self.screen_width: #bring it back to the window
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0 
        #if self.rect.bottom > self.screen_height:
            #self.rect.bottom = self.screen_height
        #if self.rect.y < 0:
            #self.rect.y = 0     

    def update(self): # updates the aim movement
        self.get_user_input()
        self.constrain_movement()
        self.lazer_group.update()
        self.recharge_lazer()
    
    # RECHARGING LAZER
    def recharge_lazer(self):
        if not self.lazer_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.lazer_time >= self.lazer_delay:
                self.lazer_ready = True