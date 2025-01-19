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
cheese_img = pygame.image.load(os.path.join("lego fortress","cheese.png"))
mouse_img = pygame.image.load(os.path.join("lego fortress","mouse_img.png"))
player_img = pygame.image.load(os.path.join("lego fortress","lego_man.png"))
playerbrick_img = pygame.image.load(os.path.join("lego fortress","lego_manbrick.png"))
playerbomb_img = pygame.image.load(os.path.join("lego fortress","lego_manbomb.png"))
brick_img = pygame.image.load(os.path.join("lego fortress","legobrick.png"))
bomb_img = pygame.image.load(os.path.join("lego fortress","bomb.png"))
boom_img = pygame.transform.scale(pygame.image.load(os.path.join("lego fortress","boom.png")),(50,50))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("lego fortress","legoback.jpg")),(1000,600))
boom_sd = pygame.mixer.Sound(os.path.join("lego fortress","boom_sd.wav"))
pygame.display.set_icon(brick_img)
coin = 100
choice = "brick"
mhb = False

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
        pass

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
            if self.image.get_width() > 20:
                self.image = pygame.transform.scale(self.image,(self.image.get_width()-0.01,self.image.get_height()-0.01))
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
                self.rect.centerx += self.speed
            elif self.rect.centerx > cheese.rect.centery:
                self.rect.centerx -= self.speed

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

allsp = pygame.sprite.Group()
player = Player()
cheese = Cheese()
mouse = Mouse()
allsp.add(player)
allsp.add(cheese)
allsp.add(mouse)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            allsp.remove(player)
            if choice == "brick" and coin >= 1:
                coin -= 1
                brick = Brick()
                allsp.add(brick)
            if choice == "bomb" and coin >= 20:
                coin -= 20
                bomb = Bomb()
                allsp.add(bomb)
            player = Player()
            allsp.add(player)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == 1:
        if choice == "brick" and coin >= 20:
            choice = "bomb"
        elif coin >= 1:
            choice = "brick"   
        time.sleep(0.1)
        pygame.display.update()

    if coin < 20 and coin >= 1:
        choice = "brick"
    elif coin < 1:
        choice = "none"

    allsp.update()
    screen.blit(back_img,(0,0))
    allsp.draw(screen)
    draw_text(screen, "Money: "+str(coin), 30,100, 20,"black")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()