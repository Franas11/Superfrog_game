from typing import Tuple

import pygame


class Floor:
    def __init__(self, x: int, y: int, width: int, height: int, window: pygame.Surface, floor_colour: Tuple):
        self.x_position = x
        self.y_position = y
        self.width = width
        self.height = height
        self.window = window
        self.colour = floor_colour
        self.hit_box = pygame.Rect(self.x_position, self.y_position, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.window, self.colour, self.hit_box)
