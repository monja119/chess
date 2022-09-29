import pygame
from pygame.locals import *
from pieces import Pieces

# initialization
pygame.init()


class Main:
    def __init__(self, new_data):
        # instance
        pieces = Pieces(new_data)
        self.tiles = pieces.tiles
        self.data = pieces.data

    def update(self, new_data):
        pieces = Pieces(new_data)
        self.tiles = pieces.tiles
        self.data = pieces.data


new_data = []
chess = Main(new_data)

# commands of the game
status_click = 0

running = True
print(chess.data)
target_pos = (0, 0)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # read to move
            if status_click == 1 and target_pos != (0, 0):
                for i in range(len(chess.tiles)):
                    tiles = chess.tiles[i]
                    if tiles.collidepoint(mouse_pos):
                        new_pos = str(tiles).strip('<rect(')
                        new_pos = eval(new_pos.strip(')>'))
                        new_pos = (new_pos[0] + 15, new_pos[1])

                        for k in range(len(chess.data)):
                            if target_pos == chess.data[k]['pos']:
                                chess.data[k]['pos'] = new_pos
                                new_data = chess.data
                                chess.data = new_data
                                chess = Pieces(new_data)
                                print("move")
                        print('new pos {} and target {} '.format(new_pos, target_pos))

                status_click = 0

            else:

                for i in range(len(chess.data)):
                    data = chess.data
                    pieces_rect = chess.data[i]['rect']
                    # verification of collied point
                    if pieces_rect.collidepoint(mouse_pos):
                        pos_index = str(pieces_rect).strip('<rect(')
                        pos_index = eval(pos_index.strip(')>'))
                        pos_index = (pos_index[0] + 15, pos_index[1])

                        status_click = 1
                        target_pos = pos_index

