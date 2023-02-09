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
        self.isMoving = False # to be used with motion detection
        self.hotkeys = ['up_arrow', 'donw_arrow', 'left_arrow', 'right_arrow', 'a', 's', 'd', 'w']


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

    def controller(self):
        if keyboard.is_pressed('left_arrow') or keyboard.is_pressed('a'):
            self.move("left")
        if keyboard.is_pressed('right_arrow') or keyboard.is_pressed('d'):
            self.move("right")
        if keyboard.is_pressed('up_arrow') or keyboard.is_pressed('w'):
            self.move("up")
        if keyboard.is_pressed('down_arrow') or keyboard.is_pressed('s'):
            self.move("down")

        for key in self.hotkeys:
            if keyboard.release(self.hotkeys[key]):
                self.isMoving = False
            elif keyboard.is_pressed(self.hotkys[key]):
                self.isMoving = True



    def update(self):
        if self.isPlayer:
            self.controller()

    def draw(self):
        pass