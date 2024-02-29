from typing import Tuple, List

import pygame

from model.coin import Coin
from model.floor import Floor
from model.player import Player
from model.timer import Timer
from view.window import Window

darkgreen = (19, 47, 19)
red = (110, 38, 14)
gray = (169, 169, 169)
dimgray = (105, 105, 105)

from model.monster import Monster

pygame.init()


class MainGameWindow(Window):
    def __init__(self, width: int, height: int, fps: int, acceleration: float, max_player_velocity: int, gravity: float,
                 max_jump_height: int, fontsize: int, font_colour: Tuple[int, int, int], font: pygame.font.Font,
                 floor_colour: Tuple[int, int, int], coin_sound: pygame.mixer.Sound, monster_sound: pygame.mixer.Sound,
                 death_sound: pygame.mixer.Sound):

        super().__init__(width, height, fps, fontsize, font_colour, font)
        self.clock = pygame.time.Clock()
        self.timer = Timer()
        self.coin_sound = coin_sound
        self.monster_sound = monster_sound
        self.player_death_sound = death_sound
        self.floors = [
            Floor(0, self.height - 50, self.width - 100, 50, self.window, darkgreen),
            Floor(600, 600, 50, 120, self.window, red),
            Floor(160, 320, 40, 180, self.window, gray),
            Floor(120, 460, 40, 40, self.window, gray),
            Floor(300, 220, 50, 40, self.window, floor_colour),
            Floor(350, 450, 150, 40, self.window, floor_colour),
            Floor(500, 170, 500, 80, self.window, dimgray),
            Floor(950, 250, 50, 300, self.window, dimgray),
            Floor(650, 450, 300, 50, self.window, floor_colour),
            Floor(1000, 500, 50, 50, self.window, dimgray),
            Floor(1120, 370, 50, 50, self.window, floor_colour),
            Floor(1000, 250, 100, 40, self.window, dimgray),
            Floor(1250, 160, 150, 700, self.window, red),
            Floor(1200, 150, 300, 50, self.window, red),
            Floor(-1, 0, 1, 766, self.window, floor_colour)
        ]
        self.coins: List[Coin] = [Coin(self.window, 110, 410),
                                  Coin(self.window, 300, 170),
                                  Coin(self.window, 900, 400),
                                  Coin(self.window, 1000, 450),
                                  Coin(self.window, 1000, 285),
                                  Coin(self.window, 1200, 665),
                                  Coin(self.window, 655, 665),
                                  Coin(self.window, 700, 15),
                                  Coin(self.window, 1300, 100),
                                  Coin(self.window, 100, 655)]
        self.player = Player(self.window, acceleration, max_player_velocity, gravity, self.floors,
                             max_jump_height)

        self.monsters = [Monster(self.window, 150, 600, 300),
                         Monster(self.window, 650, 600, 450),
                         Monster(self.window, 650, 330, 170),
                         Monster(self.window, 475, 47, 380)]
        self.EVENT_PLAYER_KILLED = False

    def generate_random_coin(self, counter: int) -> int:
        if counter > 1000:
            self.coins.append(Coin(self.window, self.width, self.height))
            return 0
        return counter

    def handle_coin_interaction(self) -> None:
        for coin in self.coins:
            if self.player.hit_box.colliderect(coin.hit_box):
                self.coins.remove(coin)
                self.player.score += 1
                self.coin_sound.play()
        for coin in self.coins:
            coin.draw()

    def handle_monster_interaction(self):
        for monster in self.monsters:
            if isinstance(monster, Monster):
                monster.update()
                monster.draw()
                monster_hitbox = monster.get_hit_box()

                if monster_hitbox.colliderect(self.player.hit_box) \
                        and self.player.hit_box.bottom >= monster_hitbox.top > self.player.hit_box.top:
                    self.monster_sound.play()
                    self.monsters.remove(monster)
                    self.player.score += 1

                elif monster_hitbox.colliderect(self.player.hit_box) \
                        and self.player.hit_box.right >= monster_hitbox.left >= self.player.hit_box.left:
                    self.player_death_sound.play()
                    self.EVENT_PLAYER_KILLED = True

                elif monster_hitbox.colliderect(self.player.hit_box) \
                        and monster_hitbox.right >= self.player.hit_box.left \
                        and monster_hitbox.left <= self.player.hit_box.right:
                    self.player_death_sound.play()
                    self.EVENT_PLAYER_KILLED = True

    def draw_objects(self=None) -> None:
        keys = pygame.key.get_pressed()
        self.player.update_position(keys)  # change of player position
        self.window.fill((0, 0, 0))
        self.player.draw()

        self.handle_monster_interaction()

        self.handle_coin_interaction()

        score_text = self.font.render(f"Score: {self.player.score}", True, self.font_colour)
        time_text = self.font.render(f"{self.timer.get_minutes()} min {self.timer.get_seconds()} sec", True,
                                     self.font_colour)

        self.window.blit(score_text, (0, 0))
        self.window.blit(time_text, (self.window.get_width() - time_text.get_width(), 0))
        for floor in self.floors:
            floor.draw()
        pygame.display.update()

    def start_game(self) -> None:
        counter = 0
        run = True
        self.timer.start()  # starting time measurement
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if self.EVENT_PLAYER_KILLED:
                run = False
            counter += self.clock.tick(self.fps)
            self.draw_objects()
            if self.player.x_position >= 1366:
                run = False
