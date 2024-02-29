from typing import List

import pygame

from model.floor import Floor


class KinematicEntity:
    def __init__(self, x: int, y: int, width: int, height: int, acceleration: float, max_velocity: int, gravity: float):
        self.x_position = x  # x position
        self.y_position = y  # y position
        self.x_previous_position = x
        self.y_previous_position = x
        self.width = width
        self.height = height
        self.hit_box = pygame.Rect(self.x_position, self.y_position, self.width, self.height)
        self.horizontal_velocity = 0
        self.vertical_velocity = 0
        self.acceleration = acceleration
        self.max_velocity = max_velocity
        self.gravity = gravity
        self.is_jumping = False

    def gravity_movement_and_hit_box_refresh(self, floors: List[Floor]):
        self.vertical_velocity += self.gravity
        self.x_position += self.horizontal_velocity
        self.y_position += self.vertical_velocity
        self.hit_box = pygame.Rect(self.x_position, self.y_position, self.width, self.height)
        for floor in floors:
            if floor.hit_box.colliderect(
                    self.hit_box):  # reverting the object to the position from the previous frame, colliderect
                # allows to check if 2 rectangles collide with each other
                if self.x_position + self.width >= floor.x_position + 1 > self.x_previous_position + self.width:
                    # collision from the right side
                    self.x_position = self.x_previous_position
                    self.horizontal_velocity = 0
                if self.x_position <= floor.x_position + floor.width - 1 < self.x_previous_position:
                    # collision from the left side
                    self.x_position = self.x_previous_position
                    self.horizontal_velocity = 0
                if self.y_position + self.height >= floor.y_position + 1 > self.y_previous_position:
                    # collision from top
                    self.y_position = self.y_previous_position
                    self.vertical_velocity = 0
                    self.is_jumping = False
                if self.y_position <= floor.y_position + floor.height - 1 < self.y_previous_position:
                    # collision from bottom
                    self.y_position = self.y_previous_position
                    self.vertical_velocity = 0

        self.x_previous_position = self.x_position
        self.y_previous_position = self.y_position
