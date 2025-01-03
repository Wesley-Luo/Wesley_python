import pygame
import random
import math
import time
import os
pygame.init()
W = 1000
H = 600
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("殭屍戰爭")
zombie_img = pygame.transform.scale(pygame.image.load(os.path.join("zombie fight","zombie_img.png")),(55,60))
player_img = pygame.transform.scale(pygame.image.load(os.path.join("zombie fight","player_img.png")),(55,50))
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("zombie fight","bullet_img.png")),(15,15))
heart_img = pygame.transform.scale(pygame.image.load(os.path.join("zombie fight","live.png")),(50,50))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("zombie fight","arctic.png")),(1000,600))
starting_img = pygame.image.load(os.path.join("zombie fight","zombie_start.png"))
pygame.display.set_icon(zombie_img)
bite_sd = pygame.mixer.Sound(os.path.join("zombie fight","bite_sd.wav"))
bite_sd.set_volume(0.5)
boom_sd = pygame.mixer.Sound(os.path.join("zombie fight","cymbal_sd.wav"))
shoot_sd = pygame.mixer.Sound(os.path.join("zombie fight","shoot_sd.wav"))    
coin_sd = pygame.mixer.Sound(os.path.join("zombie fight","coin.wav"))    
wl_sd = [pygame.mixer.Sound(os.path.join("zombie fight","win.wav")),pygame.mixer.Sound(os.path.join("zombie fight","lose.wav"))]  
pygame.mixer.music.load(os.path.join("zombie fight","zombie_sd.wav")) 
zombies = 20                                         
lives = 100

font_name = os.path.join("zombie fight","font.ttf")
def draw_text(surf, text, size, x, y,col):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = H/2
        self.ang = 0
        self.dir = 0
        self.speed = 5
        self.x = W/2
        self.y = H/2
    def update(self):
        global player_img
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] == 1:
            self.ang += 3
            self.image = pygame.transform.rotozoom(player_img,self.ang,1)
            self.reset()
        if key[pygame.K_RIGHT] == 1:
            self.ang -= 3
            self.image = pygame.transform.rotozoom(player_img,self.ang,1)
            self.reset()
        if key[pygame.K_UP] == 1:
            self.y += (0-math.cos(self.get_radians()))*self.speed
            self.x += (0-math.sin(self.get_radians()))*self.speed
        if key[pygame.K_DOWN] == 1:
            self.y += math.cos(self.get_radians())*self.speed
            self.x += math.sin(self.get_radians())*self.speed
        if self.x <= 0:
            self.x = 0
        if self.x >= 1000:
            self.x = 1000
        if self.y <= 0:
            self.y = 0
        if self.y >= 600:
            self.y = 600
        if key[pygame.K_SPACE] == 1:
            shoot_sd.play()
            shoot.pos = [self.x,self.y]
            shoot.shoot = 1
        self.rect.centerx = self.x
        self.rect.centery = self.y
    def reset(self):
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = H/2
        self.dir = self.ang%360
    def get_radians(self):
        return math.radians(self.dir)
    def bite(self):                                           
        global lives
        self.y += math.cos(self.get_radians())*self.speed*3
        self.x += math.sin(self.get_radians())*self.speed*3
        lives -= 1

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = zombie_img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(1,1000)
        self.rect.centery = random.randint(1,600)
        while self.rect.colliderect(player.rect):
            self.rect.centerx = random.randint(1,1000)
            self.rect.centery = random.randint(1,600)
        self.ang = 0
        self.dir = 0
        self.x = 0
        self.y = 0
        self.speed = random.randint(1,4)
    def update(self):
        global zombies
        self.speed = random.randint(1,4)
        self.image = pygame.transform.rotozoom(zombie_img,0,1)

        self.x = int(self.rect.centerx)
        self.y = int(self.rect.centery)

        if self.x == int(player.rect.centerx) and self.y < int(player.rect.centery):
            self.ang = 180
        elif self.x == int(player.rect.centerx) and self.y > int(player.rect.centery):
            self.ang = 0
        elif self.x < int(player.rect.centerx) and self.y == int(player.rect.centery):
            self.ang = -90
        elif self.x > int(player.rect.centerx) and self.y == int(player.rect.centery):
            self.ang = 90

        elif self.x < player.rect.centerx and self.y < player.rect.centery:
            self.ang = -135
        elif self.x < player.rect.centerx and self.y > player.rect.centery:
            self.ang = -45
        elif self.x > player.rect.centerx and self.y < player.rect.centery:
            self.ang = 135
        elif self.x > player.rect.centerx and self.y > player.rect.centery:
            self.ang = 45
        self.image = pygame.transform.rotozoom(zombie_img,self.ang,1)

        if self.x < int(player.rect.centerx):
            self.rect.centerx += self.speed/(zombies/5)
        elif self.x > int(player.rect.centerx):
            self.rect.centerx -= self.speed/(zombies/5)
        if self.y > int(player.rect.centery):
            self.rect.centery -= self.speed/(zombies/5)
        elif self.y < int(player.rect.centery):
            self.rect.centery += self.speed/(zombies/5)

        if self.rect.colliderect(shoot.rect):
            boom_sd.play()   
            shoot.__init__()
            zombies -= 1
            allsp.remove(self)
        if self.rect.colliderect(player.rect):
            player.bite()
            bite_sd.play()

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bullet_img
        self.shoot = 0
        self.bullet = 0
        self.pos = []
        self.rect = self.image.get_rect()
        self.rect.centerx = 10000
        self.rect.centery = 10000
    def update(self):
        key = pygame.key.get_pressed()
        if self.shoot == 1 and self.bullet == 0 and key[pygame.K_UP] == 0 and key[pygame.K_DOWN] == 0:
            self.shoot = 0 
            self.bullet = 1
            self.rect = self.image.get_rect()
            self.move = [math.cos(player.get_radians()),math.sin(player.get_radians())]
            self.rect.centerx = self.pos[0]
            self.rect.centery = self.pos[1]
        if self.bullet == 1:
            self.rect.centery += (0-self.move[0])*10
            self.rect.centerx += (0-self.move[1])*10
            if self.rect.centery >= 610 or self.rect.centery <= -10 or self.rect.centerx <= -10 or self.rect.centerx >= 1010:
               self.bullet = 0
               self.pos.clear()
               self.move.clear()
               self.__init__()

