from typing import Tuple

import pygame


class Window:
    def __init__(self, width: int, height: int, fps: int, fontsize: int, font_colour: Tuple[int, int, int],
                 font: pygame.font.Font):
        self.width = width
        self.height = height
        self.fps = fps
        self.fontsize = fontsize
        self.font_colour = font_colour
        self.font = font
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.width, self.height))
