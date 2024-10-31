import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("playformer")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 200

FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    clock = pygame.time.clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
              
pygame.quit()
quit()
if _name_ == "_main_":
    main(window)
