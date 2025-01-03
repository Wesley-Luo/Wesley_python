import pygame
import random
import time
import os
pygame.init()
W = 1000
H = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("小精靈")
food_img = pygame.transform.scale(pygame.image.load(os.path.join("pac man","food.png")),(10,10))
pacman_img = pygame.transform.scale(pygame.image.load(os.path.join("pac man","pacman.png")),(30,30))
block_img = pygame.transform.scale(pygame.image.load(os.path.join("pac man","block.png")),(64,64))
ghost_img1 = pygame.transform.scale(pygame.image.load(os.path.join("pac man","ghost1.png")),(30,30))
ghost_img2 = pygame.transform.scale(pygame.image.load(os.path.join("pac man","ghost2.png")),(30,30))
ghost_img3 = pygame.transform.scale(pygame.image.load(os.path.join("pac man","ghost3.png")),(30,30))
ghost_img4 = pygame.transform.scale(pygame.image.load(os.path.join("pac man","ghost4.png")),(30,30))
starting_img = pygame.image.load(os.path.join("pac man","start_pacman.png"))
win_sd = pygame.mixer.Sound(os.path.join("pac man","win.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("pac man","lose.wav"))
eat_sd = pygame.mixer.Sound(os.path.join("pac man","pacman_eat.wav"))
block_x = 0
block_y = 0
food_x = 80
food_y = 80
score = 0
ghost_imgs = [ghost_img1,ghost_img2,ghost_img3,ghost_img4]
gxs = [64,600,860,860]
gys = [64,200,64,480]
pygame.display.set_icon(pacman_img)
pygame.mixer.music.load(os.path.join("pac man","pacman_back_sd.wav"))

font_name = os.path.join("pac man","font.ttf")
def draw_text(surf, text, size, x, y,col):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface, text_rect)

def win():
    screen.blit(pygame.transform.scale(block_img,(1220,800)),(-110,-100))
    draw_text(screen,"You win!",200,W/2,270,"green")
    pygame.display.flip()
    win_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

def lose():
    screen.blit(pygame.transform.scale(block_img,(1220,800)),(-110,-100))
    draw_text(screen,"You lose!",200,W/2,270,"red")
    pygame.display.flip()
    lose_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = block_img
        self.rect = self.image.get_rect()
        self.rect.x = block_x
        self.rect.y = block_y
    def update(self):
        if self.rect.colliderect(pacman.rect):
            if pacman.move == "left":
                pacman.rect.x += 1
            if pacman.move == "right":
                pacman.rect.x -= 1
            if pacman.move == "down":
                pacman.rect.y -= 1
            if pacman.move == "up":
                pacman.rect.y += 1

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = food_img
        self.rect = self.image.get_rect()
        self.rect.x = food_x
        self.rect.y = food_y
        self.time = 0
    def update(self):
        global score,eat_sd
        if self.rect.colliderect(pacman.rect):
            score += 1
            eat_sd.play()
            allsp.remove(self)
        if score >= 286:
            time.sleep(1)
            win()

class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pacman_img
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 480
        self.move = "right"
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] == 1:
            self.move = "up"
        elif key[pygame.K_DOWN] == 1:
            self.move = "down"
        elif key[pygame.K_LEFT] == 1:
            self.move = "left"
        elif key[pygame.K_RIGHT] == 1:
            self.move = "right"

        if self.move == "up":
            self.image = pygame.transform.rotate(pacman_img,90)
            self.rect.y -= 1
        if self.move == "down":
            self.image = pygame.transform.rotate(pacman_img,-90)
            self.rect.y += 1
        if self.move == "left":
            self.image = pygame.transform.rotate(pacman_img,180)
            self.rect.x -= 1
        if self.move == "right":
            self.image = pygame.transform.rotate(pacman_img,0)
            self.rect.x += 1

class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ghost_imgs[i]
        self.start_img = self.image
        self.rect = self.image.get_rect()
        self.rect.x = gxs[i]
        self.rect.y = gys[i]
        self.move = ""
        self.time = 0
    def update(self):
        self.time += 1
        if self.time >= 135:
            self.move = random.choice(["up","down","left","right"])
            self.time = 0

        if self.move == "up":
            self.rect.centery -= 1
            if self.rect.centery <= 90:
                self.move = "down"
                self.time = 0
        if self.move == "down":
            self.rect.centery += 1
            if self.rect.centery >= 500:
                self.move = "up"
                self.time = 0
        if self.move == "left":
            self.rect.centerx -= 1
            if self.rect.centerx <= 90:
                self.move = "right"
                self.time = 0
        if self.move == "right":
            self.rect.centerx += 1
            if self.rect.centerx >= 900:
                self.move = "left"
                self.time = 0

        if self.rect.colliderect(pacman.rect):
            time.sleep(1)
            lose()

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
for i in range(15):
    block = Block()
    allsp.add(block)
    block_x += 64
block_y = 510
block_x = 0
for i in range(15):
    block = Block()
    allsp.add(block)
    block_x += 64
block_y = 64
block_x = 0
for i in range(7):
    block = Block()
    allsp.add(block)
    block_y += 64
block_y = 64
block_x = 897
for i in range(7):
    block = Block()
    allsp.add(block)
    block_y += 64

block_img = pygame.transform.scale(pygame.image.load(os.path.join("pac man","block.png")),(90,90))
block_y = 105
block_x = 95

for i in range(3):
    for i in range(6):
        block = Block()
        allsp.add(block)
        block_x += 135
    block_x = 95
    block_y += 135

for i in range(4):
    for i in range(40):
        food = Food()
        allsp.add(food)
        food_x += 20
    food_x = 80
    food_y += 135

food_y = 100
food_x = 80
for i in range(7):
    for i in range(3):
        for i in range(6):
            food = Food()
            allsp.add(food)
            food_y += 20
        food_y += 12
    food_y = 100
    food_x += 132

for i in range(4):
    ghost = Ghost()
    allsp.add(ghost)

pacman = Pacman()
allsp.add(pacman)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("black")
    allsp.update()
    allsp.draw(screen) 
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
exit()