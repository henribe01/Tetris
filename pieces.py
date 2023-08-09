import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

board = [[0] * 10] * 20


class Piece:
    def __init__(self, x: int, y: int, shape: list) -> None:
        """
        Creates a new piece
        :param x: Initial x position
        :param y: Initial y position
        :param shape: 2D quadratic list representing the shape of the piece
        """
        self.x = x
        self.y = y
        self.shape = shape

    def rotate(self, clockwise: bool = True) -> None:
        """
        Rotates the piece clockwise or counterclockwise
        :param clockwise: True if the piece should be rotated clockwise
        :return: None
        """
        if clockwise:
            self.shape = list(zip(*self.shape[::-1]))
        else:
            self.shape = list(zip(*self.shape))[::-1]

    def move(self, x: int, y: int) -> None:
        """
        Moves the piece by x and y
        :param x: x offset
        :param y: y offset
        :return: None
        """
        self.x += x
        self.y += y

