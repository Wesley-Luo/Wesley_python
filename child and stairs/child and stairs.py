import pygame
import random
import json
import time
import os

with open("child and stairs/child and stairs.json","r") as file:
    data = json.load(file)

pygame.init()
W = 1000
H = 600
child_img1 = pygame.transform.scale(pygame.image.load(os.path.join("child and stairs","child.png")),(80,80))
child_img2 = pygame.transform.scale(pygame.image.load(os.path.join("child and stairs","child2.png")),(80,80))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("child and stairs","child_stairs_back.png")),(1000,600))
paddle_img = pygame.transform.scale(pygame.image.load(os.path.join("child and stairs","paddle.png")),(100,20))
spike_img = pygame.transform.scale(pygame.image.load(os.path.join("child and stairs","spike.png")),(100,20))
slide_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("child and stairs","slide1.png")),(100,20)),pygame.transform.scale(pygame.image.load(os.path.join("child and stairs","slide2.png")),(100,20))]
starting_img = pygame.image.load(os.path.join("child and stairs","chiild_start_bg.png"))
scream_sd = pygame.mixer.Sound(os.path.join("child and stairs","scream.wav"))
slide_sd = pygame.mixer.Sound(os.path.join("child and stairs","slide.wav"))
edge_sd = pygame.mixer.Sound(os.path.join("child and stairs","ouch.wav"))
end_sd = pygame.mixer.Sound(os.path.join("child and stairs","lose.wav"))
pygame.mixer.music.load(os.path.join("child and stairs","child_back_sd.wav"))
pygame.display.set_caption("小朋友下樓梯")
pygame.display.set_icon(child_img1)
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
fall = True
paddle_num = "first"
speed = 10
pick = 0
lives = 5
score = 0

font_name = os.path.join("child and stairs","font.ttf")
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
        self.image = child_img1
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = 50
    def update(self):
        global speed
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] == 1 and self.rect.x <= 910:
            self.image = child_img1
            self.rect.centerx += speed
        elif key[pygame.K_LEFT] == 1 and self.rect.x >= 10:
            self.image = child_img2
            self.rect.centerx -= speed
        if fall == True:
            self.rect.centery += 3
        if lives <= 0:
            all_sp.remove(self)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global paddle_num
        self.image = paddle_img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,1000)
        self.rect.centery = 600
        if paddle_num =="first":
            self.rect.centerx = W/2
            paddle_num = "after"
    def update(self):
        global speed,score
        if self.rect.colliderect(player.rect) and player.rect.y+85 >= self.rect.centery:
            player.rect.centery = (self.rect.centery - 50)
            speed = 10
        elif not player.rect.centery < (self.rect.centery - 40):
            speed = 2

        self.rect.centery -= 2
        if self.rect.centery <= 0 or lives <= 0:
            score += 1
            all_sp.remove(self)

class Spike(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = spike_img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,1000)
        self.rect.centery = 600
    def update(self):
        global speed,lives,paddle_num
        if self.rect.colliderect(player.rect) and player.rect.y+85 >= self.rect.centery:
            scream_sd.play()
            lives -= 1
            time.sleep(1)
            player.rect.centery = 150
            player.rect.centerx = W/2
            paddle_num = "first"
            all_sp.remove(self)
        self.rect.centery -= 2
        if self.rect.centery <= 0 or lives <= 0:
            all_sp.remove(self)

class Slide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = slide_imgs[random.randint(0,1)]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,1000)
        self.rect.centery = 600
    def update(self):
        global speed,lives
        if self.rect.colliderect(player.rect) and player.rect.y+85 >= self.rect.centery:
            slide_sd.play()
            if self.image == slide_imgs[0]:
                player.rect.x += 5
            else:
                player.rect.x -= 5
            player.rect.centery = (self.rect.centery - 50)
            speed = 10
        elif not player.rect.centery < (self.rect.centery - 40):
            speed = 2
        self.rect.centery -= 2
        if self.rect.centery <= 0 or lives <= 0:
            all_sp.remove(self)

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

run = True
all_sp = pygame.sprite.Group()
player = Player()
paddle = Paddle()
spike = Spike()
slide = Slide()
all_sp.add(player)
all_sp.add(paddle)
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if random.choice([0,0,0,0,0,0,0,0,1]) == 1:
        pick = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,3])
        if pick == 1:
            paddle = Paddle()
            all_sp.add(paddle)
        elif pick == 2:
            spike = Spike()
            all_sp.add(spike)
        elif pick == 3:
            slide = Slide()
            all_sp.add(slide)

    screen.blit(back_img,(0,0))

    all_sp.update()
    all_sp.draw(screen)

    draw_text(screen, "lives: "+str(lives), 30, 60, 50,"white")
    draw_text(screen, "score: "+str(score), 30,200, 50,"white")
    draw_text(screen, "highscore: "+str(data["score"]), 30,880, 50,"white")
    pygame.display.flip()
    clock.tick(60)

    if player.rect.centery < 10 or player.rect.centery >= 550:
        edge_sd.play()
        time.sleep(1)
        lives -= 1
        player.rect.centery = 150
        player.rect.centerx = W/2
        paddle_num = "first"

    if lives <= 0:
        pygame.mixer.music.pause()
        screen.blit(back_img,(0,0))
        draw_text(screen, "lives: "+str(lives), 30, 60, 50,"white")
        draw_text(screen, "score: "+str(score), 30,200, 50,"white")
        draw_text(screen, "Game over!", 150,W/2,H/2,"red")
        if score > data["score"] :
            data["score"] = score
            draw_text(screen, "highscore: "+str(data["score"]), 30,880, 50,"white")
            with open("child and stairs/child and stairs.json","w") as file:
                json.dump(data,file)
            draw_text(screen, "You got a new high score!", 50,W/2,H/2+150,"red")  
        pygame.display.update()
        end_sd.play()
        time.sleep(4)
        run = False

pygame.quit()
exit()