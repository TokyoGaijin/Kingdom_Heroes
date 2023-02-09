import pygame
import keyboard
import os
import platform
import colorswatch as cs
import pyautogui
from enum import Enum
import actor
import level

class GameState(Enum):
    # Will contain game states enumerated
    pass

class OSState(Enum):
    WINDOWS = 0
    MACOS = 1
    LINUX = 2

pygame.init()

SCREEN_X = 1280
SCREEN_Y = 800
SCREEN_SIZE = (SCREEN_X, SCREEN_Y)
GAME_TITLE = "Under Construction"

WINDOW = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(GAME_TITLE)

FPS = 60
CLOCK = pygame.time.Clock()

REFRESH_COLOR = cs.black["pygame"]
# Will be useful for distros
if platform.system() == "Windows":
    CURRENT_OS = OSState.WINDOWS
elif platform.system() == "Darwin":
    CURRENT_OS = OSState.MACOS
elif platform.system() == "Linux":
    CURRENT_OS = OSState.LINUX


player = actor.Actor(WINDOW, SCREEN_X / 2 , SCREEN_Y / 2, isPlayer = True)
current_level = level.Level(WINDOW, 100, 100)

def run_game():

    inGameLoop = True
    current_level.build_level(0)


    def update():
        player.update()

        # TODO: Add collisions for the wall vs. player bounding boxes

        pygame.display.update()
        WINDOW.fill(REFRESH_COLOR)

    def draw():
        current_level.draw()
        player.draw()


    while inGameLoop:

        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inGameLoop = False

        if keyboard.is_pressed('escape'):
            inGameLoop = False

        draw()
        update()


if __name__ == ('__main__'):
    run_game()