import pygame
import numpy as np
from config import config


class Piece:
    """Class to represent a piece"""
    all_shapes = {'I': np.array([[0] * 4, ['I'] * 4, [0] * 4, [0] * 4]),
                  'J': np.array([[0, 'J', 0], [0, 'J', 0], ['J', 'J', 0]]),
                  'L': np.array([[0, 'L', 0], [0, 'L', 0], [0, 'L', 'L']]),
                  'O': np.array([['O', 'O'], ['O', 'O']]),
                  'S': np.array([[0, 'S', 'S'], ['S', 'S', 0], [0, 0, 0]]),
                  'T': np.array([[0, 'T', 0], ['T', 'T', 'T'], [0, 0, 0]]),
                  'Z': np.array([['Z', 'Z', 0], [0, 'Z', 'Z'], [0, 0, 0]])}
    colors = {'I': config['colors']['light_blue'],
              'J': config['colors']['blue'],
              'L': config['colors']['orange'],
              'O': config['colors']['yellow'],
              'S': config['colors']['green'],
              'T': config['colors']['purple'],
              'Z': config['colors']['red']}

    def __init__(self, x: int, y: int, shape: str) -> None:
        """
        Creates a new piece
        :param x: Initial x position
        :param y: Initial y position
        :param shape: 2D quadratic list representing the shape of the piece
        """
        self.x = x
        self.y = y
        self.shape = self.all_shapes[shape]
        self.color = self.colors[shape]

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

    def can_move(self, x: int, y: int) -> bool:
        """
        Checks if the piece can move by x and y
        :param x: x offset
        :param y: y offset
        :return: True if the piece can move, False otherwise
        """
        if self.x + x < 0 or self.x + x + len(self.shape[0]) > 10:
            return False
        if self.y + y < 0 or self.y + y + len(self.shape) > 20:
            return False
        return True
