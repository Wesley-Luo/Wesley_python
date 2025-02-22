import pygame
import random
import time
import math
import os
pygame.init()
W = 1000
H = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("皮卡丘打排球")
starting_img = pygame.image.load(os.path.join("pikachu volleyball","pika_start.png"))
player_img = pygame.image.load(os.path.join("pikachu volleyball", "pika.png"))
enemy_img = pygame.transform.scale(pygame.image.load(os.path.join("pikachu volleyball", "pika_2.png")),(110,110))
ball_img = pygame.transform.scale(pygame.image.load(os.path.join("pikachu volleyball", "ball.png")),(70,70))
net_img = pygame.image.load(os.path.join("pikachu volleyball", "net_pillar.png"))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("pikachu volleyball", "pikachu_back.png")),(1000,600))
win_sd = pygame.mixer.Sound(os.path.join("pikachu volleyball", "win.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("pikachu volleyball", "lose.wav"))
b_sd = pygame.mixer.Sound(os.path.join("pikachu volleyball", "bounce.wav"))
pygame.mixer.music.load(os.path.join("pikachu volleyball", "pika_back_sd.wav"))
pygame.display.set_icon(ball_img)
psc = 0
esc = 0

def win():
    screen.blit(back_img,(0,0))
    draw_text(screen,"You win!",200,W/2+10,300,"green")
    pygame.display.flip()
    win_sd.play()
    time.sleep(3)
    pygame.quit()
    exit() 

def lose():
    screen.blit(back_img,(0,0))
    draw_text(screen,"You lose!",180,W/2,300,"red")
    pygame.display.flip()
    lose_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

font_name = os.path.join("pikachu volleyball","pixel_font.ttf")
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
        self.rect.centerx = 800
        self.rect.centery = 500
        self.jump = False
        self.time = 0
        self.speed = 5
        self.ang = 0
    def update(self):
        key = pygame.key.get_pressed()
        if self.jump == True:
            self.time += 1
            self.rect.centery -= 30
            if self.time >= 7:
                self.jump = False
                self.time = 0
        if not self.rect.colliderect(net.rect) and not self.rect.centerx >= 950:
            if key[pygame.K_LEFT]:
                self.speed = self.speed*1.1
                self.rect.centerx -= self.speed
                self.image = pygame.transform.rotate(player_img, (self.speed-5)*2)
                self.ang = (self.speed-5)*2
            elif key[pygame.K_RIGHT]:
                self.speed = self.speed*1.1
                self.rect.centerx += self.speed
                self.ang =  0-(self.speed-5)*2
                self.image = pygame.transform.rotate(player_img, 0-(self.speed-5)*2)
            else:
                if self.speed > 5:
                    self.speed -= 1
                if self.ang > 0:
                    self.image = pygame.transform.rotate(player_img, (self.speed-5)*1.5)
                if self.ang < 0:
                    self.image = pygame.transform.rotate(player_img, 0-(self.speed-5)*1.5)
        else:
            self.speed = 5
            if self.rect.colliderect(net.rect):
                self.rect.centerx += 1
            elif self.rect.centerx >= 950:
                self.rect.centerx -= 1

        if key[pygame.K_UP] and self.jump == False and self.rect.centery == 500:
            self.jump = True

        if self.rect.centery < 500:
            self.rect.centery += 6
        
        if self.speed == 5 :
            self.image = pygame.transform.rotate(player_img, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ball_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 700
        self.rect.centery = 0
        self.speed = 5
        self.fly = False
        self.flew = False
        self.random = 0
        self.pos = "e"
        self.collide = False    
    def update(self):
        self.rect.centery += self.speed
        if self.rect.centery > 565:
            b_sd.play()
            if self.rect.centerx < 500:
                global psc
                psc += 1
            elif self.rect.centerx > 500:
                global esc
                esc += 1
            self.rect.centery = 0
            if self.pos == "p":
                self.rect.centerx = 700
                self.pos = "e"
            elif self.pos == "e":
                self.rect.centerx = 300
                self.pos = "p"
            self.random = 0
            self.fly = False
            self.flew = False
            self.collide = False
            time.sleep(1)

        if self.rect.colliderect(player.rect):
            b_sd.play()
            self.fly = True
            self.collide = False
            self.flew = False
            self.random = random.randint(10,30)
            self.image = pygame.transform.rotozoom(ball_img, self.random, 1)
        elif self.rect.colliderect(enemy.rect):
            b_sd.play()
            self.flew = True
            self.collide = False
            self.fly = False
            self.random = random.randint(-50,-30)
            self.image = pygame.transform.rotozoom(ball_img, self.random, 1)

        if self.fly == True:
            self.rect.centery -= math.cos(math.radians(self.random))*12
            self.rect.centerx -= math.sin(math.radians(self.random))*11
            if self.collide == False:
                self.random += 100/random.randint(30,90)
        if self.flew == True:
            self.rect.centery -= math.cos(math.radians(self.random))*25
            self.rect.centerx -= math.sin(math.radians(self.random))*12
            if self.collide == False:
                self.random -= 100/random.randint(40,100)

        if self.fly == True or self.flew == True:
            self.image = pygame.transform.rotozoom(ball_img, self.random, 1)
            if self.rect.colliderect(net.rect) and self.rect.centerx < 500:
                self.random = random.randint(30,150)
                self.collide = True
            if self.rect.colliderect(net.rect) and self.rect.centerx > 500:
                self.random = random.randint(-150,-30)
                self.collide = True
            if self.rect.y < 0:
                self.random = random.randint(-150,-100)
                self.collide = True
            if self.rect.x < 0:
                self.random = random.randint(-150,-30)
                self.collide = True
            if self.rect.x > 930:
                self.random = random.randint(100,150)
                self.collide = True
        
class Net(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = net_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.centery = 500
    def update(self):
        if pygame.sprite.collide_rect(self, player):
            player.rect.centery = 500

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 500
        self.time = 0
        self.speed = 4
    def update(self):
        if ball.rect.centerx < 480 and ball.rect.centery > 100:
            if ball.rect.centerx < self.rect.centerx:
                self.rect.centerx -= self.speed+random.choice([0,1,2,3,4])
            elif ball.rect.centerx > self.rect.centerx:
                self.rect.centerx += self.speed

pygame.mixer.music.play(-1)

start_img = pygame.transform.scale(starting_img, (1000,630))
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
enemy = Enemy()
ball = Ball()
net = Net()
allsp.add(player)  
allsp.add(net)  
allsp.add(ball)
allsp.add(enemy)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    allsp.update()
    screen.blit(back_img, (0,0))
    allsp.draw(screen)
    draw_text(screen, str(psc), 100, 900, 50,"red")
    draw_text(screen, str(esc), 100, 100, 50,"red")
    pygame.display.flip()

    if psc == 10:
        time.sleep(1)
        win()
    elif esc == 10:
        time.sleep(1)
        lose()

    clock.tick(60)
pygame.quit()
exit()