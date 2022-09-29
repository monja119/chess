import pygame
from pygame.locals import *
from board import Board

board = Board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

