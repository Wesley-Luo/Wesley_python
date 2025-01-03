import pygame
import random
import time
import os
pygame.init()
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
pygame.quit()