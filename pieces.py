import pygame
import json
from board import Board

board = Board


class Pieces:
    def __init__(self):
        # getting window
        window = board().board

        # getting position
        with open('position.json', 'r') as position:
            position = json.load(position)
        print(position["white"])
        # placing pieces
        left = 115
        top = 72
        p = pygame.image.load('images/pieces/black/pawn.png').convert_alpha()
        window.blit(p, (left, top))

        # updating game
        pygame.display.flip()
