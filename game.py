import pygame
from pieces import Piece
import numpy as np
from config import config


class Game:
    """Class to represent the game"""

    def __init__(self) -> None:
        self._running = False
        self._size = self._width, self._height = 600, 800
        self._screen = pygame.display.set_mode(self._size)
        self._clock = pygame.time.Clock()
        self._block_size = self._height // 20

        # Attributes for the game logic
        self._board = np.array([['0'] * 10] * 20)
        self._current_piece = None

    def handle_events(self, event: pygame.event.Event) -> None:
        """
        Handles events
        :param event: The event to handle
        :return: None
        """
        if config['events']['move_down'] == event.type:
            print(self._current_piece.y)
            if self._current_piece.can_move(0, 1):
                self._current_piece.move(0, 1)
            else:
                self.set_piece_on_board(self._current_piece)
                self._current_piece = Piece(0, 0, 'I')

        match event.type:
            case pygame.QUIT:
                self._running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        self._current_piece.move(-1, 0)
                    case pygame.K_RIGHT:
                        self._current_piece.move(1, 0)
                    case pygame.K_DOWN:
                        self._current_piece.move(0, 1)
                    case pygame.K_q:
                        self._current_piece.rotate(False)
                    case pygame.K_e:
                        self._current_piece.rotate()

    def update_screen(self) -> None:
        """
        Updates the screen
        :return: None
        """
        self._screen.fill((0, 0, 0))

        # Draws the board
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] != '0':
                    pygame.draw.rect(self._screen,
                                     Piece.colors[self._board[i][j]], (
                                         j * self._block_size,
                                         i * self._block_size,
                                         self._block_size, self._block_size))

        # Draws the current piece
        for i in range(len(self._current_piece.shape)):
            for j in range(len(self._current_piece.shape[i])):
                if self._current_piece.shape[i][j] != '0':
                    pygame.draw.rect(self._screen,
                                     Piece.colors[
                                         self._current_piece.shape[i][j]],
                                     (
                                         self._current_piece.x * self._block_size + j * self._block_size,
                                         self._current_piece.y * self._block_size + i * self._block_size,
                                         self._block_size, self._block_size))

        pygame.display.flip()

    def set_piece_on_board(self, piece: Piece) -> None:
        """
        Sets the piece on the board
        :param piece: The piece to set on the board
        :return: None
        """
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[i])):
                if piece.shape[i][j] != '0':
                    self._board[piece.y + i][piece.x + j] = piece.shape[i][j]

    def run(self) -> None:
        """
        Starts the game
        :return: None
        """
        self._running = True
        pygame.time.set_timer(config['events']['move_down'],
                              config['move_down_timer'])

        self._current_piece = Piece(0, 0, 'I')
        while self._running:
            for event in pygame.event.get():
                self.handle_events(event)

            # Checks if the piece can move down

            # Updates the screen
            self.update_screen()

            # Limits the FPS to 60
            self._clock.tick(60)

        pygame.quit()
