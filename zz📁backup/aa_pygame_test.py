import pygame
import random
import time
import os
pygame.init()
clock = pygame.time.Clock()
W = 1000
H = 600
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("black")
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
exit()