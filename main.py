import pygame
from pygame.locals import *
from pieces import Pieces

pygame.init()

pieces = Pieces()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

