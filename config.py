import pygame

config = {
    'screen': {
        'width': 600,
        'height': 800,
        'caption': 'Tetris'
    },
    'events': {
        'move_down': pygame.USEREVENT + 1
    },
    'colors': {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'light_blue': (0, 255, 255),
        'blue': (0, 0, 255),
        'orange': (255, 165, 0),
        'yellow': (255, 255, 0),
        'green': (0, 255, 0),
        'purple': (128, 0, 128),
        'red': (255, 0, 0)
    },
    'block_size': 30,
    'move_down_timer': 1000,
}
