from typing import Tuple

import pygame


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font: pygame.font.Font,
                 font_size: int, default_color: Tuple[int, int, int], hover_color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.font_size = font_size
        self.default_color = default_color
        self.hover_color = hover_color
        self.rect = pygame.Rect(x, y, width, height)
        self.is_hovered = False

    def draw(self, window):
        if self.is_hovered:
            color = self.hover_color
        else:
            color = self.default_color

        pygame.draw.rect(window, color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text_surface, text_rect)

    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.is_hovered = True
            else:
                self.is_hovered = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                return False
        return True
