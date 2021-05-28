import pygame
import math
import numpy as np

# --- Colors for pygame visual
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (255, 255, 153)
RED = (255, 0, 0)
BLUE = (102, 178, 255)
GREY = (211, 211, 211)

# --- Initialize pygame screen
pygame.init()
size = [500, 500]
screen = pygame.display.set_mode(size)


class Ball:
    def __init__(self, pos, radius) -> None:
        self.pos = pos
        self.radius = radius














balls = []



# --- Functions

def display_ball(ball):
    pygame.draw.circle(screen, BLACK, (ball.pos[0], ball.pos[1]), ball.radius, 0)


def draw_line(pos1, pos2):
    pass


# --- pygame code
pygame.display.set_caption("Visualization")
screen.fill(WHITE)

# Resize boxes depending on screen size

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
            pos = pygame.mouse.get_pos()
            balls.append(Ball(pos, 5))

    # --- Screen-clearing code goes here

    # --- Go ahead and update the screen with what we've drawn
    screen.fill(WHITE)
    
    for ball in balls:
        display_ball(ball)

    # --- Limit to 60 frames per second
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()
