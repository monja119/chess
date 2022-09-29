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

        for key, value in position.items():
            # white or black
            for k, v in value.items():
                # pieces id and its data
                print(k, eval(v['pos'][-1]), v['src'], sep=" - ")
                src = v['src']
                pos = eval(v['pos'][-1])
                piece = pygame.image.load(src).convert_alpha()
                window.blit(piece, pos)


        # updating game
        pygame.display.flip()
