import pygame
import json
import time
import os
pygame.init()
W = 1000
H = 600
pygame.display.set_caption("射箭遊戲")
screen = pygame.display.set_mode((W, H))
size = 0
shoot = False
shoot_time = 0
bow_pos = 700
bow_img = 0
y = 200
lr = 0
score = 0
chances = 10
plus = 0

with open("bow shooter/bowshooter.json","r") as file:
    data = json.load(file)

starting_img = pygame.image.load(os.path.join("bow shooter","bow_shooter_start.png"))
target_img = pygame.transform.scale(pygame.image.load(os.path.join("bow shooter","target.png")),(W,H))
bow_imgs = [pygame.image.load(os.path.join("bow shooter","bow1.png")),pygame.image.load(os.path.join("bow shooter","bow2.png")),pygame.image.load(os.path.join("bow shooter","bow3.png")),pygame.image.load(os.path.join("bow shooter","bow4.png")),pygame.image.load(os.path.join("bow shooter","bow5.png"))]
pygame.display.set_icon(bow_imgs[0])
shoot_sd = pygame.mixer.Sound(os.path.join("bow shooter","shoot_sd.wav"))
hit_sd = pygame.mixer.Sound(os.path.join("bow shooter","hit_sd.wav"))
scored_sd = pygame.mixer.Sound(os.path.join("bow shooter","scored_sd.wav"))
powering_sd = pygame.mixer.Sound(os.path.join("bow shooter","powering_sd.wav"))
complete_sd = pygame.mixer.Sound(os.path.join("bow shooter","game_complete_sd.wav"))
missed_sd = pygame.mixer.Sound(os.path.join("bow shooter","missed_sd.wav"))
pygame.mixer.music.load(os.path.join("bow shooter","back_sd_shoot_game.wav"))

font_name = os.path.join("bow shooter","font.ttf")
def draw_text(surf, text, size, x, y,col):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface, text_rect)

pygame.mixer.music.play(-1)

start_img = pygame.transform.scale(starting_img, (1500,1000))
screen.blit(start_img, (-250,-205))
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
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and shoot == False:
            shoot = True
            for i in range(3):
                screen.blit(bow_imgs[i],(bow_pos,200))
                bow_pos -= 10
                pygame.display.flip()
                time.sleep(0.2)
                powering_sd.play()
                screen.blit(target_img,(0,0))
            y += 200
            bow_img = 4
            shoot_sd.play()

    if shoot == True:
        size += 90
        target_img = pygame.transform.scale(pygame.image.load(os.path.join("bow shooter","target.png")),(W+size,H+size))
        shoot_time += 1
        if shoot_time >= 50:
            chances -= 1
            hit_sd.play()
            shoot = False
            shoot_time = 0
            time.sleep(1)
            if bow_pos <= 0:
                plus = int(700-bow_pos)
            else:
                plus = int(700-(bow_pos/2-W/2))
            plus = round(abs(plus)/3)
            if plus <= 200:
                plus = 0
            score += plus
            draw_text(screen,"+"+ str(plus), 230, W/2, 250,"black")
            pygame.display.flip()
            if not plus == 0:
                scored_sd.play()
            else:
                missed_sd.play()
            time.sleep(2)
            size = 0
            target_img = pygame.transform.scale(pygame.image.load(os.path.join("bow shooter","target.png")),(W,H))
            screen.blit(target_img,(0,0))
            bow_img = 0
            y = 200

    else:
        if shoot == False:
            if lr == 1:
                bow_pos -= 5
                if bow_pos <= 0:
                    lr = 0
            elif lr == 0:
                bow_pos += 5
                if bow_pos >= 900:
                    lr = 1

    screen.blit(target_img,(0-size/2,0-size/2))
    screen.blit(bow_imgs[bow_img],(bow_pos,y))
    draw_text(screen,"score: "+ str(score), 30, 650, 15,"black")
    draw_text(screen,"highscore: "+ str(data["score"]), 30, 850, 15,"black")
    draw_text(screen,"chances: "+ str(chances), 30, 90, 15,"black")
    pygame.display.flip()

    if chances == 0:
        time.sleep(1)
        screen.fill("grey")
        draw_text(screen,"Game complete!", 100, W/2, 250,"red")
        draw_text(screen,"score: "+ str(score), 50, W/2, 350,"red")

        if score >= data["score"]:
            data["score"] = score
            draw_text(screen,"You got a new high score! ", 20, W/2, 400,"red")
            with open("bow shooter/bowshooter.json","w") as file:
                json.dump(data,file)
        
        pygame.display.flip()
        complete_sd.play()
        time.sleep(5)
        run = False
        
pygame.quit()
exit()