import pygame
from pygame.locals import *
from pieces import Pieces
from moves import Moves

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

# status of the game
status_click = 0
piece_color = ['black', 'white']
turn = ''
moves = 0


running = True
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
                        data = chess.data
                        new_pos = str(tiles).strip('<rect(')
                        new_pos = eval(new_pos.strip(')>'))
                        new_pos = (new_pos[0] + 15, new_pos[1])

                        for k in range(len(chess.data)):
                            if target_pos == chess.data[k]['pos'] and target_pos != new_pos:
                                # MOVEMENT <>
                                move = Moves(target_pos, new_pos, name, color, chess.data)

                                if move.accept is not None:
                                    # updating position
                                    chess.data[k]['pos'] = new_pos  # pos
                                    # updating rectangle
                                    chess.data[k]['rect'] = pygame.Rect(new_pos[0] - 15, new_pos[1], 100, 72)
                                    # pushing new data
                                    new_data = chess.data
                                    chess = Pieces(new_data)
                                    # updating moves
                                    moves += 1
                                    turn = piece_color[moves % 2]
                                    break

                status_click = 0

            else:

                for i in range(len(chess.data)):
                    data = chess.data
                    pieces_rect = data[i]['rect']
                    # verification of collied point
                    if pieces_rect.collidepoint(mouse_pos):
                        color = data[i]['src'].split('/')[2]
                        name = data[i]['src'].split('/')[-1].split('.')[0]
                        src = data[i]['src']
                        # managing turn
                        if moves == 0:
                            moves = piece_color.index(color)
                            turn = piece_color[moves % 2]

                        if turn == color:
                            pos_index = str(pieces_rect).strip('<rect(')
                            pos_index = eval(pos_index.strip(')>'))
                            pos_index = (pos_index[0] + 15, pos_index[1])
                            target_pos = pos_index

                        status_click = 1
