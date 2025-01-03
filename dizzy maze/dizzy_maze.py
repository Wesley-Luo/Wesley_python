import pygame
import random
import time
import os
pygame.init()

FPS = 60    
size = 50
level = 0
timer = 6050
clock = pygame.time.Clock()
dark = pygame.transform.scale(pygame.image.load(os.path.join("dizzy maze", "dark.png")), (12800, 8800))
playerimg1 = pygame.transform.scale(pygame.image.load(os.path.join("dizzy maze", "elephant_maze.png")), (size, size-20))
playerimg2 = pygame.transform.scale(pygame.image.load(os.path.join("dizzy maze", "elephant_maze_other.png")), (size, size-20))
blackimg = pygame.transform.scale(pygame.image.load(os.path.join("dizzy maze", "black.png")), (size, size))
whiteimg = pygame.transform.scale(pygame.image.load(os.path.join("dizzy maze", "white.png")), (size, size))
redimg = pygame.transform.scale(pygame.image.load(os.path.join("dizzy maze", "redimg.png")), (size, size))
greenimg = pygame.transform.scale(pygame.image.load(os.path.join("dizzy maze", "greenimg.png")), (size, size))
level_img = pygame.transform.scale(pygame.image.load(os.path.join("dizzy maze", "level.png")), (1000,600))
starting_img = pygame.image.load(os.path.join("dizzy maze", "maze_start_back.png"))
pygame.display.set_icon(playerimg1)
next_sd = pygame.mixer.Sound(os.path.join("dizzy maze", "next.wav"))
win_sd = pygame.mixer.Sound(os.path.join("dizzy maze", "win.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("dizzy maze", "lose.wav"))
pygame.mixer.music.load(os.path.join("dizzy maze", "mazeback.wav"))
font_name = os.path.join("dizzy maze","font.ttf")
x = 0
y = 0
W = 1000
H = 600
pimg = playerimg1
pygame.display.set_caption("暈眩迷宮")
screen = pygame.display.set_mode((W, H))
player_rect = pimg.get_rect()
player_rect.x = 50
player_rect.y = 500
ang = 0

def win():
    screen.fill("black")
    draw_text(screen,"You win!", 200, W/2, H/2,"green")
    pygame.display.update()
    win_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()
def lose():
    time.sleep(2)
    screen.fill("black")
    draw_text(screen,"You lose!", 200, W/2, H/2,"red")
    pygame.display.update()
    lose_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

maze1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 3, 0],
         [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

maze2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

maze3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 1, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
         [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 2, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

allmaze = random.choice([[maze1, maze2, maze3],[maze2, maze1, maze3],[maze3, maze2, maze1],[maze3, maze1, maze2],[maze1, maze3, maze2],[maze2, maze3, maze1]])
map = allmaze[0]

def draw_text(surf,text, size, x, y,col):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface, text_rect)

class Maze(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global pic
        if pic == 1:
            self.image = whiteimg
        elif pic == 2:
            self.image = redimg
        elif pic == 3:
            self.image = greenimg
        else:
            self.image = blackimg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

def draw():
    global x, y, allgp, pic
    x = 0
    y = 0
    allgp = pygame.sprite.Group()
    for a in range(len(map)):
        for i in range(len(map[0])):
            pic = map[a][i]
            maze = Maze()
            allgp.add(maze)
            x += size
        x = 0
        y += size

pygame.mixer.music.play(-1)

start_img = pygame.transform.scale(starting_img, (1200,900))
screen.blit(start_img, (-90,-195))
pygame.display.update()
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            waiting = False

draw()
run = True
while run:
    clock.tick(FPS)
    mx = int(player_rect.x/50)
    my = int(player_rect.y/50)
    pos = map[my][mx]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and map[my-1][mx] != 0:
                player_rect.y -= size
            elif event.key == pygame.K_DOWN and map[my+1][mx] != 0:
                player_rect.y += size
            elif event.key == pygame.K_LEFT and map[my][mx-1] != 0:
                pimg = playerimg2
                player_rect.x -= size
            elif event.key == pygame.K_RIGHT and map[my][mx+1] != 0:
                pimg = playerimg1
                player_rect.x += size

    if pos == 3:
        time.sleep(1)
        if level == 2:
            time.sleep(1)
            win()
        else:
            screen.blit(level_img,(0,0))
            pygame.display.flip()
            next_sd.play()
            time.sleep(1)
            level += 1
            map = allmaze[level]
            draw()
            player_rect.x = 50
            player_rect.y = 500
            mx = int(player_rect.x/50)
            my = int(player_rect.y/50)
            pos = map[my][mx]

    screen.fill("black")
    allgp.update()
    allgp.draw(screen)
    screen.blit(pimg, (player_rect.x, player_rect.y+10))
    screen.blit(dark, (player_rect.centerx-6550, player_rect.centery-4410))
    draw_text(screen,"level: "+str(level+1), 40, W/2-100, 30,"black")
    draw_text(screen, "time: "+ str(int(timer/60)), 40, W/2+100, 30,"black")
    pygame.display.flip()
    timer -= 1
    
    if timer <= 1:
        lose()

pygame.quit()
exit()