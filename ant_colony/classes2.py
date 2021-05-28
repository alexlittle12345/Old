import random
import numpy as np
from pygame import Vector2
import math


# --- Colors for pygame visual
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (51, 200, 0)
RED = (255, 0, 0)
BLUE = (102, 178, 255)
GREY = (211, 211, 211)

# --- Tile types
_HOME = 'home'
_FOOD = 'food'
_WALL = 'wall'
_EMPTY = 'empty'


class Ant:
    def __init__(self, pos: Vector2, dir: Vector2, color, size, change_dir_tend) -> None:
        self.pos = pos
        self.color = color
        self.size = size
        self.dir = dir
        self.change_dir_tend = change_dir_tend

        self.food = 0

    def update(self, tiles):

        self.move(tiles)


    def move(self, tiles):

        # Randomly change direction
        change_dir_trigger = random.choices(
            [0, 1], weights=[1-self.change_dir_tend, self.change_dir_tend], k=1)
        if change_dir_trigger[0] == 1:
            dir_array = self.dir
            theta = np.radians(random.random()*360)
            c, s = np.cos(theta), np.sin(theta)
            R = np.array(((c, -s), (s, c)))
            dir_array = np.matmul(R, dir_array)
            self.dir = dir_array

        self.pos = self.pos + self.dir







class Tile:
    def __init__(self, loc : Vector2, type = 'empty') -> None:
        self.count = 0
        self.loc = loc
        self.type = type # type can be 'empty', 'home', 'food', 'wall'
        
        
        self.update()
    

    def update(self):
        if self.type == _HOME:
            self.color = RED
        elif self.type == _FOOD:
            self.color = GREEN
        elif self.type == _WALL:
            self.color = GREY
        else: self.color = WHITE
