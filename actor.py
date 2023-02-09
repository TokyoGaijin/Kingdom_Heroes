import pygame
import keyboard
from enum import Enum
import os

# Do a useful enum state here

class Actor(object):
    def __init__(self, surface, posX, posY, default_sprite = os.path.join("sprites/human", "female_commoner_0.png"), isPlayer = False):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.actor_sprite = pygame.image.load(default_sprite)
        self.isPlayer = isPlayer
        self.hotkeys = ['up', 'down', 'left', 'right', 'a', 's', 'd', 'w']
        self.isMoving = False # to be used with motion detection

        # vital stats
        self.speed = 5

        # animation frames
        # to be populated here


    def move(self, direction):
        if self.isMoving:
            if direction == "up":
                self.posY -= self.speed
            if direction == "down":
                self.posY += self.speed
            if direction == "left":
                self.posX -= self.speed
            if direction == "right":
                self.posX += self.speed



    def on_release_movekey(self, key):
        for keys in self.hotkeys:
            if key.name == keys:
                self.isMoving = False


    def controller(self):
        if keyboard.is_pressed('left_arrow') or keyboard.is_pressed('a'):
            self.isMoving = True
            self.move("left")
        if keyboard.is_pressed('right_arrow') or keyboard.is_pressed('d'):
            self.isMoving = True
            self.move("right")
        if keyboard.is_pressed('up_arrow') or keyboard.is_pressed('w'):
            self.isMoving = True
            self.move("up")
        if keyboard.is_pressed('down_arrow') or keyboard.is_pressed('s'):
            self.isMoving = True
            self.move("down")

        keyboard.on_release(self.on_release_movekey)






    def update(self):
        print(self.isMoving)
        if self.isPlayer:
            self.controller()

    def draw(self):
        self.surface.blit(self.actor_sprite, (self.posX, self.posY))