class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = heart_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 10000
        self.rect.centery = 10000
    def update(self):
        global lives
        if random.randint(0,100) == 50:
            self.random()
        if self.rect.colliderect(player.rect):
            lives += 10
            coin_sd.play()
            self.random()
    def random(self):
        self.rect.centerx = random.randint(10,990)
        self.rect.centery = random.randint(10,590)
            

def win():
    screen.blit(back_img,(0,0))
    draw_text(screen,"lives: "+str(lives), 30, 65, 15,"black")
    draw_text(screen,"You win!",220, W/2, 300,"green")
    pygame.display.update()
    wl_sd[0].play()
    time.sleep(3)
    pygame.quit()
    exit()

def lose():
    screen.blit(back_img,(0,0))
    draw_text(screen,"lives: 0", 30, 65, 15,"black")
    draw_text(screen,"You lose!",210, W/2, 300,"red")
    pygame.display.update()
    wl_sd[1].play()
    time.sleep(3)
    pygame.quit()
    exit()

pygame.mixer.music.play(-1)

start_img = pygame.transform.scale(starting_img, (1000,600))
screen.blit(start_img, (0,0))
pygame.display.update()
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            waiting = False
       
allsp = pygame.sprite.Group()
player = Player()
shoot = Shoot() 
allsp.add(player)
allsp.add(shoot)
for i in range(3):
    heart = Heart()
    allsp.add(heart)
for i in range(20):
    zombie = Zombie()   
    allsp.add(zombie)

screen.blit(back_img,(0,0))
draw_text(screen,"The game is about to start.", 50, 500, 30,"orange")
allsp.update()
allsp.draw(screen)
pygame.display.flip()  
time.sleep(3)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(back_img,(0,0))
    allsp.update()
    allsp.draw(screen)
    draw_text(screen,"lives: "+str(lives), 30, 65, 15,"black")
    if zombies <= 0:
        time.sleep(2)
        win()
    if lives <= -1:
        pygame.display.update()
        time.sleep(2)
        lose()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()