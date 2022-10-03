import pygame


class Board:
    def __init__(self):
        # static values
        width = 800
        height = 504

        # window
        self.board = pygame.display.set_mode((width, height))
        self.tiles = []
        self.path = []
        self.draw_board(self.path)
        # displaying
        pygame.display.set_caption("Chess Game")
        pygame.display.flip()

    def draw_board(self, path):

        # background
        white = (100, 100, 100)
        black = (50, 50, 50)

        colors = [white, black]
        left, top = 0, 0
        tile_width, tile_height = 100, 72

        # loading rectangles and creating tiles
        for i in range(56):
            if i % 8 == 0 and i != 0:
                top += tile_height
                left = 0
                colors = list(reversed(colors))

            # updating tiles
            self.tiles.append(
                pygame.Rect(left, top, tile_width, tile_height)
            )
            # loading images
            pygame.draw.rect(self.board, colors[i % 2], pygame.Rect(left, top, tile_width, tile_height))
            left += tile_width
