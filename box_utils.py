import random

# Constants
SCREEN_WIDTH = 800
BOX_WIDTH = 40
BOX_HEIGHT = 200

def shuffle_boxes():
    possible_x_positions = list(range(0, SCREEN_WIDTH - BOX_WIDTH, BOX_WIDTH))
    random.shuffle(possible_x_positions)  # Shuffle the positions to vary their order
    return [(x, 600 - 50 - BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT) for x in possible_x_positions[:20]]
