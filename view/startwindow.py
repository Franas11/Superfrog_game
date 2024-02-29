from typing import Tuple

import pygame

from view.button import Button
from view.window import Window


class StartWindow(Window):
    def __init__(self, width: int, height: int, fps: int, fontsize: int, font_colour: Tuple[int, int, int],
                 font: pygame.font.Font):
        super().__init__(width, height, fps, fontsize, font_colour, font)
        self.button = Button(483, 700, 400, 50, "Start game!", font, 20, (22, 230, 11), (11, 131, 230))

    def show_start_screen(self) -> bool:
        title_text = self.font.render("Welcome to the super frog game!!!", True, self.font_colour)
        description_text_lines = [
            "Game rules:",
            "Press 'a' to move the character left,",
            "'d' to move right.",
            "Collect coins to increase your score.",
            "The timer is located in the top right",
            "corner of the screen."
        ]

        running = True
        while running:
            for event in pygame.event.get():
                running = self.button.handle_event(event)  # Pass events to the button
                if running is False:
                    return True
                if event.type == pygame.QUIT:
                    return False

            self.window.fill((0, 0, 0))
            self.window.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 50))

            # Calculate the position of the description text
            description_x = 50
            description_y = 100 + title_text.get_height()  # Add some spacing after the title

            # Render each line of the description text
            line_height = self.font.get_linesize()
            for i, line in enumerate(description_text_lines):
                line_rendered = self.font.render(line, True, self.font_colour)
                line_y = description_y + i * line_height
                self.window.blit(line_rendered, (description_x, line_y))

            self.button.draw(self.window)  # Draw the button

            pygame.display.flip()
            self.clock.tick(self.fps)
