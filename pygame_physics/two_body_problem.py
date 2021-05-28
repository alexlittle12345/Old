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
size = [1000, 700]
screen = pygame.display.set_mode(size)

ball_set = []


class Ball():
    """ ball class """

    def __init__(self, pos, vel, acc, m, size):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.acc = [acc[0], acc[1]]
        self.m = m
        self.size = size
        self.color = BLACK
        self.thickness = 0
        ball_set.append(self)

    def display(self):
        pygame.draw.circle(
            screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.size, self.thickness)

    def move(self):
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]

        self.vel[0] = self.vel[0] + self.acc[0]
        self.vel[1] = self.vel[1] + self.acc[1]

    def r(self):
        return self.size  # return radius

    def mom(self):
        return self.m * self.vel  # return momentum


def rel_vec(ball1, ball2):
    x_diff = ball1.pos[0] - ball2.pos[0]
    y_diff = ball1.pos[1] - ball2.pos[1]
    return np.array([x_diff, y_diff])


def rel_dist(ball1, ball2):
    x_diff = ball1.pos[0] - ball2.pos[0]
    y_diff = ball1.pos[1] - ball2.pos[1]
    rel_vec = np.array([x_diff, y_diff])
    return np.linalg.norm(rel_vec)


planet1 = Ball([300, 50], [0.5, 0], [0, 0], 7, 30)
planet2 = Ball([700, 650], [-0.5, 0], [0, 0], 7, 30)


def gravity(planet):
    G = 0.002
    force = np.array([0,0])
    for body in ball_set:
        if body != planet:
            force = force + -((G * planet.m * body.m) / rel_dist(planet, body))*rel_vec(planet, body)
    
    return force


def update_acc():
    # Add forces together for each planet
    for planet in ball_set:
        force = gravity(planet)  # add forces here
        planet.acc = (force / planet.m)


def update_vec():
    for planet in ball_set:
        planet.vel = planet.vel + planet.acc


def update_pos():
    for planet in ball_set:
        planet.pos = planet.pos + planet.vel


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
            ball_set.append(Ball(pos, [0, 0], [0, 0], 0.1, 3))

    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    for ball in ball_set:
        ball.display()

    update_acc()
    update_vec()
    update_pos()

    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
