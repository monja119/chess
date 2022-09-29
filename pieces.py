import pygame
import json
from board import Board

board = Board()


class Pieces:
    def __init__(self, data):
        # getting window
        window = board.board
        self.tiles = board.tiles
        self.data = data

        # getting position
        with open('position.json', 'r') as position:
            position = json.load(position)

        # LOADING IMAGES
        if not data:
            for key, value in position.items():
                # white or black
                for k, v in value.items():
                    # pieces id and its data
                    src = v['src']
                    pos = eval(v['pos'][-1])
                    rect = pygame.Rect(pos[0] - 15, pos[1], 100, 72)  # because x = x + 15
                    self.data.append({
                        'pos': pos,
                        'src': src,
                        'rect': rect
                    })

                    # loading
                    piece = pygame.image.load(src).convert_alpha()
                    window.blit(piece, pos)  # loading
        else:
            board.draw_board()
            for i in range(len(data)):
                piece = pygame.image.load(data[i]['src']).convert_alpha()
                window.blit(piece, data[i]['pos'])
        # updating game
        pygame.display.flip()
