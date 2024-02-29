import pygame

coin_image = pygame.image.load("images/coin.png")  # loading image is global, reducing I/O operations


class Coin:
    def __init__(self, window: pygame.Surface, width: int, height: int):
        self.image = coin_image
        self.x_position = width
        self.y_position = height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.window = window
        self.hit_box = pygame.Rect(self.x_position, self.y_position, self.width, self.height)

    def draw(self):
        self.window.blit(self.image, (self.x_position, self.y_position))
