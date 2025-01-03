import pygame
import random
import time
import os

pygame.init()
W = 1000   
H = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("超級對決")

energy = 100
play = True
start_img = pygame.transform.scale(pygame.image.load(os.path.join("super battle","battle_start_img.png")),(1100,800))
p_normal_img = pygame.transform.scale(pygame.image.load(os.path.join("super battle","player_normal.png")),(60,70))
e_normal_img = pygame.transform.scale(pygame.image.load(os.path.join("super battle","enemy_normal.png")),(60,70))
p_attack_img = pygame.transform.scale(pygame.image.load(os.path.join("super battle","player_attack.png")),(75,70))
e_attack_img = pygame.transform.scale(pygame.image.load(os.path.join("super battle","enemy_attack.png")),(75,70))
p_defense_img = pygame.transform.scale(pygame.image.load(os.path.join("super battle","player_defense.png")),(65,70))
e_defense_img = pygame.transform.scale(pygame.image.load(os.path.join("super battle","enemy_defense.png")),(65,70))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("super battle","battle_back.png")),(1010,600))
wlsd = [pygame.mixer.Sound(os.path.join("super battle","win.wav")),pygame.mixer.Sound(os.path.join("super battle","lose.wav"))]
wlbg = pygame.transform.scale(pygame.image.load(os.path.join("super battle","Spotlight.png")),(1000,600))
pygame.display.set_icon(p_normal_img)
burn = pygame.mixer.Sound(os.path.join("super battle","burn_sd.wav"))
sword_sd = pygame.mixer.Sound(os.path.join("super battle","sword.wav"))
sword_sd.set_volume(100)
shield_sd = pygame.mixer.Sound(os.path.join("super battle","shield.wav"))
shield_sd.set_volume(1)
pygame.mixer.music.load(os.path.join("super battle","battle_bgsd.wav"))
pygame.mixer.music.set_volume(0.3)

font_name = os.path.join("super battle","font.ttf")
def draw_text(surf, text, size, x, y,col):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface, text_rect)

def win():
    screen.blit(wlbg,(0,0))
    draw_text(screen,"You win!",200,W/2,H/2,"green")
    pygame.display.flip()
    wlsd[0].play()
    time.sleep(3)
    pygame.quit()
def lose():
    screen.blit(wlbg,(0,0))
    draw_text(screen,"You lose!",200,W/2,H/2,"red")
    pygame.display.flip()
    wlsd[1].play()
    time.sleep(3)
    pygame.quit()
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p_normal_img
        self.rect = self.image.get_rect()
        self.rect.x = W/2-200
        self.rect.y = H/2+110
        self.speed = 2
        self.tmr = 0
    def update(self):
        global energy,play
        key = pygame.key.get_pressed()
        if self.image != p_defense_img:
            if key[pygame.K_LEFT] == 1:
                self.rect.x -= self.speed
                if enemy.rect.colliderect(self.rect):
                    self.rect.x += self.speed
            if key[pygame.K_RIGHT] == 1:
                self.rect.x += self.speed
                if enemy.rect.colliderect(self.rect):
                    self.rect.x -= self.speed

        if key[pygame.K_a] == 1:
            if play == True:
                play = False
                sword_sd.play()
            if energy >= 2:
                energy -= 2
            self.image = p_attack_img
        elif key[pygame.K_s] == 1:
            if play == True:
                play = False
                shield_sd.play()
            self.image = p_defense_img
        else:
            play = True
            self.image = p_normal_img
        if self.rect.colliderect(enemy.rect):
            if (enemy.image == e_attack_img and self.image != p_defense_img) or (enemy.image == e_defense_img and self.image == p_attack_img):
                self.rect.x -= self.speed+random.randint(1,6)
        if self.rect.x <= 100 or self.rect.x >= 850:
            burn.play()
            time.sleep(1)
            lose()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = e_normal_img
        self.rect = self.image.get_rect()
        self.rect.x = W/2+140
        self.rect.y = H/2+110
        self.speed = 1
        self.sword = True
        self.shield = True
    def update(self):
        if not self.rect.colliderect(player.rect):
            self.rect.x -= self.speed
        if self.rect.colliderect(player.rect):
            if player.image == p_attack_img:
                self.image = random.choice([e_defense_img,e_normal_img])
            elif player.image == e_defense_img:
                self.image = e_normal_img
            if player.image == p_attack_img and self.image != e_defense_img:
                self.rect.x += self.speed+random.randint(1,energy+1)
            else:
                self.image = random.choice([e_attack_img])
        if self.rect.x <= 100 or self.rect.x >= 850:
            time.sleep(1)
            win()

allgp = pygame.sprite.Group()
player = Player()
enemy = Enemy()
allgp.add(player)
allgp.add(enemy)   

pygame.mixer.music.play(-1)

screen.blit(start_img, (-50,-100))
pygame.display.update()
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            waiting = False

running = True
while running:

    if energy != 100 and player.image != p_attack_img:
        energy += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(back_img,(0,0))
    allgp.draw(screen)
    allgp.update()
    if energy <= 80:
        draw_text(screen,"{ power:"+str(energy)+" }",20,W/2,H/2,"black")
    else:
        draw_text(screen,"{ power:"+str(energy)+" }",20,W/2,H/2,"red")
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
exit()