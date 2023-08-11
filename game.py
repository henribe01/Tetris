import pygame
from pieces import Piece
import numpy as np
import random
from config import config

block_size = config['game_settings']['block_size']
board_width = config['game_settings']['board_width']
board_height = config['game_settings']['board_height']
line_width = config['screen_settings']['line_width']


class Tetris:
    def __init__(self):
        self._board = np.array([['0'] * 10] * 20)
        self._current_piece = None
        self._next_piece = None
        self._running = True
        self._screen = pygame.display.set_mode((
            config['screen_settings']['screen_width'],
            config['screen_settings']['screen_height']))
        self._clock = pygame.time.Clock()
        self.score = 0
        # Milliseconds after which the move_down event is triggered
        self.move_down_interval = config['events']['move_down_interval']

    def new_piece(self) -> Piece:
        """
        Selects a random piece and initializes it at the top of the board
        :return: Piece
        """
        shapes = Piece.piece_shapes.keys()
        shape = random.choice(list(shapes))
        return Piece(
            config['game_settings']['board_width'] // 2 - len(shape) // 2, 0,
            shape)

    def valid_move(self, piece: Piece, x: int, y: int) -> bool:
        """
        Checks if a move is valid
        :param piece: Piece that is being moved
        :param x: x to move by
        :param y: y to move by
        :return: True if valid, False if invalid
        """
        for i, row in enumerate(piece.shape):
            for j, block in enumerate(row):
                if block != '0':
                    if piece.x + j + x < 0 or piece.x + j + x >= \
                            config['game_settings']['board_width']:
                        return False
                    if piece.y + i + y >= config['game_settings'][
                        'board_height']:
                        return False
                    if self._board[piece.y + i + y][piece.x + j + x] != '0':
                        return False
        return True

    def _handle_events(self) -> None:
        """
        Handles pygame events
        :return: None
        """
        move_directions = {pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0),
                           pygame.K_DOWN: (0, 1)}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key in move_directions:
                    if self.valid_move(self._current_piece,
                                       *move_directions[event.key]):
                        self._current_piece.move(
                            *move_directions[event.key])
                if event.key == pygame.K_q:
                    self._current_piece.rotate(False)
                if event.key == pygame.K_e:
                    self._current_piece.rotate()
                if event.key == pygame.K_SPACE:
                    while self.valid_move(self._current_piece, 0, 1):
                        self._current_piece.move(0, 1)
                    self.lock_piece(self._current_piece)

    def lock_piece(self, piece: Piece) -> None:
        """
        Locks a piece in place, creating a new piece
        :param piece: Piece to lock
        :return: None
        """
        for i, row in enumerate(piece.shape):
            for j, block in enumerate(row):
                if block != '0':
                    self._board[piece.y + i][piece.x + j] = block
        self._current_piece = self._next_piece
        self._next_piece = self.new_piece()

    def move_down(self) -> None:
        """
        Moves the current piece down if possible, otherwise locks it in place
        :return: None
        """
        if self.valid_move(self._current_piece, 0, 1):
            self._current_piece.move(0, 1)
        else:
            self.lock_piece(self._current_piece)

    def clear_lines(self) -> None:
        """
        Clears lines that are full
        :return: None
        """
        for i, row in enumerate(self._board):
            if '0' not in row:
                self._board = np.delete(self._board, i, 0)
                self._board = np.insert(self._board, 0, ['0'] * 10, 0)
                self.score += 100  # Increment score
                self.move_down_interval -= 5  # Speed up game

    def check_game_over(self) -> bool:
        """
        Checks if the game is over
        :return: True if game over, False otherwise
        """
        for block in self._board[0]:
            if block != '0':
                return True
        return False

    def _draw(self) -> None:
        """
        Draws the game
        :return: None
        """
        # Draw background

        self._screen.fill(config['colors']['black'])
        # Draw borders
        pygame.draw.rect(self._screen, config['colors']['white'], (
            0, 0, block_size * board_width + line_width * 2,
            block_size * board_height + line_width * 2), line_width)

        # Draw score
        score_text = pygame.font.SysFont('Arial', 32).render(
            f'Score: {self.score}', True, config['colors']['white'])
        self._screen.blit(score_text, (block_size * board_width + 20, 20))

        # Draw board
        for y, row in enumerate(self._board):
            for x, block in enumerate(row):
                if block != '0':
                    pygame.draw.rect(self._screen, Piece.colors[block], (
                        x * block_size + line_width,
                        y * block_size + line_width,
                        block_size,
                        block_size))

        # Draw current piece
        for y, row in enumerate(self._current_piece.shape):
            for x, block in enumerate(row):
                if block != '0':
                    pygame.draw.rect(self._screen, Piece.colors[block], (
                        (x + self._current_piece.x) * block_size + line_width,
                        (y + self._current_piece.y) * block_size + line_width,
                        block_size,
                        block_size
                    ))

        # Draw grid
        for i in range(board_width):
            pygame.draw.line(self._screen, config['colors']['white'], (
                i * block_size + line_width,
                line_width), (i * block_size + line_width,
                              block_size * board_height + line_width))
        for i in range(board_height):
            pygame.draw.line(self._screen, config['colors']['white'], (
                line_width,
                i * block_size + line_width), (
                                 block_size * board_width + line_width,
                                 i * block_size + line_width))

        # Draw next piece
        next_text = pygame.font.SysFont('Arial', 32).render(
            'Next:', True, config['colors']['white'])
        self._screen.blit(next_text, (block_size * board_width + 20, 100))

        for y, row in enumerate(self._next_piece.shape):
            for x, block in enumerate(row):
                if block != '0':
                    pygame.draw.rect(self._screen, Piece.colors[block], (
                        (x + board_width + 1) * block_size + line_width,
                        (y + 3) * block_size + line_width + 20,
                        block_size,
                        block_size
                    ))
        pygame.display.flip()

    def run(self) -> None:
        """
        Starts the game and runs the main loop
        :return: None
        """
        pygame.init()

        self._running = True
        self._current_piece = self.new_piece()
        self._next_piece = self.new_piece()

        time_since_last_move_down = 0

        while self._running:
            time_since_last_move_down += self._clock.get_time()
            if time_since_last_move_down >= self.move_down_interval:
                time_since_last_move_down = 0
                self.move_down()
                self.clear_lines()
            self._handle_events()
            self._draw()
            self._clock.tick(config['game_settings']['fps'])
