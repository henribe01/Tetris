import pygame


class Game:
    """Class to represent the game"""

    def __init__(self) -> None:
        self._running = False
        self._size = self._width, self._height = 800, 600
        self._screen = pygame.display.set_mode(self._size)
        self._clock = pygame.time.Clock()

    def handle_events(self, event: pygame.event.Event) -> None:
        """
        Handles events
        :param event: The event to handle
        :return: None
        """
        if event.type == pygame.QUIT:
            self._running = False

    def run(self) -> None:
        """
        Starts the game
        :return: None
        """
        self._running = True
        while self._running:
            for event in pygame.event.get():
                self.handle_events(event)
            self._screen.fill((0, 0, 0))
            pygame.display.flip()
            self._clock.tick(60)
        pygame.quit()
