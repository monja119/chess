import pygame


class Board:
    def __init__(self):
        width = 800
        height = 504

        # window
        self.bord = pygame.display.set_mode((width, height))
        # background
        white = (255, 255, 255)
        black = (0, 0, 0)
        colors = [white, black]
        left, top = 0, 0
        tile_width, tile_height = 100, 72

        for i in range(56):
            if i % 8 == 0 and i != 0:
                top += tile_height
                left = 0
                colors = list(reversed(colors))
            pygame.draw.rect(self.bord, colors[i % 2], pygame.Rect(left, top, tile_width, tile_height))
            left += tile_width

        # displaying
        pygame.display.set_caption("Chess Game")
        pygame.display.flip()

