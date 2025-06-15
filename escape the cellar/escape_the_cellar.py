import pygame
import random
import math
import time
import os
pygame.init()
clock = pygame.time.Clock()

W = 1200
H = 800
TOTAL = 20
setx = 50   
sety = 0
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("地窖逃生記")

backpack_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","backpack.png")),(50,380))
player_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","player.png")),(40,40))
player2_img = pygame.transform.flip(player_img,True,False)
player_walk_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","player_walk.png")),(40,40))
player_walk2_img = pygame.transform.flip(player_walk_img,True,False)
wall1_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","wall1.png")),(50,50))
wall2_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","wall2.png")),(50,50))
wall3_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","wall3.png")),(50,50))
stone_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","stone.png")),(50,50))
bomb_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","tnt.png")),(50,52))
boom_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boom.png")),(70,70))
box_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","box.png")),(40,40))
web_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","web.png")),(50,50))
brick_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","brick.png")),(50,50))
bat_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","bat.png")),(40,40))
batfly_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","batfly.png")),(40,40))
bat2_img = pygame.transform.flip(bat_img,True,False)
batfly2_img = pygame.transform.flip(batfly_img,True,False)
gun_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","gun.png")),(40,30))
gun2_img = pygame.transform.flip(gun_img,True,False)
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","bullet.png")),(11,11))
aim_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","aim.png")),(60,60))
aim2_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","aim2.png")),(50,50))
blood_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","blood.png")),(50,50))
boxgun_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxgun.png")),(600,600))
shield_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","shield.png")),(30,30))
shield2_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","shield2.png")),(40,40))
boxshield_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxshield.png")),(600,600))
dark_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","dark.png")),(4000,3000))
potion_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","potion.png")),(20,30))
boxpotion_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxpotion.png")),(600,600))
poison_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","poison.png")),(20,30))
boxpoison_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxpoison.png")),(600,600))
smoke_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","smoke.png")),(1200,800))
drink_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","drink.png")),(20,30))
boxdrink_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxdrink.png")),(600,600))
choose_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","choose.png")),(27,27))
dead_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","dead.png")),(600,550))
dead_img.set_alpha(0)
heal_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","heal.png")),(60,60))
speed_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","speed.png")),(60,60))
scissors_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","scissor.png")),(20,30))
boxscissors_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxscissors.png")),(600,600))
darkweb_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","darkweb.png")),(50,50))
hammer_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","hammer.png")),(100,120))
slimey_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","slimy.png")),(30,30))
boxhammer_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxhammer.png")),(600,600))
darkbomb_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","darkbomb.png")),(50,50))
boxslimey_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxslimey.png")),(600,600))
ladder_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","ladder.png")),(10,30))
boxladder_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","boxladder.png")),(600,600))
bigladder_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","bigladder.png")),(50,750))
end_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","end.png")),(1200,800))
floor_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","floor.png")),(1200,10))
start1_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","start1.png")),(200,100))
start2_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","start2.png")),(200,100))
pause1_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","pause1.png")),(30,30))
pause1_2_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","pause1.png")),(40,40))
pause2_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","pause2.png")),(30,30))
pause2_2_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","pause2.png")),(40,40))
start_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","start.png")),(1200,805))
heal_img.set_alpha(100)
speed_img.set_alpha(100)

dust1_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","dust1.png")),(20,20))
dust2_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","dust2.png")),(20,20))
dust3_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","dust3.png")),(20,20))
dust4_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","dust4.png")),(20,20))

walk_sd = pygame.mixer.Sound(os.path.join("escape the cellar","walk.wav"))
jump_sd = pygame.mixer.Sound(os.path.join("escape the cellar","jump.wav"))
bite_sd = pygame.mixer.Sound(os.path.join("escape the cellar","bite.wav"))
shoot_sd = pygame.mixer.Sound(os.path.join("escape the cellar","shoot.wav"))
cymbal_sd = pygame.mixer.Sound(os.path.join("escape the cellar","cymbal.wav"))
defense_sd = pygame.mixer.Sound(os.path.join("escape the cellar","defense.wav"))
boom_sd = pygame.mixer.Sound(os.path.join("escape the cellar","boom.wav"))
put_sd = pygame.mixer.Sound(os.path.join("escape the cellar","put.wav"))
magic_sd = pygame.mixer.Sound(os.path.join("escape the cellar","magic.wav"))
poison_sd = pygame.mixer.Sound(os.path.join("escape the cellar","poison.wav"))
box_sd = pygame.mixer.Sound(os.path.join("escape the cellar","box.wav"))
desw_sd = pygame.mixer.Sound(os.path.join("escape the cellar","desw.wav"))
desb_sd = pygame.mixer.Sound(os.path.join("escape the cellar","desb.wav"))
dun_sd = pygame.mixer.Sound(os.path.join("escape the cellar","dun.wav"))
glue_sd = pygame.mixer.Sound(os.path.join("escape the cellar","glue.wav"))
climb_sd = pygame.mixer.Sound(os.path.join("escape the cellar","climb.wav"))
change_sd = pygame.mixer.Sound(os.path.join("escape the cellar","change.wav"))
level_sd = pygame.mixer.Sound(os.path.join("escape the cellar","level.wav"))
din_sd = pygame.mixer.Sound(os.path.join("escape the cellar","din.wav"))
winner_sd = pygame.mixer.Sound(os.path.join("escape the cellar","winner.wav"))

pygame.mixer.music.load(os.path.join("escape the cellar","backsound.wav"))
pygame.display.set_icon(player_img)

