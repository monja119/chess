import pygame
from board import Board

board = Board


class Pieces:
    def __init__(self):
        # getting window
        window = board().board

        # placing pieces
        left = 115
        top = 72
        p = pygame.image.load('images/pieces/black/pawn.png').convert_alpha()
        window.blit(p, (left, top))

        # updating game
        pygame.display.flip()
