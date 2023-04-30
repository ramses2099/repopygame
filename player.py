from typing import Any

import pygame as pg

from settings import *


class Player(pg.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, pos, group):
        # Call the parent class (Sprite) constructor
        pg.sprite.Sprite.__init__(self, group)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pg.Surface([P_WIDTH, P_HEIGTH])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=pos)

        # movement atrributes
        self.direction = pg.math.Vector2()
        self.position = pg.math.Vector2(self.rect.center)

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.direction.y = -1
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, dt):
        self.position += self.direction * P_SPEED * dt
        self.rect.center = self.position

    def update(self, dt) -> None:
        self.input()
        self.move(dt)
