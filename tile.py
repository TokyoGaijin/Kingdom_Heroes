import pygame
import os

class Tile(object):
    def __init__(self, surface, posX, posY, tile_type = None, tile_image = None):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.size_w, self.size_y = 32, 32
        self.tile_type = tile_type
        self.tile_image = tile_image
        self.tile_art = pygame.image.load(os.path.join(f"elements/{self.tile_type}", f"{self.tile_image}.png"))
        self.bounding_block = pygame.Rect(self.size_w, self.size_y, self.posX, self.posY)
        self.tile_image = None

    def draw(self):
        self.surface.blit(self.tile_art, (self.posX, self.posY))