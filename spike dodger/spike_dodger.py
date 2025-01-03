import pygame
import random
import time
import os
pygame.init()
W = 1000
H = 600
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("尖刺閃躲王")

starting_img = pygame.image.load(os.path.join("spike dodger","dodger_start.png"))
spike_img = pygame.transform.scale(pygame.image.load(os.path.join("spike dodger","spike.png")),(100,130))
block_img = pygame.transform.scale(pygame.image.load(os.path.join("spike dodger","block.png")),(120,120))
pyramid_img = pygame.transform.scale(pygame.image.load(os.path.join("spike dodger","pyramid.png")),(100,130))
coin_img = pygame.transform.scale(pygame.image.load(os.path.join("spike dodger","ball_coin.png")),(110,110))
road_img = pygame.transform.scale(pygame.image.load(os.path.join("spike dodger","spike_road.png")),(1050,600))
player_img = pygame.transform.scale(pygame.image.load(os.path.join("spike dodger","spike_player.png")),(100,160))
line_img = pygame.transform.scale(pygame.image.load(os.path.join("spike dodger","line.png")),(10,30))
eat_sd = pygame.mixer.Sound(os.path.join("spike dodger","ate_coin.wav"))
rip_sd = pygame.mixer.Sound(os.path.join("spike dodger","rip.wav"))
ouch_sd = pygame.mixer.Sound(os.path.join("spike dodger","oops.wav"))
win_sd = pygame.mixer.Sound(os.path.join("spike dodger", "win.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("spike dodger", "lose.wav"))
pygame.mixer.music.load(os.path.join("spike dodger","dodger_sd.wav"))
pygame.mixer.music.set_volume(0.3)
pygame.display.set_icon(spike_img)
line_pos = -20
score = 0
lives = 5

font_name = os.path.join("spike dodger","font.ttf")
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
        self.rect.centery = 480
        self.track = 2
        self.jump = False
        self.time = 0
    def update(self):
        global score,lives
        if self.rect.collidepoint(spike1.rect.centerx,spike1.rect.centery):
            ouch_sd.play()
            lives -= 1
            spike1.__init__()
        elif self.rect.collidepoint(spike2.rect.centerx,spike2.rect.centery):
            ouch_sd.play()   
            lives -= 1                                                                                                               
            spike2.__init__()
        if self.rect.collidepoint(coin.rect.centerx,coin.rect.centery):
            score += 1
            coin.__init__()
            eat_sd.play()

class Spike1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice([block_img,spike_img,pyramid_img])
        self.rect = self.image.get_rect()
        self.rect.centery = random.randint(-400,-40)
        self.rect.centerx = random.choice([400,500,600])
        self.road = self.rect.centerx
    def update(self):
        if self.road == spike2.road:
            self.__init__()
        if self.rect.centery < 700:
            self.rect.centery += 10
            if self.rect.centery > -20:
                if self.road == 400:
                    self.rect.centerx -= 4
                elif self.road == 600:
                    self.rect.centerx += 4
        else:
            self.__init__()

class Spike2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice([block_img,spike_img,pyramid_img])
        self.rect = self.image.get_rect()                         
        self.rect.centery = random.randint(-400,-40)
        self.rect.centerx = random.choice([400,500,600])
        self.road = self.rect.centerx
    def update(self):
        if self.road == spike1.road:
            self.__init__()
        if self.rect.centery < 700:
            self.rect.centery += 10
            if self.rect.centery > -20:
                if self.road == 400:
                    self.rect.centerx -= 4
                elif self.road == 600:
                    self.rect.centerx += 4
        else:
            self.__init__()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.centery = random.randint(-200,-40)
        self.rect.centerx = random.choice([400,500,600])
        self.road = self.rect.centerx
        if self.road == spike1.road or self.road == spike2.road:
            self.__init__()
    def update(self):
        if self.rect.centery < 700:
            self.rect.centery += 10
            if self.rect.centery > -20:
                if self.road == 400:
                    self.rect.centerx -= 4
                elif self.road == 600:
                    self.rect.centerx += 4
        else:
            self.__init__()

class Line(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global line_pos
        self.image = line_img
        self.rect = self.image.get_rect()
        self.rect.centery = line_pos
        self.rect.centerx = 500
        self.size = 0
    def update(self):
        self.size += 0.5
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("spike dodger","line.png")),(10+self.size,30+self.size))
        if self.rect.centery < 700:
            self.rect.centery += 10
        else:
            self.rect.centery = -20
        if self.rect.centery > 650:
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

allsp = pygame.sprite.Group()
for i in range(10):
    line = Line()
    allsp.add(line)
    line_pos += 80
player = Player()
spike1 = Spike1()
spike2 = Spike2()
coin = Coin()
allsp.add(player)
allsp.add(spike1)
allsp.add(spike2)
allsp.add(coin)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and player.track < 3:
                rip_sd.play()
                player.rect.centerx += 300
                player.track += 1
            elif event.key == pygame.K_LEFT and player.track > 1:
                rip_sd.play()
                player.rect.centerx -= 300
                player.track -= 1

    screen.fill("green")
    screen.blit(road_img,(0,0))

    allsp.update()
    allsp.draw(screen)

    draw_text(screen, "score: "+str(score), 30,70, 20,"black")
    draw_text(screen, "lives: "+str(lives), 30,200, 20,"black")
    pygame.display.flip()

    if score >= 50:
        time.sleep(2)
        screen.fill("grey")
        draw_text(screen,"You win!", 200, W/2, H/2,"dark green")
        pygame.display.update()
        win_sd.play()
        time.sleep(3)
        run = False
    elif lives <= 0:
        time.sleep(2)
        screen.fill("grey")
        draw_text(screen,"You lose!", 200, W/2, H/2,"red")
        pygame.display.update()
        lose_sd.play()
        time.sleep(3)
        run = False

    clock.tick(60)

pygame.quit()
exit()