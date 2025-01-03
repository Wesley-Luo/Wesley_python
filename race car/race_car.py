import pygame
import random
import time
import math
import os
pygame.init()
W = 1000
H = 600
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("賽車遊戲")
clock = pygame.time.Clock()
player_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("race car","race_car.png")),(150,70)),-90)
road_img = pygame.transform.scale(pygame.image.load(os.path.join("race car","road.png")),(4000,3800))
stars = [pygame.transform.scale(pygame.image.load(os.path.join("race car","star1.png")),(150,150)),pygame.transform.scale(pygame.image.load(os.path.join("race car","star2.png")),(150,150))]
green_flag_img = pygame.image.load(os.path.join("race car","green flag.png"))
starting_img = pygame.image.load(os.path.join("race car","race_car_start.png"))
pygame.display.set_icon(player_img)
eat_sd = pygame.mixer.Sound(os.path.join("race car","eat.wav"))
goal_sd = pygame.mixer.Sound(os.path.join("race car","Tada.wav"))
out_sd = pygame.mixer.Sound(os.path.join("race car","out_sd.wav"))
din_sd = pygame.mixer.Sound(os.path.join("race car","din_sd.wav"))
wl_sd = [pygame.mixer.Sound(os.path.join("race car","win.wav")),pygame.mixer.Sound(os.path.join("race car","lose.wav"))]
createx = [511,1331,-543,905,-1077]
createy = [1543,1008,618,-1172,-229]
pygame.mixer.music.load(os.path.join("race car","Video Game 1.wav"))
score = 0
timer = 1260

font_name = os.path.join("race car","font.ttf")
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
    def reset(self):
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = H/2
        self.dir = self.ang%360
    def get_radians(self):
        return math.radians(self.dir)

class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = road_img
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = 500
        self.x = -777
        self.y = 1347
        self.speed = 15
        self.key = 0
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] == 1:
            self.y += math.cos(player.get_radians())*self.speed
            self.x += math.sin(player.get_radians())*self.speed
            self.key = 15
        if key[pygame.K_DOWN] == 1:
            self.y += (0-math.cos(player.get_radians()))*self.speed
            self.x += (0-math.sin(player.get_radians()))*self.speed
        if self.key != 0 and key[pygame.K_UP] == 0 and key[pygame.K_DOWN] == 0:
            self.speed *= 0.9
            self.y += (math.cos(player.get_radians()))*self.speed
            self.x += (math.sin(player.get_radians()))*self.speed
            self.key -= 1
            if self.key <= 0:
                self.speed = 15

        if key[pygame.K_SPACE] == 1:
            self.speed *= 1.001
        else:
            self.speed = 15
            
        self.rect.centerx = self.x
        self.rect.centery = self.y
        if not self.rect.colliderect(player.rect):
            out_sd.play()
            time.sleep(1)
            self.__init__()
            

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = stars[random.randint(0,1)]
        self.rect = self.image.get_rect()
        self.x = createx[0]
        self.y = createy[0]
    def update(self):
        global score
        self.rect.centerx = self.x + road.x
        self.rect.centery = self.y + road.y
        if self.rect.collidepoint(player.rect.centerx,player.rect.centery):
            eat_sd.play()
            score += 1
            allsp.remove(self)

class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = green_flag_img
        self.rect = self.image.get_rect()
        self.x = 1200
        self.y = -1100
    def update(self):
        global score
        if score >= 5 :
            self.rect.centerx = self.x + road.x
            self.rect.centery = self.y + road.y
            if self.rect.colliderect(player.rect):
                road.speed = 0
                goal_sd.play()
                time.sleep(2)
                win()
                allsp.remove(self)
        else:
            self.rect.centerx = 100000000
            self.rect.centery = 100000000

def win():
    screen.fill("orange")
    draw_text(screen,"You win!",220, W/2, 300,"dark green")
    pygame.display.update()
    wl_sd[0].play()
    time.sleep(3)
    pygame.quit()
    exit()
def lose():
    screen.fill("orange")
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
            din_sd.play()
            waiting = False
     
allsp = pygame.sprite.Group()
road = Road()
allsp.add(road)
player = Player()
allsp.add(player)
flag = Flag()
allsp.add(flag)
for i in range(len(createx)):
    star = Star()
    allsp.add(star)
    createx.pop(0)
    createy.pop(0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("green")
    allsp.update()
    allsp.draw(screen)
    draw_text(screen,"score:"+str(score)+"/5",50, 120, 25,"white")
    timer -= 1
    draw_text(screen,"time:"+str(int(timer/60)),50, 890, 25,"white")
    pygame.display.flip()
    if timer <= 0:
        time.sleep(2)
        lose()
    clock.tick(60)

pygame.quit()
exit() 