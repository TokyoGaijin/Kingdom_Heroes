import pygame
import random
import keyboard
import os
from enum import Enum

class CharacterState(Enum):
    ALIVE = 0
    ASLEEP = 1
    POISONED = 2
    PETRIFIED = 3
    DEAD = 4

class JobState(Enum):
    WARRIOR = 0
    MAGIC_USER = 1
    HEALER = 2
    THIEF = 3
    SUMMONER = 4
    CHARMER = 5
    COMMONER = 6

class RaceState(Enum):
    HUMAN = 0
    ELF = 1
    SMALLS = 2
    TROLL = 3
    CENTAUR = 4
    KLINGORC = 5

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class Character(object):
    def __init__(self, surface, startX, startY, isPlayer = False, job = JobState.WARRIOR, race = "human", gender = "female"):
        self.surface = surface
        self.posX = startX
        self.posY = startY
        self.isPlayer = isPlayer
        self.job = job
        self.speed = 5


        self.health = 100
        self.mana = 0
        self.intel = 0
        self.strength = 0
        self.luck = 0
        self.charisma = 0
        self.action_points = 2
        self.level = 0

        self.inventory = []
        self.char_points = 25

        self.message = None


        if self.job == JobState.WARRIOR:
            self.strength += 5
        elif self.job == JobState.MAGIC_USER:
            self.mana += 5
        elif self.job == JobState.HEALER:
            self.intel += 5
            self.mana += 3
        elif self.job == JobState.THIEF:
            self.luck += 5
            self.charisma += 2
        elif self.job == JobState.SUMMONER:
            self.mana += 3
            self.intel += 3
            self.intel += 3
        elif self.job == JobState.CHARMER:
            self.charisma += 5


        self.name = "Player1"
        self.gender = gender
        self.race = race

        if self.gender == Gender.MALE and self.job == JobState.WARRIOR:
            self.default_sprite = os.path.join("sprites", "human/warrior_base.png")

        self.sprite_dir = "sprites"
        self.walk_down_strip = [pygame.image.load(os.path.join(self.sprite_dir, f"{self.race}/{self.gender}_walk_down_{i}.png")) for i in range(0,3)]
        self.walk_up_strip = [pygame.image.load(os.path.join(self.sprite_dir, f"{self.race}/{self.gender}_walk_up_{i}.png")) for i in range(0, 3)]
        # Default directon = right
        self.walk_strip = [pygame.image.load(os.path.join(self.sprite_dir, f"{self.race}/{self.gender}_walk_right_{i}.png")) for i in range(0, 3)]
        self.character_sprite = pygame.image.load(os.path.join(self.sprite_dir, f"{self.race}/{self.gender}_walk_down_1.png"))

        # file format: race / gender_action_direction_index
        self.direction = "down"


    def walk_anim(self, direction):
        current_frame = 0
        rate_time = 4
        counter = 0
        #try:
        if current_frame >= 3:
            current_frame = 0

        if direction == "down":
            for frame in range(0, len(self.walk_down_strip)):
                self.surface.blit(self.walk_down_strip[frame], self.posX, self.posY)
            counter += 1
            if counter % rate_time == 0:
                self.current_frame += 1

        # except Exception:
        #     print("Something wrong happened.")





    def add_points(self, attrib, points_to_add):
        if self.isPlayer:
            if attrib == "mana":
                self.mana += points_to_add
            elif attrib == "intelligence":
                self.intel += points_to_add
            elif attrib == "strength":
                self.strength += points_to_add
            elif attrib == "luck":
                self.luck += points_to_add
            elif attrib == "charisma":
                self.charisma += points_to_add

            self.char_points -= self.points_to_add

            if points_to_add >= self.char_points:
                self.message = "Not enough points."
                print(self.message)
        else:
            self.message = "Attributes cannot be set to a NPC."
            print(self.message)


    def move(self, direction):
        # for the overworld
        if direction == "left":
            self.posX -= self.speed
        if direction == "right":
            self.posX += self.speed
        if direction == "up":
            self.posY -= self.speed
        if direction == "down":
            self.posY += self.speed

        self.walk_anim(direction)
        

    def update(self):
        if self.isPlayer:
            if keyboard.is_pressed('up_arrow') or keyboard.is_pressed('w'):
                self.move("up")
            if keyboard.is_pressed('down_arrow') or keyboard.is_pressed('s'):
                self.move("down")
            if keyboard.is_pressed('left_arrow') or keyboard.is_pressed('a'):
                self.move("left")
            if keyboard.is_pressed('right_arrow') or keyboard.is_pressed('d'):
                self.move("right")

    def draw(self):
        self.surface.blit(self.character_sprite, (self.posX, self.posY))