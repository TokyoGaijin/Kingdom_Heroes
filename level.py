import pygame
import os
import tile

class Level(object):
    def __init__(self, surface, startX, startY):
        self.surface = surface
        self.startX = startX
        self.startY = startY
        self.posX, self.posY = startX, startY
        self.level_map = [["---WWWWWWWWWWWWW----",
                           "---WWFFFFFFFFFWW----",
                           "-WWFFFFFFFFFFFFFWW--",
                           "-WWFFFFFFFFFFFFFWW--",
                           "--WWFFFFFFFFFFFWW---",
                           "----WWFFFFFFFWW-----",
                           "------WWFFFWW-------",
                           "------WWFFFWW-------",
                           "---WWWWWFFFWWWW-----",
                           "---WWFFFFFFFFWW-----",
                           "---WWFFFFFFFFWW-----",
                           "---WWFFFFFFFFWW-----",
                           "---WWWWFFFFWWWW-----",
                           "-----WWFFFFWW-------",
                           "----WWWFFFFWWW------",
                           "--WWFFFFFFFFFFWW----",
                           "--WWFFFFFFFFFFWW----",
                           "--WWFFFFFFFFFFWW----",
                           "--WWWWWWWWWWWWWW----"],]

        # TODO: Add wider levels and readjust the height of each level to fit the screen perfectly.
        # TODO: Create separate objects for walls vs. floors and so-on to allow the player collisions

        self.current_level = []

    def build_level(self, level_index):
        skip_step = 32

        for row in self.level_map[level_index]:
            for col in row:
                if col == "W":
                    self.current_level.append(tile.Tile(self.surface, self.posX, self.posY, tile_type = "wall", tile_image = "brick_gray_1"))
                if col == "F":
                    self.current_level.append(tile.Tile(self.surface, self.posX, self.posY, tile_type = "floor", tile_image = "cobble_blood_2_new"))
                self.posX += skip_step

            self.posY += skip_step
            self.posX = self.startX


    def draw(self):
        for tiles in self.current_level:
            tiles.draw()