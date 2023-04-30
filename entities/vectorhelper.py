from pygame import Vector2
import math


class VectorHelper():
    """
    class vector helper for helping operation with vector2 pygame class
    """

    @staticmethod
    def add(vec1: Vector2, vec2: Vector2) -> Vector2:
        """
        Add function to add another vector and  return new vector
        """
        vec: Vector2 = Vector2()
        vec.x = vec1.x + vec2.x
        vec.y = vec1.y + vec2.y
        return vec

    @staticmethod
    def sub(vec1: Vector2, vec2: Vector2) -> Vector2:
        """
        Sub function to sub another vector and  return new vector
        """
        vec: Vector2 = Vector2()
        vec.x = vec1.x - vec2.x
        vec.y = vec1.y - vec2.y
        return vec

    @staticmethod
    def mult(vec1: Vector2, n: float) -> Vector2:
        """
        Mult function to mult another vector and  return new vector
        """
        vec: Vector2 = Vector2()
        vec.x = vec1.x * n
        vec.y = vec1.y * n
        return vec

    @staticmethod
    def div(vec1: Vector2, n: float) -> Vector2:
        """
        Div function to div another vector and  return new vector
        """
        vec: Vector2 = Vector2()
        vec.x = vec1.x / n
        vec.y = vec1.y / n
        return vec

    @staticmethod
    def limit(vec1: Vector2, max: float) -> Vector2:
        """
        Limit function to Limit another vector and  return new vector
        """
        mult: float = 0
        length: float = math.sqrt(vec1.x**2 + vec1.y**2)
        vec: Vector2 = Vector2()
        if length > max:
            mult = max / length
        else:
            mult = 1.0

        vec.x = vec1.x * mult
        vec.y = vec1.y * mult
        return vec
