import pygame
import random
import time
import os
pygame.init()
W = 1000
H = 600
press = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("樂高堡壘")
cheese_img = pygame.image.load(os.path.join("lego fortress","cheese.png"))
player_img = pygame.image.load(os.path.join("lego fortress","lego_man.png"))
brick_img1 = pygame.image.load(os.path.join("lego fortress","legobrick.png"))
brick_img2 = pygame.image.load(os.path.join("lego fortress","legobrick2.png"))
brick_img3 = pygame.image.load(os.path.join("lego fortress","legobrick3.png"))
brick_img4 = pygame.image.load(os.path.join("lego fortress","legobrick4.png"))
brick_img5 = pygame.image.load(os.path.join("lego fortress","legobrick5.png"))
brick_img6 = pygame.image.load(os.path.join("lego fortress","legobrick6.png"))
pygame.display.set_icon(brick_img1)
coin = 100

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
        self.image = pygame.transform.scale(self.image,(90,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = mouse[0]
        self.rect.centery = mouse[1]
    def update(self):
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
        self.image = random.choice([brick_img1,brick_img2,brick_img3,brick_img4,brick_img5,brick_img6])
        self.image = pygame.transform.scale(self.image,(50,30))
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery+10
        self.follow = True
    def update(self):
        global press,coin
        if self.follow == True:
            self.rect.centerx = player.rect.centerx
            self.rect.centery = player.rect.centery+10
            if press == True and not self.rect.colliderect(cheese.rect) and coin >:
                coin -= 1
                self.follow = False
                brick = Brick()
                allsp.add(brick)
                pygame.display.update()

allsp = pygame.sprite.Group()
player = Player()
brick = Brick()
cheese = Cheese()
allsp.add(player)
allsp.add(brick)
allsp.add(cheese)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            press = True
            allsp.update()
            press = False

    allsp.update()
    screen.fill("white")
    allsp.draw(screen)
    draw_text(screen, "money: "+str(coin), 30,100, 20,"red")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()