LEVEL20 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
level = 1
press = False
pause = False
reallevel = 1
levelcol = (255,255,255)
levelcolindex = 0
touch = 0
stand = 1
havegun = 0
haveshield = 0
havepotion = 0
havedark = 0
havepoison = 0
havedrink = 0
havescissors = 0
havehammer = 0
haveslimey = 0
haveladder = 0
have = []
have1 = []
have2 = []

select = ["gun","shield","potion","poison","drink","scissors","hammer","slimey","ladder"]
ins = ["Click mouse to shoot bullets.","Press space to defense.","Press d to drink potion if you are bitten by a bat.","Press d to drink the sports drink, you can jump higher and run faster for 15 seconds.","Press mouse to throw the poisonous smoke.","Choose a spider web and press mouse to cut it.","Choose a TNT and press mouse to destroy it.","Choose a block and press mouse to put the slimy glue.","Choose a block and press mouse to put the ladder."]
instr = ""
carry = ""
refreshdown = False
refreshtime = 0
chra = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,4,4,4,4]

font_name = os.path.join("escape the cellar","pixel_font.ttf")
def draw_text(text, size, x, y,col,alpha):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    text_surface.set_alpha(alpha)
    screen.blit(text_surface, text_rect)

def win():
    time.sleep(0.5)
    screen.blit(end_img,(0,0))
    pygame.display.flip()
    pygame.mixer.music.stop()
    winner_sd.play()
    time.sleep(7)
    pygame.quit()
    exit()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 5
        self.time = 0
        self.time2 = 0
        self.time3 = 0
        self.jump = 0
        self.super = 0
        self.start = 1
        self.image.set_alpha(1)
    def update(self):
        global touch,have,refreshdown,refresh,ladder,haveladder,slimey,webgp,shield,havedark,reallevel
        if pause == False:
            if self.start == 1:
                pygame.time.delay(2)
                self.image.set_alpha(1)
                for i in range(127):
                    self.image.set_alpha(i*2)
                    pygame.time.delay(1)
                    allsp.draw(screen)
                    pygame.display.update()
                self.start = 0
                self.image.set_alpha(255)

            if refreshdown == False:
                key = pygame.key.get_pressed()
                if touch == 0 and self.jump == 0 or stand == 0 and not (self.rect.colliderect(ladder.rect) and haveladder == 0) and not self.rect.colliderect(bigladder.rect):
                    self.rect.centery += 4
                self.walk()
                if key[pygame.K_UP] and (touch == 1 or self.rect.y > 750) and not (self.rect.colliderect(ladder.rect) and haveladder == 0) and not self.rect.colliderect(bigladder.rect):
                    self.jump = 1
                    touch = 0
                if self.rect.colliderect(ladder.rect) and haveladder == 0:
                    if key[pygame.K_UP]:
                        climb_sd.play()
                        self.rect.y -= 5
                    elif key[pygame.K_DOWN]:
                        climb_sd.play()
                        self.rect.y += 5
                else:
                    if key[pygame.K_LEFT]:
                        self.rect.x -= self.speed+self.super
                    if key[pygame.K_RIGHT]:
                        self.rect.x += self.speed+self.super
                    if self.jump == 1:
                        self.jumpup()
                    if self.rect.x <= 50:
                        self.rect.x = 51
                    if self.rect.x >= 1110:
                        self.rect.x = 1109
                    if self.rect.y <= -20 and level < TOTAL:
                        reallevel += 1
                        self.rect.centerx = W/2+20
                        self.rect.y = 750
                        self.start = 1
                        level_sd.play()
                        time.sleep(0.3)
                        refreshdown = True
                        self.image.set_alpha(1)
                        refresh()
                        allsp.remove(self)
                    if self.rect.y > 760:
                        self.rect.y = 760
                    for _ in pygame.sprite.spritecollide(self,webgp,False):
                        if not self.jump == 1:
                            self.speed = 1
                        if self.jump == 1:
                            self.speed = 5
                    if shield.shield == True:
                        self.speed = 2
                    if havedark == 1:
                        self.speed = 4
                    if not pygame.sprite.spritecollide(self,webgp,False) and not shield.shield == True and not self.speed == 10 and not self.rect.colliderect(slimey.rect):
                        self.speed = 5
                    if self.rect.colliderect(slimey.rect) and slimey.put != [0,0]:
                        self.speed = 4
                    if self.rect.y <= 755:
                        self.rect.y += self.speed
                    if not self.time3 <= 0:
                        self.time3 -= 1
                        if self.time3 <= 1:
                            draw_text("Supermode ends.", 30, W/2, 30, "red", 255)
                            pygame.display.flip()
                            pygame.time.delay(1000)
                    else:
                        self.time3 = 0
                        self.super = 0
                        pygame.display.flip()
    def walk(self):
        ky = pygame.key.get_pressed()
        if ky[pygame.K_LEFT] or ky[pygame.K_RIGHT]:
            if self.rect.y <= 760:
                dust()
            self.time += 1
            if self.time >= 10:
                self.time = 0
                if ky[pygame.K_RIGHT]:
                    walk_sd.play()
                    if self.image == player_img:
                        self.image = player_walk_img
                    else:
                        self.image = player_img
                else:
                    walk_sd.play()
                    if self.image == player2_img:
                        self.image = player_walk2_img
                    else:
                        self.image = player2_img
    def jumpup(self):
        global touch
        self.rect.y -= 4*self.speed
        self.time2 += 1
        if self.time2 >= 2.1*self.speed*(self.super/3+1) and not self.rect.colliderect(ladder.rect) and not self.rect.colliderect(bigladder.rect):
            self.time2 = 0
            self.jump = 0
            jump_sd.play()

