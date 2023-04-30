import pygame as pg

from player import Player
from settings import *


class Level:
    def __init__(self) -> None:
        # get the display surface
        self.display_surface = pg.display.get_surface()

        # sprite groups
        self.all_sprites = pg.sprite.Group()

        # call setup function
        self.setup()

    def setup(self):
        # sprite player
        self.player = Player(WHITE, (25, 50), self.all_sprites)

    def run(self, dt) -> None:
        self.display_surface.fill(BLACK)
        # draw
        self.all_sprites.draw(self.display_surface)
        # update
        self.all_sprites.update(dt)
