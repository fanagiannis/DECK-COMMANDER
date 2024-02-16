#Αρχικοποίηση της Pygame
import pygame
import random 

pygame.init()

    #Παράθυρο
screen_width = 1280

screen_height = 720

game_display = pygame.display.set_mode((screen_width,screen_height))

color = (31,222,69)

pygame.display.set_caption("Tower Defense")


    #Σκορ και ζωές
score = 0
lives = 3
 


    #IMAGES
target = pygame.image.load('TowerDefense//stiill.png')

spaceshipleft = pygame.image.load('TowerDefense//enemy_left.png')
spaceshipleft2 = pygame.transform.scale(spaceshipleft, (100,100))

spaceshipright = pygame.image.load('TowerDefense//enemy_right.png')
spaceshipright2 = pygame.transform.scale(spaceshipright, (100,100))



bg = pygame.image.load('TowerDefense//bg.png')

bg2 = pygame.transform.scale(bg,(1280,720))

aim = pygame.image.load("TowerDefense//aim.png") 

pygame.display.update()   

     #Κλάση AIM
class player(object):
    def __init__(self,x,y,width,height,vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel  
      

class enemy(object):
    def __init__(self):
        self.image = spaceshipleft2
        self.image = spaceshipright2
        self.x = screen_width+200
        self.y = random.randint(0,screen_height)
        self.width = 100
        self.height = 100
        self.vel = 10
        self.direction=1 

    def movement(self):
        if self.x<0:
            self.direction=-1 
        if self.x>screen_width:
            self.direction=1   
        self.x -= self.direction*self.vel

    def update(self):
        self.movement()

class Spawner():
    def __init__(self,time):
        self.group=pygame.sprite.Group()
        self.time_set=time
        self.spawn_time=self.time_set

    def spawn(self):
        E = enemy()
        self.group.add(E)
    
    def reset_timer(self):
        self.spawn_time=self.time_set
        
    def update(self):
        self.group.update()
        if self.spawn_time==0:
            self.spawn()
            self.reset_timer()
        self.spawn_time-=1

    #Συνάρτηση Redraw
def redrawGamewindow():

    game_display.blit(bg2,(0,0))

    game_display.blit(target,(0,0))   
    
    #dgame_display.blit(spaceshipleft2,(enemy_.x,enemy_.y))
    
    game_display.blit(aim,(aim_.x,aim_.y))
    
    font = pygame.font.SysFont('pixel-LCD-7', 30)

    text = font.render("SCORE: " + str(score), 1, color)

    game_display.blit(text, (1090,10))

    text = font.render("LIVES: " + str(lives), 1, color)

    game_display.blit(text, (1090,50))

    pygame.display.update()

     #Main βρόγχος του παιχνιδιού
aim_ = player(600,300,75,75,10)

run = True

clock = pygame.time.Clock()

#enemy_ = enemy(1200,300,75,75,10)

spawner=Spawner(25)

while run:
    clock.tick(20)
    
    for event in pygame.event.get(): #επιστρέφονται οι ενέργειες του χρήστη
        if event.type == pygame.QUIT:   #έξοδος από το παράθυρο
            run = False

    # Movement of the character and Boundaries
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and aim_.x > aim_.vel:
        aim_.x -= aim_.vel
    
    elif keys[pygame.K_d] and aim_.x < screen_width - aim_.width - aim_.vel :
        aim_.x += aim_.vel
    
    elif keys[pygame.K_w] and aim_.y > aim_.vel:
        aim_.y -= aim_.vel
    
    if keys[pygame.K_s] and aim_.y < screen_height - aim_.height - aim_.vel:
        aim_.y += aim_.vel

    if keys [pygame.K_SPACE]:
        pygame.draw.circle(game_display, (0,200, 0), (aim_.x + 37.5, aim_.y + 37.5), 37.5)
        pygame.display.update() 

    spawner.update()
    redrawGamewindow()


pygame.quit()
        