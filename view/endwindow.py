from typing import Tuple

import pygame
from view.button import Button
from view.window import Window


class EndWindow(Window):
    def __init__(self, width: int, height: int, fps: int, fontsize: int, font_colour: Tuple[int, int, int],
                 font: pygame.font.Font, score: int, time_minutes: int, time_seconds: int, check_player_life: bool):
        super().__init__(width, height, fps, fontsize, font_colour, font)
        self.score = score
        self.time_minutes = time_minutes
        self.time_seconds = time_seconds
        self.end_button = Button(200, 500, 300, 50, "End Game", font, 20, (255, 0, 0), (173, 66, 66))
        self.play_again_button = Button(800, 500, 350, 50, "Play Again", font, 20, (25, 64, 38), (34, 128, 65))
        self.is_player_dead = check_player_life

    def show_end_screen(self) -> bool:
        score_text = self.font.render(f"Score: {self.score}", True, self.font_colour)
        time_text = self.font.render(f"Time: {self.time_minutes:02d} min {self.time_seconds:02d} sec", True,
                                     self.font_colour)
        if not self.is_player_dead:
            game_result_text = self.font.render(f"YOU WON", True, self.font_colour)
        else:
            game_result_text = self.font.render(f"YOU LOST", True, self.font_colour)

        running = True
        while running:
            for event in pygame.event.get():
                running = self.end_button.handle_event(event) and self.play_again_button.handle_event(event)
                if not running:
                    return self.play_again_button.handle_event(event)  # Return the result of the play again button
                if event.type == pygame.QUIT:
                    return True

            self.window.fill((0, 0, 0))
            self.window.blit(score_text, (self.width // 2 - score_text.get_width() // 2, 50))
            self.window.blit(time_text, (self.width // 2 - time_text.get_width() // 2, 100))
            self.window.blit(game_result_text, (self.width // 2 - game_result_text.get_width() // 2, 300))

            self.end_button.draw(self.window)
            self.play_again_button.draw(self.window)

            pygame.display.flip()
            self.clock.tick(self.fps)
