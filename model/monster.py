import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self, window: pygame.Surface, x_position, y_position, steps_distance):
        super().__init__()
        self.image = pygame.image.load("images/snail.png")

        self.width, self.height = 137, 123

        self.x_position = x_position
        self.y_position = y_position
        self.window = window

        # Set monster's speed
        self.speed = 1

        self.direction_right = True
        self.steps = 0
        self.steps_distance = steps_distance

    def draw(self):
        self.window.blit(self.image, (self.x_position, self.y_position))

    def update(self):
        # Moving the monster
        if self.direction_right:
            self.x_position += self.speed
            self.steps += self.speed
            if self.steps >= self.steps_distance:
                self.direction_right = False
        if not self.direction_right:
            self.x_position -= self.speed
            self.steps -= self.speed
            if self.steps <= 0:
                self.direction_right = True

    def get_hit_box(self):
        return pygame.Rect(self.x_position, self.y_position, self.width, self.height)