class Dust(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagelist = [dust1_img,dust2_img,dust3_img,dust4_img]
        self.choose = (round(player.time2/2))%3
        self.image = self.imagelist[self.choose].convert_alpha()
        self.rect = self.image.get_rect()
        if player.image == player_img or player.image == player_walk_img:
            self.rect.x = player.rect.centerx-30
        else:
            self.rect.x = player.rect.centerx+30
        self.rect.y = player.rect.centery+random.randint(-10,10)
        self.time = 0
        self.gg = 1
        self.image.set_alpha(100)
    def update(self):
        self.gg = 1
        for i in pygame.sprite.spritecollide(self,stonegp,False):
            self.gg = 0
        self.time += 1
        if self.time <= 50:
            self.image.set_alpha(200-self.time*4)
        else:
            self.gg = 1
        if self.gg == 1:
            self.image.set_alpha(100)
            self.kill()
def dust():
    if refreshdown == False:
        dust = Dust()
        allsp.add(dust)

class Bat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bat_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50,1100)
        self.rect.y = random.randint(0,750)
        self.dir = random.choice(["l","r"])
        self.time = 0
        self.fall = False
        self.speed = 10
    def update(self):
        global allsp,player,bullet,haveshield,havedark
        if pause == False:
            if refreshdown == True:
                self.kill()

            if self.fall == False:
                self.time += self.speed
                if self.dir == "l":
                    self.image = bat_img
                else:
                    self.image = bat2_img
                if self.time >= 20:
                    self.time = 0
                    if self.image == bat_img:
                        self.image = batfly_img
                    elif self.image == batfly_img:
                        self.image = bat_img
                    if self.image == bat2_img:
                        self.image = batfly2_img
                    elif self.image == batfly2_img:
                        self.image = bat2_img
                if self.dir == "l":
                    self.rect.x -= self.speed/5
                else:
                    self.rect.x += self.speed/5
                if self.dir == "l" and self.rect.x <= 51:
                    self.dir = "r"
                elif self.dir == "r" and self.rect.x >= 1109:
                    self.dir = "l"
                self.rect.y += random.randint(0-self.speed,self.speed)
                if self.rect.y <= 0 or self.rect.y >= 760:
                    self.kill()
                if self.rect.colliderect(player.rect) and shield.shield == False and self.speed != 0:
                    bite_sd.play()
                    self.image = blood_img.convert_alpha()
                    self.rect = self.image.get_rect()
                    self.rect.centerx = player.rect.centerx
                    self.rect.centery = player.rect.centery
                    for i in range(100):
                        self.image = pygame.transform.rotozoom(blood_img,0,1+i/70)
                        self.rect = self.image.get_rect()
                        self.rect.centerx = player.rect.centerx
                        self.rect.centery = player.rect.centery
                        allsp.draw(screen)
                        pygame.time.delay(1)
                        pygame.display.flip()
                    for j in range(127):
                        self.image.set_alpha(255-j*2)
                        allsp.draw(screen)
                        pygame.time.delay(1)
                        pygame.display.flip()
                    havedark = 1
                    dark.time += 255
                    self.kill()
                if self.rect.colliderect(bullet.rect) or self.rect.colliderect(shield.rect) and shield.shield == True:
                    if self.rect.colliderect(bullet.rect):
                        cymbal_sd.play()
                    else:
                        defense_sd.play()
                    self.fall = True
                    bullet.rect.x = -50
                    bullet.rect.y = -50
                if self.rect.colliderect(poison.rect) or (abs(self.rect.y - poison.rect.centery) <=100 and abs(self.rect.x - poison.rect.centerx)<= 100 and poison.smoke == True):
                    self.fall = True
                if abs(self.rect.centery - slimey.rect.centery) < 75 and abs(self.rect.centerx - slimey.rect.centerx) < 75 and slimey.put != [0,0]:
                    if self.speed != 0:
                        glue_sd.play()
                        self.speed = 0
            if self.fall == True:
                if self.rect.y >= 770:
                    self.kill()
                else:
                    self.image = pygame.transform.flip(bat_img,False,True)
                    self.rect.y += 5
        
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice([wall1_img,wall2_img,wall3_img])
        self.rect = self.image.get_rect()
        self.rect.x = setx
        self.rect.y = sety
    def update(self):
        if pause == False:
            if refreshdown == True:
                self.rect.y += 2
                if self.rect.y >= 800:
                    self.kill()

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = brick_img
        self.rect = self.image.get_rect()
        self.rect.x = setx
        self.rect.y = sety
    def update(self):
        if pause == False:
            if refreshdown == True:
                self.rect.y += 2
                if self.rect.y >= 800:
                    self.kill()

class Stone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = stone_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = setx
        self.rect.y = sety
    def update(self):
        global touch,have2,haveslimey,haveladder
        if pause == False:
            mpos = pygame.mouse.get_pos()
            if self.rect.y == 750 and (self.rect.x >= 550 and self.rect.x <= 750) and refreshdown == False and level < TOTAL:
                self.kill()

            if pygame.sprite.collide_rect(self,player) and not (player.rect.colliderect(ladder.rect) and haveladder == 0):
                touch = 1
                player.rect.y -= 5
                if self.rect.y < player.rect.centery-40:
                    player.rect.y += 30 
                    player.jump = 0
                    dust()
                if abs(self.rect.centery - player.rect.centery) <= 20:
                    if self.rect.centerx < player.rect.centerx:
                        player.rect.x += 10
                    if self.rect.centerx > player.rect.centerx:
                        player.rect.x -= 10
                player.jump = 0
            if not self.rect.y == 750 and not self.rect.y == 0:
                if abs(mpos[0]-self.rect.centerx) < 25 and abs(mpos[1]-self.rect.centery) < 25 and (carry == "slimey" or carry == "ladder") and refreshdown == False:   
                    self.image.set_alpha(150)
                    if mouse_click[0] and haveslimey == 1 and carry == "slimey":
                        put_sd.play()
                        slimey.put = [self.rect.centerx,self.rect.centery]
                        haveslimey = 0
                        have.remove("slimey")
                        have2.remove("slimey")
                        time.sleep(0.1)
                    elif mouse_click[0] and haveladder == 1 and carry == "ladder":
                        put_sd.play()
                        ladder.put = [self.rect.centerx,self.rect.centery]
                        haveladder = 0
                        have.remove("ladder")
                        have2.remove("ladder") 
                        time.sleep(0.1) 
                else:
                    self.image.set_alpha(255)
            if refreshdown == True:
                self.rect.y += 2
                if self.rect.y >= 800:
                    self.kill()
                
