from typing import List

import pygame.image

from model.floor import Floor
from model.kinematicentity import KinematicEntity

pygame.mixer.init()
jump_sound = pygame.mixer.Sound("./soundtrack/jump_sound.mp3")


class Player(KinematicEntity):
    def __init__(self, window: pygame.Surface, acceleration: float, max_velocity: int, gravity: float,
                 floor: List[Floor], max_jump_height):
        self.image = pygame.image.load("images/frog.png")  # player's view
        super().__init__(15, 500, self.image.get_width(), self.image.get_height(), acceleration, max_velocity, gravity)
        self.window = window  # main game window reference
        self.score = 0
        self.floor = floor
        self.max_jump_height = max_jump_height

    # below moving frog functionality
    def update_position(self, keys: tuple) -> None:
        self.gravity_movement_and_hit_box_refresh(self.floor)
        if keys[pygame.K_a] and abs(self.horizontal_velocity) < self.max_velocity:
            self.horizontal_velocity -= self.acceleration
        elif keys[pygame.K_d] and self.horizontal_velocity < self.max_velocity:
            self.horizontal_velocity += self.acceleration
        elif keys[pygame.K_SPACE] and self.is_jumping is False:
            self.vertical_velocity -= self.max_jump_height
            self.is_jumping = True
            jump_sound.play()
        elif not (keys[pygame.K_d] or keys[pygame.K_a]):
            if self.horizontal_velocity > 0:
                self.horizontal_velocity -= self.acceleration
            elif self.horizontal_velocity < 0:
                self.horizontal_velocity += self.acceleration

    # below draw a frog
    def draw(self):
        self.window.blit(self.image, (self.x_position, self.y_position))
