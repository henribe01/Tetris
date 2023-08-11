import pygame

config = {
    'game_settings': {
        'board_height': 20,
        'board_width': 10,
        'block_size': 40,
        'fps': 60,
    },
    'screen_settings': {
        'screen_width': 600,
        'screen_height': 800 + 10,
        'line_width': 5,
    },
    'colors': {
        'light_blue': (0, 255, 255),
        'dark_blue': (0, 0, 255),
        'orange': (255, 165, 0),
        'yellow': (255, 255, 0),
        'green': (0, 255, 0),
        'purple': (128, 0, 128),
        'red': (255, 0, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
    },
    'events': {
        'move_down_interval': 1000,
    },
}
