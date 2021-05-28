import pygame
import math
import numpy as np
import random
import classes2
from pygame import Vector2


# --- Colors for pygame visual
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (51, 200, 0)
RED = (255, 0, 0)
BLUE = (102, 178, 255)
GREY = (211, 211, 211)

# --- Initialize pygame screen
pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)

# --- Initialize ants
ant_count = 1
ant_size = 20
avg_speed = 1
change_dir_tend = 0.04
ant_color = BLACK
ants = []

init_positions = []
init_dir = []
for i in range(ant_count):
    init_position = [5, 5]

    # Random initial direction:
    theta = np.radians(random.random()*360)
    init_direction = [np.cos(theta)*avg_speed, np.sin(theta)*avg_speed]

    new_ant = classes2.Ant(Vector2(init_position),
                          Vector2(init_direction),
                          ant_color,
                          ant_size,
                          change_dir_tend)
    ants.append(new_ant)



# --- Initialize tiles
tiles = []



# FUNCTIONS ---------------------------------------------------------------------------------------------

def display_ant(ant: classes2.Ant):
    pygame.draw.rect(screen, ant.color,
                     (ant.pos[0], ant.pos[1], ant.size, ant.size))


def display_tile(tile: classes2.Tile):
    pygame.draw.rect(screen, tile.color,
                     (tile.loc[0], tile.loc[1], ant_size, ant_size))


# calculate tile position in tiles list from vector position on screen
def tile_number(pos : Vector2): 
    x = math.floor(pos[0] / ant_size)
    y = math.floor(pos[1] / ant_size)
    tile_number = int(y*(size[0]/ant_size) + x)
    return tile_number



def boundary_check(ants):
    for ant in ants:
        if ant.pos[0] + ant.dir[0] >= size[0]:
            ant.dir[0] = -ant.dir[0]
        if ant.pos[1] + ant.dir[1] >= size[1]:
            ant.dir[1] = -ant.dir[1]
        if ant.pos[0] + ant.dir[0] <= 0:
            ant.dir[0] = -ant.dir[0]
        if ant.pos[1] + ant.dir[1] <= 0:
            ant.dir[1] = -ant.dir[1]



# START -------------------------------------------------------------------------------------------------

pygame.display.set_caption("Visualization")
screen.fill(WHITE)

# Loop until user clicks the close button
done = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

while not done:
    # --- Game logic should go here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                pos = Vector2(pygame.mouse.get_pos())
                new_tile = classes2.Tile(pos, type='food')
                tiles.append(new_tile)
            if mouse_presses[2]:
                pos = Vector2(pygame.mouse.get_pos())
                new_tile = classes2.Tile(pos, type='wall')
                tiles.append(new_tile)


            

    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    
    # --- Draw / update tiles
    for i in range(len(tiles)):
        tiles[i].update()
        display_tile(tiles[i])



    # --- Draw / update ants
    for i in range(len(ants)):
        ants[i].update(tiles)
        display_ant(ants[i])




    # --- Detect collisions
    boundary_check(ants)

    # --- Update movement

    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
