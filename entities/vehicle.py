import pygame
from pygame import Vector2, Color, Surface
from .vectorhelper import VectorHelper


class Vehicle():
    """
    class represent vehicle
    """

    def __init__(self, position: Vector2, color: Color, radius: int) -> None:
        self._color = color
        self._radius = radius
        self._position = position
        self._velocity = Vector2(0, 0)
        self._acceleration = Vector2(0.1, 0.5)

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, self._color, self._position, self._radius)

    def update(self, screen: Surface) -> None:
        self._velocity = VectorHelper.add(self._velocity, self._acceleration)

        self._position = VectorHelper.add(self._position, self._velocity)

        # bounds
        if self._position.x >= screen.get_width() - self._radius or self._position.x <= 0:
            self._velocity.x = self._velocity.x * -1

        if self._position.y >= screen.get_height() - self._radius or self._position.y <= 0:
            self._velocity.y = self._velocity.y * -1