class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bomb_img
        self.rect = self.image.get_rect()
        self.rect.x = setx
        self.rect.y = sety
        self.collide = 0
        if sety > 650 and reallevel < TOTAL:
            self.kill()
    def update(self):
        global player,run,reallevel
        if pause == False:
            for i in pygame.sprite.spritecollide(self,stonegp,False):
                self.collide = 1
            if self.collide == 0 and self.rect.y > 0 and reallevel != TOTAL:
                self.kill()
            self.collide = 0
            if self.rect.y > 0 and refreshdown == False and level < TOTAL:
                if self.rect.y > 650:
                    self.kill()
            if refreshdown == False:
                if pygame.sprite.collide_rect(self,player) and abs(self.rect.centery - player.rect.centery) < 30 and abs(self.rect.centerx - player.rect.centerx) < 30 and self.rect.y < 750:
                    self.rect.y -= 10
                    self.rect.x -= 10
                    self.image = boom_img
                    boom_sd.play()
                    for i in range(120):
                        self.image.set_alpha(215-i*2)
                        allsp.draw(screen)
                        pygame.display.flip()
                    dead_img.set_alpha(215)
                    dun_sd.play()
                    if level < TOTAL:
                        player.rect.centerx = W/2+20
                        player.rect.y = 755
                    else:
                        player.rect.centerx = 70
                        player.rect.y = 705
                    screen.blit(dead_img,(300,100))
                    pygame.display.flip()
                    time.sleep(2)
                    dead_img.set_alpha(0)
                    self.kill()
                if havehammer == 1 and carry == "hammer" and self.rect.colliderect(hammer.rect):
                    self.image = darkbomb_img
                    if mouse_click[0]:
                        desb_sd.play()
                        if player.image == player_img or player.image == player_walk_img:
                            hammer.image = pygame.transform.rotozoom(hammer_img,-60,1)
                        else:
                            hammer.image = pygame.transform.rotozoom(hammer_img,60,1)
                        for i in range(60):
                            self.image.set_alpha(215-i*4)
                            allsp.draw(screen)
                            pygame.display.flip()
                        self.image.set_alpha(255)
                        self.kill()
                else:
                    self.image = bomb_img
                    self.image.set_alpha(255)
            if refreshdown == True:
                self.rect.y += 2
                if self.rect.y >= 800:
                    self.kill()
            if run == False:
                self.rect.x = -50
                self.rect.y = -50
                self.kill()

class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = box_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = setx+5
        self.rect.y = sety+12
        self.collide = 0
        self.random = ""
    def update(self):
        global havegun,haveshield,havepotion,havepoison,havedrink,havescissors,havehammer,haveslimey,haveladder,select,have
        if pause == False:
            if refreshdown == True:
                self.rect.y += 2
                if self.rect.y >= 800:
                    allsp.remove(self)
                if self.rect.y >= 500 and (self.rect.x >= 550 and self.rect.x <= 750):
                    allsp.remove(self)
            for i in pygame.sprite.spritecollide(self,stonegp,False):
                self.collide = 1
            if self.collide == 0:
                allsp.remove(self)
                box = Box()
                allsp.add(box)
            if self.rect.colliderect(player.rect) and select != []:
                if self.collide == 1:
                    self.random = random.choice(select)
                else:
                    allsp.remove(self)
            if self.rect.colliderect(player.rect) and select == []:
                draw_text("Your backpack is too full.", 30, W/2, 30, "red", 255)
            self.collide = 0
            if refreshdown == False and select != [] and self.random != "":
                box_sd.play()
                if self.random == "gun":
                    select.remove("gun")
                    boxgun_img.set_alpha(215)
                    screen.blit(boxgun_img,(300,100))
                    havegun = 1
                    have.append("gun")
                    have1.append("gun")
                    self.remove()
                elif self.random == "shield":
                    select.remove("shield")
                    boxshield_img.set_alpha(215)
                    screen.blit(boxshield_img,(300,100))
                    haveshield = 1
                    have.append("shield")
                    have1.append("shield")
                    self.remove()
                elif self.random == "potion":
                    select.remove("potion")
                    boxpotion_img.set_alpha(215)
                    screen.blit(boxpotion_img,(300,100))
                    havepotion = 1
                    have.append("potion")
                    have2.append("potion")
                    self.remove()
                elif self.random == "poison":
                    select.remove("poison")
                    boxpoison_img.set_alpha(215)
                    screen.blit(boxpoison_img,(300,100))
                    havepoison = 1
                    have.append("poison")
                    have2.append("poison")
                    self.remove()
                elif self.random == "drink":
                    select.remove("drink")
                    boxdrink_img.set_alpha(215)
                    screen.blit(boxdrink_img,(300,100))
                    havedrink = 1
                    have.append("drink")
                    have2.append("drink")
                    self.remove()
                elif self.random == "scissors":
                    select.remove("scissors")
                    scissors_img.set_alpha(215)
                    screen.blit(boxscissors_img,(300,100))
                    havescissors = 1
                    have.append("scissors")
                    have1.append("scissors")
                    self.remove()
                elif self.random == "hammer":
                    select.remove("hammer")
                    scissors_img.set_alpha(215)
                    screen.blit(boxhammer_img,(300,100))
                    havehammer = 1
                    have.append("hammer")
                    have1.append("hammer")
                    self.remove()
                elif self.random == "slimey":
                    select.remove("slimey")
                    slimey_img.set_alpha(215)
                    screen.blit(boxslimey_img,(300,100))
                    haveslimey = 1
                    have.append("slimey")
                    have2.append("slimey")
                    self.remove()
                elif self.random == "ladder":
                    select.remove("ladder")
                    slimey_img.set_alpha(215)
                    screen.blit(boxladder_img,(300,100))
                    haveladder = 1
                    have.append("ladder")
                    have2.append("ladder")
                    self.remove()
    def remove(self):
        pygame.display.update()
        time.sleep(1.5)
        for i in range(120):
            self.image.set_alpha(215-i*2)
            allsp.draw(screen)
            pygame.display.flip()
        self.kill()

            
