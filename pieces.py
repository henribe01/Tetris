import numpy as np
from config import config


class Piece:
    piece_shapes = {'I': np.array([['0'] * 4, ['I'] * 4, ['0'] * 4, ['0'] * 4]),
                    'J': np.array(
                        [['J', '0', '0'], ['J', 'J', 'J'], ['0', '0', '0']]),
                    'L': np.array(
                        [['0', '0', 'L'], ['L', 'L', 'L'], ['0', '0', '0']]),
                    'O': np.array([['O', 'O'], ['O', 'O']]),
                    'S': np.array(
                        [['0', 'S', 'S'], ['S', 'S', '0'], ['0', '0', '0']]),
                    'T': np.array(
                        [['0', 'T', '0'], ['T', 'T', 'T'], ['0', '0', '0']]),
                    'Z': np.array(
                        [['Z', 'Z', '0'], ['0', 'Z', 'Z'], ['0', '0', '0']])}
    colors = {'I': config['colors']['light_blue'],
              'J': config['colors']['dark_blue'],
              'L': config['colors']['orange'],
              'O': config['colors']['yellow'],
              'S': config['colors']['green'],
              'T': config['colors']['purple'],
              'Z': config['colors']['red']
              }

    def __init__(self, x: int, y: int, shape: str):
        self.x = x
        self.y = y
        self.shape = Piece.piece_shapes[shape]

    def rotate(self, turn_clockwise: bool = True):
        """
        Rotates the piece 90 degrees clockwise or counterclockwise
        :param turn_clockwise: True for clockwise, False for counterclockwise
        :return: None
        """
        if turn_clockwise:
            self.shape = np.rot90(self.shape, k=-1)
        else:
            self.shape = np.rot90(self.shape, k=1)

    def move(self, x: int, y: int):
        """
        Moves the piece by x and y
        :param x: x to move by
        :param y: y to move by
        :return: None
        """
        self.x += x
        self.y += y
