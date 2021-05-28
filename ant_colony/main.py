import pygame
import math
import numpy as np
import random
import classes
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
size = [500, 500]
screen = pygame.display.set_mode(size)

# --- Initialize ants
ant_count = 500
ant_size = 5
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

    new_ant = classes.Ant(Vector2(init_position),
                            Vector2(init_direction), 
                            ant_color, 
                            ant_size,
                            change_dir_tend)
    ants.append(new_ant)



# --- Initialize attractors
foods = []




# FUNCTIONS ---------------------------------------------------------------------------------------------

def display_ant(ant: classes.Ant):
    pygame.draw.rect(screen, ant.color, (ant.pos[0], ant.pos[1], ant.size, ant.size))


def display_food(food: classes.Food):
    pygame.draw.rect(screen, GREEN, (food.pos[0], food.pos[1], 5, 5))


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


def create_food_bundle(x, y):
    for i in range(x):
        for j in range(y):
            pos = Vector2(size[0] - 5*i, size[0] - 5*j)
            new_food = classes.Food(pos)
            foods.append(new_food)





create_food_bundle(20,20)


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = Vector2(pygame.mouse.get_pos())
            new_food = classes.Food(pos)
            foods.append(new_food)
            

    # --- Screen-clearing code goes here
    screen.fill(WHITE)




    # --- Drawing code should go here

    # --- Draw / update ants
    for i in range(len(ants)):
        ants[i].update(foods)

        ants[0].draw_trail = True
        if ants[i].draw_trail == True:
            for j in range(len(ants[i].trail.path)):
                if j > 0:
                    pygame.draw.line(
                        screen, RED, ants[i].trail.path[j-1], ants[i].trail.path[j])

        display_ant(ants[i])


    # --- Draw / update food
    foods = [food for food in foods if food.collected == False]
    for i in range(len(foods)):
        foods[i].update_pos()
        display_food(foods[i])
        

    boundary_check(ants)



    # --- Detect collisions

    # --- Update movement

    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(1000)

# Close the window and quit
pygame.quit()


