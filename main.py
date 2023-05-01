import sys

import pygame as pg

from level import Level
from settings import *
from support import *


class Game:
    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            dt = self.clock.tick(FPS) / 1000
            self.level.run(dt)

            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
