import pygame
import random
import json
import time
import os
pygame.init()
W = 1000
H = 600
GREY = ((110,110,110))
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("恐龍遊戲")
dino_jump_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","dinosaur.png")),(110,110))
dino_run1_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","dinorun1.png")),(100,100))
dino_run2_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","dinorun2.png")),(100,100))
dead_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","dinodead.png")),(100,100))
dino_duck1_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","dinoduck1.png")),(120,65))
dino_duck2_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","dinoduck2.png")),(120,65))
cactus1_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","LargeCactus.png")),(50,80))
cactus2_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","SmallCactus.png")),(120,65))
bird1_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","bird1.png")),(140,60))
bird2_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","bird2.png")),(140,60))
cloud_img = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","cloud.png")),(130,70))
game_over = pygame.transform.scale(pygame.image.load(os.path.join("google dinosaur","gameover.png")),(800,130))
track_img = pygame.image.load(os.path.join("google dinosaur","track.png"))
pygame.display.set_icon(dino_jump_img)
oops_sd = pygame.mixer.Sound(os.path.join("google dinosaur","hurt_sd.wav"))
jump_sd = pygame.mixer.Sound(os.path.join("google dinosaur","jump.wav"))
wlsd = [pygame.mixer.Sound(os.path.join("google dinosaur","win.wav")),pygame.mixer.Sound(os.path.join("google dinosaur","lose.wav"))]
pygame.mixer.music.load(os.path.join("google dinosaur","dino_music.wav"))
track_x1 = 0
track_x2 = 1200
track_y = 450
track_speed = 0
score = 0

with open("google dinosaur/google dinosaur.json","r") as file:
    data = json.load(file)
print(data)

font_name = os.path.join("google dinosaur","pixel_font.ttf")
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
        self.image = dino_run1_img
        self.rect = self.image.get_rect()
        self.rect.centery = 420
        self.rect.centerx = W/2
        self.mode = "run"
        self.time1 = 0
        self.time2 = 0
        self.time3 = 0
    def update(self):
        global track_speed
        key = pygame.key.get_pressed()
        if self.mode == "run":
            self.time1 += 1
            if self.time1 >= 5:
                self.time1 = 0 
                if self.image != dino_run2_img:
                    self.image = dino_run2_img
                elif self.image != dino_run1_img:
                    self.image = dino_run1_img
            if key[pygame.K_UP] == 1:
                jump_sd.play()
                self.time2 = 0
                self.image = dino_jump_img
                self.mode = "jump"
            elif key[pygame.K_DOWN] == 1:
                self.time3 = 0 
                self.image = dino_duck1_img
                self.mode = "duck"

        if self.mode == "duck":
            if key[pygame.K_DOWN] == 1:
                self.rect.centery = 450
                self.time3 += 1        
                if self.time3 >= 5:
                    self.time3 = 0 
                    if self.image != dino_duck2_img:
                        self.image = dino_duck2_img
                    elif self.image != dino_duck1_img:
                        self.image = dino_duck1_img
            else:
                self.rect.centery = 420
                self.mode = "run"
            
        if self.mode == "jump":
            self.time2 += 1
            self.rect.centery -= 24
            if self.time2 >= 10:
                self.time2 = 0
                self.mode = "fall"
        if self.mode == "fall":
            self.time2 += 1
            self.rect.centery += 8
            if self.time2 >= 30:
                self.mode = "run"
                self.image = dino_run1_img

        if self.rect.collidepoint(cactus.rect.centerx,cactus.rect.centery) or self.rect.colliderect(bird.rect) and self.rect.centerx >= bird.rect.centerx and self.image != dead_img:
            self.rect.x -= 10
            self.image = dead_img
            self.dead()
            cactus.speed = 0
            bird.speed = 0
            cloud.speed = 0
            track_speed = 0

    def dead(self):
        oops_sd.play()
        self.mode = "die"
        self.image = dead_img
        allsp.update()
        allsp.draw(screen)
        pygame.display.flip()
        time.sleep(1)

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice([cactus1_img,cactus2_img])
        self.rect = self.image.get_rect()
        self.rect.centery = 430
        self.rect.x = 1000+random.randint(0,200)
        self.speed = 7
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -100:
            self.__init__()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bird1_img
        self.rect = self.image.get_rect()
        self.rect.centery = 350
        self.rect.x = 1000+random.randint(100,200)
        self.time = 0
        self.speed = random.randint(8,12)
        self.show = random.randint(0,1000) 
    def update(self):
        if self.show == 0:
            self.rect.x -= 10
            self.time += 1
            if self.time >= 7:
                self.time = 0
                if self.image != bird1_img:
                    self.image = bird1_img
                elif self.image != bird2_img:
                    self.image = bird2_img
            if self.rect.x <= -100:
                self.__init__()
        else:
            self.__init__()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(cloud_img,(random.randint(110,150),random.randint(110,150)))
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(10,100)
        self.rect.x = 1000+random.randint(0,500)
        self.speed = 7
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -100:
            self.__init__()

pygame.mixer.music.play(-1)

waiting = True
screen.fill("white")
draw_text(screen,"Press key[up] to jump above the cactuses,", 30,W/2, 100,"black")
draw_text(screen,"Press key[down] to duck the birds,", 30,W/2, 140,"black")
draw_text(screen,"Press key[space] to start the game.", 30,W/2, 180,"black")
screen.blit(dino_jump_img,(200,310))
screen.blit(cactus2_img,(500,345))
screen.blit(bird1_img,(800,300))
screen.blit(track_img,(0,400))
pygame.display.flip()
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            waiting = False

allsp = pygame.sprite.Group()
player = Player()
cactus = Cactus()
bird = Bird()
cloud = Cloud()
allsp.add(player)
allsp.add(cactus)
allsp.add(bird)
allsp.add(cloud)

run = True
track_speed = 7
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    track_x1 -= track_speed
    track_x2 -= track_speed
    if track_x1 <= -2500:
        track_x1 = 1000
    if track_x2 <= -2500:
        track_x2 = 1000

    screen.fill("white")
    screen.blit(track_img,(track_x1,track_y))
    screen.blit(track_img,(track_x2,track_y))
    allsp.update()
    allsp.draw(screen)
    score += 1
    draw_text(screen, "score:"+str(score), 30,600, 20,GREY)
    draw_text(screen, "highscore:"+str(data["score"]), 30, 850, 20,GREY)

    if player.mode == "die":
        screen.blit(game_over,(100,200))
        pygame.display.flip()
        if score > data["score"] :
            data["score"] = score
            with open("google dinosaur/google dinosaur.json","w") as file:
                json.dump(data,file)
            draw_text(screen, "You got a new high score!", 50,W/2,H/2+20,GREY)
            wlsd[0].play()
        else:  
            wlsd[1].play()

        pygame.display.flip()    
        time.sleep(5)
        run = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()