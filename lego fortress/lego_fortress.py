import pygame
import random
import time
import os
pygame.init()
W = 1000
H = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("樂高堡壘")
coin_img = pygame.image.load(os.path.join("lego fortress","legocoin.png"))
cheese_img = pygame.image.load(os.path.join("lego fortress","cheese.png"))
mouse_img = pygame.image.load(os.path.join("lego fortress","mouse_img.png"))
player_img = pygame.image.load(os.path.join("lego fortress","lego_man.png"))
playerbrick_img = pygame.image.load(os.path.join("lego fortress","lego_manbrick.png"))
playerbomb_img = pygame.image.load(os.path.join("lego fortress","lego_manbomb.png"))
brick_img = pygame.image.load(os.path.join("lego fortress","legobrick.png"))
bomb_img = pygame.image.load(os.path.join("lego fortress","bomb.png"))
treasure_img = pygame.image.load(os.path.join("lego fortress","treasure.png"))
boom_img = pygame.transform.scale(pygame.image.load(os.path.join("lego fortress","boom.png")),(50,50))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("lego fortress","legoback.png")),(1000,600))
starting_img = pygame.image.load(os.path.join("lego fortress","legostartback.png"))
boom_sd = pygame.mixer.Sound(os.path.join("lego fortress","boom_sd.wav"))
bite_sd = pygame.mixer.Sound(os.path.join("lego fortress","legobite_sd.wav"))
coin_sd = pygame.mixer.Sound(os.path.join("lego fortress","legocoin_sd.wav"))
put_sd = pygame.mixer.Sound(os.path.join("lego fortress","legoput_sd.wav"))
win_sd = pygame.mixer.Sound(os.path.join("lego fortress", "win.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("lego fortress", "lose.wav"))
pygame.mixer.music.load(os.path.join("lego fortress","legoback_sd.wav"))
pygame.display.set_icon(brick_img)
coins = 100
timer = 3660
choice = "bomb"
mhb = False

def win():
    screen.blit(back_img,(0,0))
    draw_text(screen,"You win!",200,W/2,300,"green")
    pygame.display.flip()
    win_sd.play()
    time.sleep(3)
    pygame.quit()
    exit() 

def lose():
    screen.blit(back_img,(0,0))
    draw_text(screen,"You lose!",200,W/2,300,"red")
    pygame.display.flip()
    lose_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

font_name = os.path.join("lego fortress","font.ttf")
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
        mouse = pygame.mouse.get_pos()
        self.image = player_img
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = mouse[0]
        self.rect.centery = mouse[1]
    def update(self):
        global choice
        if choice == "brick":
            self.image = playerbrick_img
            self.image = pygame.transform.scale(self.image,(70,100))
        if choice == "bomb":
            self.image = playerbomb_img
            self.image = pygame.transform.scale(self.image,(70,100))
        if choice == "none":
            self.image = player_img
            self.image = pygame.transform.scale(self.image,(90,100))
        mouse = pygame.mouse.get_pos()
        self.rect.centerx = mouse[0]
        self.rect.centery = mouse[1]

class Cheese(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cheese_img
        self.image = pygame.transform.scale(self.image,(90,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = H/2
    def update(self):
        if self.rect.collidepoint(mouse.rect.center):
            bite_sd.play()
            time.sleep(1)
            lose()

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = brick_img
        self.image = pygame.transform.scale(self.image,(50,30))
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery+10
        self.save = []
    def update(self):
        if self.rect.colliderect(mouse.rect) and not self.rect.colliderect(player.rect):
            mouse.move = False
            if self.image.get_width() > 1:
                self.image = pygame.transform.scale(self.image,(self.image.get_width()-0.00000001,self.image.get_height()-0.00000001))
            else:
                mouse.move = True
                allsp.remove(self)
            self.save = [self.image.get_width(),self.image.get_height()]
            self.image = brick_img
            self.image = pygame.transform.scale(self.image,self.save)
         
class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = mouse_img
        self.size = 100
        self.image = pygame.transform.scale(self.image,(self.size,self.size/2))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice([0,1000])
        self.rect.centery = random.randint(0,600)
        if self.rect.centerx > cheese.rect.centery:
            self.image = pygame.transform.rotozoom(self.image,180,1)
        self.move = True
        self.speed = 1
    def update(self):
        if self.move == True:
            if self.rect.centery < cheese.rect.centery:
                self.rect.centery += self.speed
            elif self.rect.centery > cheese.rect.centery:
                self.rect.centery -= self.speed
            if self.rect.centerx < cheese.rect.centerx:
                self.rect.centerx += self.speed*2
            elif self.rect.centerx > cheese.rect.centerx:
                self.rect.centerx -= self.speed*2

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bomb_img
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery+10
    def update(self):
        if self.rect.colliderect(mouse.rect) and not self.rect.colliderect(player.rect):
            mouse.move = False
            boom_sd.play()
            self.image = boom_img
            allsp.draw(screen)
            pygame.display.update()
            time.sleep(1)
            mouse.__init__()
            allsp.remove(self)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice([coin_img,coin_img,coin_img,coin_img,coin_img,coin_img,coin_img,coin_img,coin_img,treasure_img])
        self.pic = self.image
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(50,950)
        self.rect.centery = random.randint(50,550)
    def update(self):
        global coins
        if self.rect.collidepoint(player.rect.center):
            coin_sd.play()
            if self.pic == coin_img:
                coins += 1
            else:
                coins += 2
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
player = Player()
cheese = Cheese()
mouse = Mouse()
allsp.add(player)
allsp.add(cheese)
allsp.add(mouse)
for i in range(2):
    coin = Coin()
    allsp.add(coin)

run = True
while run:

    if timer <= 0:
        time.sleep(1)
        win()

    timer -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            allsp.remove(player)
            if choice == "brick" and coins >= 1:
                coins -= 1
                brick = Brick()
                allsp.add(brick)
                put_sd.play()
            if choice == "bomb" and coins >= 10:
                coins -= 10
                bomb = Bomb()
                allsp.add(bomb)
                put_sd.play()
            player = Player()
            allsp.add(player)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == 1:
        if choice == "brick" and coins >= 10:
            choice = "bomb"
        elif coins >= 1:
            choice = "brick"   
        time.sleep(0.2)
        pygame.display.update()

    if coins < 10 and coins >= 1:
        choice = "brick"
    elif coins < 1:
        choice = "none"

    allsp.update()
    screen.blit(back_img,(0,0))
    allsp.draw(screen)
    draw_text(screen, "Money: "+str(coins), 30,100, 20,"black")
    draw_text(screen, "brick: coin*1", 30,120, 580,"red")
    draw_text(screen, "bomb: coin*10", 30,350, 580,"brown")
    draw_text(screen, "Timer: "+str(int(timer/60)), 30,900, 20,"black")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()