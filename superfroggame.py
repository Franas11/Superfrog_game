import pygame

from view.endwindow import EndWindow
from view.maingamewindow import MainGameWindow
from view.startwindow import StartWindow

pygame.init()  # initialization of Pygame library

# -------------------SETTINGS-AND-GLOBAL-VARIABLES----------------------------------------------------------------------
PROGRAM_NAME = "SuperFrog - Jan Franasowicz"
PROGRAM_LOGO = pygame.image.load("images/super_frog_logo.png")
WIDTH = 1366
HEIGHT = 768
FPS = 60  # setting the game's FPS
ACCELERATION = 0.5  # setting game speed
MAX_PLAYER_VELOCITY = 10  # speed of player
GRAVITY = 0.8
MAX_JUMP_HEIGHT = 18
FONTSIZE = 32
FONT_COLOUR = (255, 255, 255)
FONT = pygame.font.Font("font/emulogic.ttf", FONTSIZE)
FLOOR_COLOUR = (0, 204, 0)
# ----------------------------------------------------------------------------------------------------------------------

pygame.display.set_caption(PROGRAM_NAME)
pygame.display.set_icon(PROGRAM_LOGO)
CLOCK = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.music.load("soundtrack/main_theme.mp3")
coin_sound = pygame.mixer.Sound("soundtrack/coin_sound.mp3")
monster_sound = pygame.mixer.Sound("soundtrack/monster_death_sound.mp3")
death_sound = pygame.mixer.Sound("soundtrack/death_sound.mp3")
pygame.mixer.music.play(-1)

game = MainGameWindow(WIDTH, HEIGHT, FPS, ACCELERATION, MAX_PLAYER_VELOCITY, GRAVITY,
                      MAX_JUMP_HEIGHT, FONTSIZE, FONT_COLOUR, FONT, FLOOR_COLOUR, coin_sound, monster_sound,
                      death_sound)

if __name__ == '__main__':
    start_window = StartWindow(WIDTH, HEIGHT, FPS, FONTSIZE, FONT_COLOUR, FONT)
    if_player_want_play = start_window.show_start_screen()
    if_player_want_quit_game = False
    while if_player_want_play is True and if_player_want_quit_game is False:
        game = MainGameWindow(WIDTH, HEIGHT, FPS, ACCELERATION, MAX_PLAYER_VELOCITY, GRAVITY,
                              MAX_JUMP_HEIGHT, FONTSIZE, FONT_COLOUR, FONT, FLOOR_COLOUR, coin_sound, monster_sound,
                              death_sound)
        player = game.player
        timer = game.timer
        game.start_game()
        end_window = EndWindow(WIDTH, HEIGHT, FPS, FONTSIZE, FONT_COLOUR, FONT, player.score, timer.get_minutes(),
                               timer.get_seconds(), game.EVENT_PLAYER_KILLED)
        if_player_want_quit_game = end_window.show_end_screen()