class Web(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = web_img
        self.rect = self.image.get_rect()
        self.rect.x = setx
        self.rect.y = sety
        self.collide = 0
        self.image.set_alpha(255)
    def update(self):
        if pause == False:
            if abs(self.rect.y - 750) < 10 and (self.rect.x >= 550 and self.rect.x <= 750):
                self.rect.x = -50
                self.rect.y = -50
                allsp.remove(self)
            if havescissors == 1 and carry == "scissors" and self.rect.colliderect(player.rect):
                darkweb_img.set_alpha(255)
                self.image = darkweb_img
                if mouse_click[0]:
                    desw_sd.play()
                    for i in range(60):
                        self.image.set_alpha(215-i*4)
                        allsp.draw(screen)
                        pygame.display.flip()
                    self.rect.x = -100
                    self.rect.y = -100
                    allsp.remove(self)
            else:
                self.image = web_img
                self.image.set_alpha(255)
            if refreshdown == True:
                self.rect.y += 2
                if self.rect.y >= 800:
                    webgp.remove(self)
                    allsp.remove(self)
            
class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = gun_img
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = -50
    def update(self):
        global havegun,mouse_pos,carry
        if pause == False:
            if havegun == 1 and carry == "gun":
                self.rect.centery = player.rect.centery
                if mouse_pos[0] >= player.rect.centerx:
                    self.image = gun2_img
                    self.rect.centerx = player.rect.centerx+30
                else:
                    self.image = gun_img
                    self.rect.centerx = player.rect.centerx-20
            else:
                self.rect.x = -50
                self.rect.y = -50

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = -50
        self.shoot = 0
        self.spx = 0
        self.spy = 0
    def update(self):
        global mouse_click,havegun,mouse_pos,carry
        if pause == False:
            if mouse_click[0] and havegun == 1 and self.shoot == 0 and carry == "gun"and not pygame.sprite.collide_rect(player,aim) and refreshdown == False:
                shoot_sd.play()
                self.rect.x = gun.rect.centerx
                self.rect.y = gun.rect.centery-10
                self.shoot = 1
                self.spx = (aim.rect.centerx - self.rect.centerx)/15
                self.spy = (aim.rect.centery - self.rect.centery)/15
            if self.shoot == 1:
                self.rect.centerx += self.spx
                self.rect.centery += self.spy
                if self.rect.colliderect(aim.rect) or self.rect.x <= 0 or self.rect.x >= 1200 or self.rect.y <= 0 or self.rect.y >= 800:
                    self.shoot = 0
                    self.rect.x = -50
                    self.rect.y = -50 

class Aim(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = aim_img
        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = -200
    def update(self):
        global mouse_pos,havegun,carry
        if pause == False:
            if havegun == 1 and bullet.shoot == 0 and carry == "gun" and refreshdown == False:
                self.rect.centerx = mouse_pos[0]
                self.rect.centery = mouse_pos[1]
            else:
                self.rect.x = -200
                self.rect.y = -200

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = shield_img
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100
        self.shield = False
    def update(self):
        global haveshield,carry
        if pause == False:
            if haveshield == 1 and carry == "shield":
                self.rect.centerx = player.rect.centerx
                if player.image == player_img or player.image == player_walk_img:
                    self.rect.centerx = player.rect.centerx + 10
                elif player.image == player2_img or player.image == player_walk2_img:
                    self.rect.centerx = player.rect.centerx - 10
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    self.image = shield2_img
                    self.shield = True
                else:
                    self.image = shield_img
                    self.shield = False
                self.rect.centery = player.rect.centery
            else:
                self.rect.x = -100
                self.rect.y = -100

class Dark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = dark_img
        self.rect = self.image.get_rect()
        self.rect.x = -10000
        self.rect.y = -10000
        self.time = 255
        self.speed = 0.5
    def update(self):
        global havedark
        if pause == False:
            if havedark == 1:
                self.speed = self.time/510
                self.time -= self.speed
                self.rect.centerx = player.rect.centerx
                self.rect.centery = player.rect.centery
                self.image.set_alpha(self.time)
                if self.time <= 0:
                    havedark = 0
                    self.time = 0
            else:
                self.rect.x = -10000000
                self.rect.y = -10000000
                self.speed = self.time/510
            if refreshdown == True:
                self.time = 0

class Potion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = potion_img
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100
    def update(self):
        global havepotion,havedark,select,carry
        if pause == False:
            key = pygame.key.get_pressed()
            if havepotion == 1 and key[pygame.K_d] and havedark == 1 and carry == "potion":
                draw_text("healing...", 30, W/2, 30, "red", 255)
                pygame.display.flip()
                pygame.time.delay(1000)
                dark.time = 0
                havepotion = 0
                select.append("potion")
                have.remove("potion")
                have2.remove("potion")
                screen.blit(heal_img,(player.rect.x-20,player.rect.y-20))
                magic_sd.play()
                pygame.display.flip()
                pygame.time.delay(1000)
            if havepotion == 1 and carry == "potion":
                self.rect.centerx = player.rect.centerx
                self.rect.centery = player.rect.centery
            else:
                self.rect.centerx = -100
                self.rect.centery = -100

class Poison(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = poison_img
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100
        self.shoot = 0
        self.spx = 0
        self.spy = 0
        self.time = 0
        self.smoke = False
    def update(self):
        global havepoison,select,mouse_click,mouse_pos,have,have2,carry
        if pause == False:
            if havepoison == 1 and carry == "poison":
                if self.shoot == 0 and self.smoke == False:
                    self.rect.centerx = player.rect.centerx
                    self.rect.centery = player.rect.centery
                if mouse_click[0] and self.shoot == 0 and self.smoke == False: 
                    self.rect.centerx = player.rect.centerx
                    self.rect.centery = player.rect.centery
                    self.shoot = 1
                    self.spx = (aim2.rect.centerx - self.rect.centerx)/25
                    self.spy = (aim2.rect.centery - self.rect.centery)/25
                if self.shoot == 1:
                    self.rect.centerx += self.spx
                    self.rect.centery += self.spy 
                    if abs(self.rect.centerx - aim2.rect.centerx) + abs(self.rect.centery - aim2.rect.centery) <= 10 or self.rect.x <= 0 or self.rect.x >= 1200 or self.rect.y <= 0 or self.rect.y >= 800:
                        poison_sd.play()
                        self.shoot = 0
                        self.image = smoke_img
                        self.smoke = True
            else:
                self.rect.centerx = -100
                self.rect.centery = -100
            if self.smoke == True:
                self.time += 1
                if self.time <= 200:
                    self.image.set_alpha(255-self.time*1.25)
                    self.rect = self.image.get_rect()
                else:
                    self.smoke = False
                    self.time = 0
            if self.image == smoke_img and self.smoke == False:
                self.shoot = 0
                self.rect.x = -100
                self.rect.y = -100
                havepoison = 0
                select.append("poison")
                have.remove("poison")
                have2.remove("poison")
                self.__init__()

class Aim2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = aim2_img
        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = -200
    def update(self):
        global mouse_pos,havepoison,carry
        if pause == False:
            if havepoison == 1 and poison.shoot == 0 and carry == "poison" and refreshdown == False:
                self.rect.centerx = mouse_pos[0]
                self.rect.centery = mouse_pos[1]
            else:
                self.rect.x = -200
                self.rect.y = -200
            if poison.smoke == True:
                self.rect.x = -200
                self.rect.y = -200

class Choose(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = choose_img
        self.image.set_alpha(70)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 45
        self.pos = 1
        self.range = 0
    def update(self):
        if pause == False:
            self.range += 1
            self.range = self.range % 7
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and self.pos > 1 and self.range == 1:
                change_sd.play()
                self.pos -= 1
                self.rect.y -= 27
            if key[pygame.K_s] and self.pos < 9 and self.range == 1:
                change_sd.play()
                self.pos += 1
                self.rect.y += 27
            if self.pos == 5:
                self.rect.y = 257
            if self.pos == 4:
                self.rect.y = 126
            if key[pygame.K_1]:
                self.pos = 1
                self.rect.y = 45
            if key[pygame.K_2]:
                self.pos = 2
                self.rect.y = 72
            if key[pygame.K_3]:
                self.pos = 3
                self.rect.y = 99
            if key[pygame.K_4]:
                self.pos = 4
                self.rect.y = 126
            if key[pygame.K_5]:
                self.pos = 5
                self.rect.y = 257
            if key[pygame.K_6]:
                self.pos = 6
                self.rect.y = 284
            if key[pygame.K_7]:
                self.pos = 7
                self.rect.y = 311
            if key[pygame.K_8]:
                self.pos = 8
                self.rect.y = 338
            if key[pygame.K_9]:
                self.pos = 9
                self.rect.y = 365

class Drink(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = drink_img
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100
    def update(self):
        global havedrink,select,carry
        if pause == False:
            key = pygame.key.get_pressed()
            if havedrink == 1 and key[pygame.K_d] and carry == "drink":
                draw_text("Supermode starts.", 30, W/2, 30, "red", 255)
                pygame.display.flip()
                pygame.time.delay(1000)
                player.super = 2
                player.time3 = 1500
                havedrink = 0
                select.append("drink")
                have.remove("drink")
                have2.remove("drink")
                screen.blit(speed_img,(player.rect.x-20,player.rect.y-20))
                magic_sd.play()
                pygame.display.flip()
                pygame.time.delay(1000)
                
            if havedrink == 1 and carry == "drink":
                self.rect.centerx = player.rect.centerx
                self.rect.centery = player.rect.centery
            else:
                self.rect.centerx = -100
                self.rect.centery = -100
            
class Scissors(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = scissors_img
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100
    def update(self):
        global havescissors,select,carry
        if pause == False:
            if havescissors == 1 and carry == "scissors":
                self.rect.centerx = player.rect.centerx
                self.rect.centery = player.rect.centery
            else:
                self.rect.centerx = -100
                self.rect.centery = -100

class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = hammer_img
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100
    def update(self):
        global havehammer,select,carry
        if pause == False:
            if havehammer == 1 and carry == "hammer":
                self.rect.centerx = player.rect.centerx
                self.rect.centery = player.rect.centery-10
                if not mouse_click[0]:
                    self.image = pygame.transform.rotozoom(hammer_img,0,1)
            else:
                self.rect.centerx = -100
                self.rect.centery = -100

class Slimey(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = slimey_img
        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = -200
        self.put = [0,0]
    def update(self):
        global haveslimey,select,carry
        if pause == False:
            if haveslimey == 1 and carry == "slimey":
                self.rect.centerx = player.rect.centerx
                self.rect.centery = player.rect.centery-10

            if self.put != [0,0]:
                slimey_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","slimy.png")),(150,150))
                self.image = slimey_img
                self.rect = self.image.get_rect()
                self.rect.centerx = self.put[0]
                self.rect.centery = self.put[1]

                if refreshdown == True:
                    self.rect.centerx = -200
                    self.rect.centery = -200
                    self.put = [0,0]
                    allsp.remove(self)
                else:
                    self.rect.centerx = self.put[0]
                    self.rect.centery = self.put[1]
            else:
                self.rect.centerx = -200
                self.rect.centery = -200

class Ladder(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ladder_img
        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = -200
        self.put = [0,0]
    def update(self):
        global haveladder,select,carry
        if pause == False:
            if haveladder == 1 and carry == "ladder":
                self.rect.centerx = player.rect.centerx
                self.rect.centery = player.rect.centery-10

            if self.put != [0,0]:
                ladder_img = pygame.transform.scale(pygame.image.load(os.path.join("escape the cellar","ladder.png")),(50,150))
                self.image = ladder_img
                self.rect = self.image.get_rect()
                self.rect.centerx = self.put[0]
                self.rect.centery = self.put[1]

                if refreshdown == True:
                    self.rect.centerx = -200
                    self.rect.centery = -200
                    self.put = [0,0]
                    allsp.remove(self)
                else:
                    self.rect.centerx = self.put[0]
                    self.rect.centery = self.put[1]
            else:
                self.rect.centerx = -200
                self.rect.centery = -200

class Bigladder(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bigladder_img
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = -800
    def update(self):
        if pause == False:
            if refreshdown == True:
                self.rect.y += 2
            if level == TOTAL and self.rect.colliderect(player.rect):
                player.rect.centerx = self.rect.centerx
                player.speed = 0
                climb_sd.play()
                player.rect.centery -= 10
                if player.rect.centery < 0:
                    win()
                    allsp.remove(self)

class Pausebutton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pause1_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 925
        self.rect.centery = 25
        self.pause = False
        self.range = 0
    def update(self):
        global pause
        self.range += 1
        self.range = self.range%5
        if self.pause == False:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = pause1_2_img
                self.rect = self.image.get_rect()
                if pygame.mouse.get_pressed()[0] and self.range == 1:
                    self.pause = True
            else:
                self.image = pause1_img
                self.rect = self.image.get_rect()
        elif self.pause == True:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = pause2_2_img
                self.rect = self.image.get_rect()
                if pygame.mouse.get_pressed()[0] and self.range == 1:
                    self.pause = False
            else:
                self.image = pause2_img
                self.rect = self.image.get_rect()
        self.rect.centerx = 925
        self.rect.centery = 25
        pause = self.pause

class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = start1_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 537
        self.rect.centery = 670
    def update(self):
        global press
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.rect.centery = 675
            self.image = start2_img
            if pygame.mouse.get_pressed()[0] and press == False:
                press = True
                self.rect.centerx = -200
                self.rect.centery = -200
                start.remove(self)
        else:
            self.rect.centery = 670
            self.image = start1_img
            
def draw_backpack():
    global carry,havegun,havepotion,haveshield,have2,have1,instr,ins
    for i in have1:
        if i == "gun":
            screen.blit(pygame.transform.scale(gun_img,(30,20)),(10,(have1.index("gun"))*27+45))
        if i == "shield":
            screen.blit(pygame.transform.scale(shield_img,(20,20)),(10,(have1.index("shield"))*27+45))
        if i == "scissors":
            screen.blit(pygame.transform.scale(scissors_img,(20,30)),(10,(have1.index("scissors"))*27+45))
        if i == "hammer":
            screen.blit(pygame.transform.scale(hammer_img,(15,25)),(12,(have1.index("hammer"))*27+45))
    for i in have2:
        if i == "potion":
            screen.blit(pygame.transform.scale(potion_img,(20,30)),(12,(have2.index("potion"))*27+260))
        if i == "poison":
            screen.blit(pygame.transform.scale(poison_img,(20,30)),(12,(have2.index("poison"))*27+260))
        if i == "drink":
            screen.blit(pygame.transform.scale(drink_img,(20,30)),(12,(have2.index("drink"))*27+260))
        if i == "slimey":
            screen.blit(pygame.transform.scale(slimey_img,(20,20)),(12,(have2.index("slimey"))*27+260))
        if i == "ladder":
            screen.blit(pygame.transform.scale(ladder_img,(20,20)),(12,(have2.index("ladder"))*27+260))
        
    carry = ""
    if havegun == 1:
        if choose.pos == have1.index("gun")+1:
            carry = "gun"
            instr = ins[0]
    if haveshield == 1:
        if choose.pos == have1.index("shield")+1:
            carry = "shield"
            instr = ins[1]
    if havescissors == 1:
        if choose.pos == have1.index("scissors")+1:
            carry = "scissors"
            instr = ins[5]
    if havehammer == 1:
        if choose.pos == have1.index("hammer")+1:
            carry = "hammer"
            instr = ins[6]
    if havepotion == 1:
        if choose.pos-5 == have2.index("potion"):
            carry = "potion"
            instr = ins[2]
    if havepoison == 1:
        if choose.pos-5 == have2.index("poison"):
            carry = "poison"
            instr = ins[4]
    if havedrink == 1:
        if choose.pos-5 == have2.index("drink"):
            carry = "drink"
            instr = ins[3]
    if haveslimey == 1:
        if choose.pos-5 == have2.index("slimey"):
            carry = "slimey"
            instr = ins[7]
    if haveladder == 1:
        if choose.pos-5 == have2.index("ladder"):
            carry = "ladder"
            instr = ins[8]
    if carry == "":
        instr = ""

start = pygame.sprite.Group()
button = Button()
start.add(button)

pygame.mixer.music.play(-1)

screen.blit(start_img, (0,0))
pygame.display.update()
waiting = True
while waiting:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
            pygame.quit()
    if press == True:
        din_sd.play()
        waiting = False
    screen.blit(start_img, (0,0))
    start.update()
    start.draw(screen)

allsp = pygame.sprite.Group()
stonegp = pygame.sprite.Group()
webgp = pygame.sprite.Group()

for i in range(16):
    setx = 50
    for i in range(22):
        set = random.choice(chra)
        wall = Wall()
        allsp.add(wall)
        if set == 1:
            stone = Stone()
            allsp.add(stone)
            stonegp.add(stone)
        if set == 2:
            bomb = Bomb()
            allsp.add(bomb)
        if set == 3:
            box = Box()
            allsp.add(box)
        if set == 4:
            web = Web()
            allsp.add(web)
            webgp.add(web)
        setx += 50
    sety += 50

setx = 0
sety = 0
for i in range(2):
    for i in range(17):
        brick = Brick()
        allsp.add(brick)
        sety += 50
    setx = 1150
    sety = -50

def refresh():
    global set,setx,sety,refreshdown,refreshtime,levelcolindex,levelcol,chra
    sety = -800
    setx = 50
    for i in range(16):
        setx = 50   
        for j in range(22):
            if level < TOTAL-1:
                set = random.choice(chra)
            if level == TOTAL-1:
                set = LEVEL20[int((sety+850)/50-1)][int(setx/50-1)]
            wall = Wall()
            allsp.add(wall)

            if set == 1:
                stone = Stone()
                allsp.add(stone)
                stonegp.add(stone)
            if set == 2:
                bomb = Bomb()
                allsp.add(bomb)
            if set == 3:
                box = Box()
                allsp.add(box)
            if set == 4:
                web = Web()
                allsp.add(web)
                webgp.add(web)
            setx += 50
        sety += 50

    setx = 0
    sety = -800
    for i in range(2):
        for i in range(17):
            brick = Brick()
            allsp.add(brick)
            sety += 50
        setx = 1150
        sety = -800
    if level == TOTAL-1:    
        bigladder = Bigladder()
        allsp.add(bigladder)

bigladder = Bigladder()
pausebutton = Pausebutton()
allsp.add(pausebutton)
player = Player()
shield = Shield()
allsp.add(player)
allsp.add(shield)
gun = Gun()
allsp.add(gun)
scissors = Scissors()
allsp.add(scissors)
hammer = Hammer()
allsp.add(hammer)
slimey = Slimey()
allsp.add(slimey)
ladder = Ladder()
allsp.add(ladder)
dark = Dark()
allsp.add(dark)
bullet = Bullet()
allsp.add(bullet)
potion = Potion()
allsp.add(potion)
drink = Drink()
allsp.add(drink)
poison = Poison()
allsp.add(poison)
aim = Aim()
allsp.add(aim)
aim2 = Aim2()
allsp.add(aim2)
choose = Choose()

run = True
bat = Bat()
allsp.add(bat)
player.rect.centerx = W/2+20
player.rect.y = 755
while run:

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if random.randint(0,250) == 50:
        bat = Bat()
        allsp.add(bat)
    
    if pause == True:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume(1)

    if refreshdown == True and pause == False:
        refreshtime += 1
    if refreshtime > 400:
        level += 1
        refreshtime = 0
        refreshdown = False
        time.sleep(0.1)
        for i in [bat,shield,gun,scissors,hammer,dark,bullet,potion,drink,poison,aim,aim2,ladder,slimey]:
            allsp.remove(i)
            i.kill()
        for i in [player,bat,shield,gun,scissors,hammer,dark,bullet,potion,drink,poison,aim,aim2,ladder,slimey]:
            allsp.add(i)
        if reallevel == TOTAL:
            player.rect.centerx = 70
            player.rect.y = 705
        else:
            player.rect.centerx = W/2+20
            player.rect.y = 755
            
    if pause == False:
        levelcolindex += 0.1
    levelcol = ["red","orange","yellow","green","skyblue","purple","pink"]
    allsp.update()
    screen.fill("black")
    screen.blit(wall1_img,(0,0))
    allsp.draw(screen)

    if level == 1 and refreshdown == False:
        screen.blit(floor_img,(0,795))
    screen.blit(backpack_img,(0,20))
    draw_backpack()
    choose.update()

    if level <= TOTAL:
        draw_text("level:" + str(level) +"/20",30,1050,20,levelcol[math.ceil(levelcolindex)%len(levelcol)],255)
    if refreshdown == False:
        draw_text(instr,15,700,785,"white",100)
    screen.blit(choose.image,(choose.rect.x,choose.rect.y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()