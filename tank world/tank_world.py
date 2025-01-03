import pygame
import random
import time
import os
pygame.init()

W = 1000
H = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("坦克世界")
tank_img = pygame.image.load(os.path.join("tank world","tank.png"))
enemy_imgs = [pygame.image.load(os.path.join("tank world","enemy.png")),pygame.image.load(os.path.join("tank world","enemy2.png"))]
boom_img = pygame.image.load(os.path.join("tank world","destroyed.png"))
bullet_imgs = [pygame.image.load(os.path.join("tank world","bullet.png")),pygame.image.load(os.path.join("tank world","bullet2.png"))]
none = pygame.image.load(os.path.join("tank world","nothing.png"))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("tank world","tank_back.png")),(1000,600))
starting_img = pygame.image.load(os.path.join("tank world","tank_start.png"))
sounds = [pygame.mixer.Sound(os.path.join("tank world","cymbal.wav")),pygame.mixer.Sound(os.path.join("tank world","pew.wav"))]
wl_sd = [pygame.mixer.Sound(os.path.join("tank world","win.wav")),pygame.mixer.Sound(os.path.join("tank world","lose.wav"))]
score = 0
pygame.display.set_icon(tank_img)
pygame.mixer.music.load(os.path.join("tank world","trap beat.wav"))

font_name = os.path.join("tank world","font.ttf")
def draw_text(surf, text, size, x, y,col):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface, text_rect)

def lose():
    time.sleep(2)
    screen.blit(back_img,(0,0))
    draw_text(screen, "Game Over!", 150,W/2, 300,"red")
    pygame.display.flip()
    wl_sd[1].play()
    time.sleep(3)
    pygame.quit()
    exit()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =  tank_img
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = 540
        self.time = 0
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] == 1 and self.rect.x >= 0:
            self.rect.centerx -= 5
        if key[pygame.K_RIGHT] == 1 and self.rect.x <= 910:
            self.rect.centerx += 5
        if self.rect.colliderect(shoot.rect) and shoot.bullet == 1 or self.image == boom_img:
            self.image = boom_img
            sounds[0].play()
            lose()
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = none
        self.bullet = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = 540
    def update(self):
        key = pygame.key.get_pressed()
        if (key[pygame.K_SPACE] == 1 and self.bullet == 0):
            sounds[1].play()
            self.image = bullet_imgs[0]
            self.rect = self.image.get_rect()
            self.rect.centerx = player.rect.centerx
            self.rect.y = 500
            self.bullet = 1
        if self.bullet != 0:
            self.rect.centery -= 10
            if self.rect.centery <= -10:
               self.bullet = 0
               self.__init__()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_imgs[random.randint(0,1)]
        self.speed = random.randint(2,5)
        self.rect = self.image.get_rect()
        self.time = 0
        self.rect.centerx = random.randint(100,900)
        self.rect.centery = -10
    def update(self):
        global score
        self.rect.y += self.speed
        if self.rect.y >= 600:
            self.__init__()
        if self.rect.colliderect(bullet.rect) and bullet.bullet == 1:
            self.image = boom_img
            self.speed = 0
            bullet.__init__()
            self.time = 1
            sounds[0].play()
            score += 1
        if self.rect.colliderect(player.rect):
            player.image = boom_img
            self.image = boom_img
            self.speed = 0
            sounds[0].play()
        if self.time != 0:
            self.time += 1
            if self.time >= 20:
                self.__init__()
        if random.randint(0,50) == 1 and shoot.bullet == 0 and self.image != boom_img:
            shoot.shoot = 1
            shoot.pos = [self.rect.centerx,self.rect.centery]

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = none
        self.shoot = 0
        self.bullet = 0
        self.pos = []
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = 540
    def update(self):
        if self.shoot == 1 and self.bullet == 0:
            self.shoot = 0 
            self.bullet = 1
            self.image = bullet_imgs[1]
            self.rect = self.image.get_rect()
            self.rect.centerx = self.pos[0]
            self.rect.centery = self.pos[1]
        if self.bullet == 1:
            self.rect.centery += 7
            if self.rect.centery >= 610:
               self.bullet = 0
               self.__init__()

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

allsp =  pygame.sprite.Group()       
player = Player()
bullet = Bullet()
shoot = Shoot()
allsp.add(player)
allsp.add(bullet)
allsp.add(shoot)
for i in range(3):
    enemy = Enemy()
    allsp.add(enemy)

run = True
while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(back_img,(0,0))
    allsp.update()
    allsp.draw(screen)
    draw_text(screen, "score: "+str(score), 30,65, 20,"black")
    pygame.display.flip()

    if score >= 20:
        time.sleep(2)
        screen.blit(back_img,(0,0))
        draw_text(screen, "You win!", 200,W/2, 300,"green")
        pygame.display.flip()
        wl_sd[0].play()
        time.sleep(3)
        run = False

pygame.quit()
exit()