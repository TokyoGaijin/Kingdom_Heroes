import pygame
import keyboard
from enum import Enum
import os

# TODO: Do a useful enum state here

# TODO: Create the males for each job, females for each job, separate races and job sprites, etc.

class Actor(object):
    def __init__(self, surface, posX, posY, default_sprite = os.path.join("sprites/human", "female_walk_down_1.png"), gender = "female", isPlayer = False):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.actor_sprite = pygame.image.load(default_sprite)
        self.isPlayer = isPlayer
        self.hotkeys = ['up', 'down', 'left', 'right', 'a', 's', 'd', 'w']
        self.isMoving = False
        self.gender = gender
        self.current_frame = 0
        self.bounding_block = pygame.Rect(self.actor_sprite.get_width(), self.actor_sprite.get_height(), self.posX, self.posY)


        # vital stats
        self.speed = 5

        # animation frames
        self.walk_x = [pygame.image.load(os.path.join("sprites/human", f"{self.gender}_walk_right_{i}.png")) for i in range(0, 3)]
        self.walk_up = [pygame.image.load(os.path.join("sprites/human", f"{self.gender}_walk_up_{i}.png")) for i in range(0, 3)]
        self.walk_down = [pygame.image.load(os.path.join("sprites/human", f"{self.gender}_walk_down_{i}.png")) for i in range(0, 3)]

        self.current_direction = "down"

        # TODO: Create enemy conditions for battle
        # TODO: Create an inventory array/list


    # TODO: Create a character creation function to be used in-game

    def anim_actor(self, direction):
        # need the species, gender and direction for this to work
        animation_duration = 600 # matches 60 FPS in a multiple of 3

        for i in range(0, animation_duration):
            if direction == "right":
                self.surface.blit(self.walk_x[self.current_frame], (self.posX, self.posY))
            elif direction == "left":
                self.surface.blit(pygame.transform.flip(self.walk_x[self.current_frame], True, False), (self.posX, self.posY))
            elif direction == "up":
                self.surface.blit(self.walk_up[self.current_frame], (self.posX, self.posY))
            elif direction == "down":
                self.surface.blit(self.walk_down[self.current_frame], (self.posX, self.posY))


            if (i + 1) % animation_duration == 0:
                self.current_frame += 1

            if self.current_frame > 2:
                self.current_frame = 0




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

        self.bounding_block.x = self.posX
        self.bounding_block.y = self.posY
        self.current_direction = direction


    def on_release_movekey(self, key):
        for keys in self.hotkeys:
            if key.name == keys:
                self.isMoving = False


    def controller(self):
        if keyboard.is_pressed('left_arrow') or keyboard.is_pressed('a'):
            self.isMoving = True
            self.move("left")
            self.anim_actor("left")
        if keyboard.is_pressed('right_arrow') or keyboard.is_pressed('d'):
            self.isMoving = True
            self.move("right")
            self.anim_actor("right")
        if keyboard.is_pressed('up_arrow') or keyboard.is_pressed('w'):
            self.isMoving = True
            self.move("up")
            self.anim_actor("up")
        if keyboard.is_pressed('down_arrow') or keyboard.is_pressed('s'):
            self.isMoving = True
            self.move("down")
            self.anim_actor("down")

        keyboard.on_release(self.on_release_movekey)





    def update(self):
        if self.isPlayer:
            self.controller()



    def draw(self):
        if not self.isMoving:
            # self.surface.blit(self.actor_sprite, (self.posX, self.posY))
            if self.current_direction == "down":
                self.surface.blit(self.actor_sprite, (self.posX, self.posY))
            if self.current_direction == "up":
                self.surface.blit(self.walk_up[1], (self.posX, self.posY))
            if self.current_direction == "left":
                self.surface.blit(pygame.transform.flip(self.walk_x[1], True, False), (self.posX, self.posY))
            if self.current_direction == "right":
                self.surface.blit(self.walk_x[1], (self.posX, self.posY))