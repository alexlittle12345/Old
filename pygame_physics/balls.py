import pygame
import math
import numpy as np
import random


# --- Colors for pygame visual
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (255, 255, 153)
RED = (255, 0, 0)
BLUE = (102, 178, 255)
GREY = (211, 211, 211)

# --- Initialize pygame screen
pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)



ball_set = []
class Ball():
    """ ball class """

    def __init__(self, pos, vel, acc, m, size):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0],vel[1]]
        self.acc = [acc[0], acc[1]]
        self.m = m
        self.size = size
        self.color = BLACK
        self.thickness = 0
    
    def display(self):
        pygame.draw.circle(
            screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.size, self.thickness)
    
    def move(self):
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]

        self.vel[0] = self.vel[0] + self.acc[0]
        self.vel[1] = self.vel[1] + self.acc[1]
    
    def r(self):
        return self.size # return radius
    
    def mom(self):
        return self.m * self.vel

def dist_diff(ball1, ball2):
    x_diff = (ball1.pos[0] - ball2.pos[0])
    y_diff = (ball1.pos[1] - ball2.pos[1])
    return math.sqrt(x_diff ** 2 + y_diff ** 2)

# Dot product function, instead of importing numpy. Does not error check for diff vector lengths
def dot(v1, v2):
    sum = 0
    vec_len = len(v1)
    for i in range(vec_len):
        sum = sum + v1[i]*v2[i]
    return sum

def collisionDetectWalls():

    """
    for ball in ball_set:
        if ball.pos[0] > size[0] + ball.size:
            ball.pos[0] = - ball.size
        if ball.pos[1] > size[1] + ball.size:
            ball.pos[1] = - ball.size
        if ball.pos[0] < - ball.size:
            ball.pos[0] = size[0] + ball.size
        if ball.pos[1] < - ball.size:
            ball.pos[1] = size[1] + ball.size
    """

    for ball in ball_set:
        if ball.pos[0] > size[0] - ball.size:
            ball.vel[0] = - ball.vel[0]
        if ball.pos[1] > size[1] - ball.size:
            ball.vel[1] = - ball.vel[1]
        if ball.pos[0] < ball.size:
            ball.vel[0] = - ball.vel[0]
        if ball.pos[1] < ball.size:
            ball.vel[1] = - ball.vel[1]


def collisionDetectBalls():
    # Create list of colliding balls
    collision_list = []
    for ball1 in ball_set:
        for ball2 in ball_set:
            if ball1 != ball2:
                if dist_diff(ball1, ball2) <= ball1.r() + ball2.r():
                    if (ball1, ball2) not in collision_list and (ball2, ball1) not in collision_list:
                        collision_list.append((ball1, ball2))
                        #print (collision_list)
    
    
    for (ball1, ball2) in collision_list:
        v1 = np.array(ball1.vel)
        v2 = np.array(ball2.vel)
        p1 = np.array(ball1.pos)
        p2 = np.array(ball2.pos)

        v1n = v1 - (2*ball2.m)/(ball1.m+ball2.m) * (np.dot(v1 - v2, p1 - p2)/(np.linalg.norm(p1 - p2)**2))*(p1 - p2)
        v2n = v2 - (2*ball1.m)/(ball1.m+ball2.m) * (np.dot(v2 - v1, p2 - p1)/(np.linalg.norm(p2 - p1)**2))*(p2 - p1)

        ball1.vel = v1n
        ball2.vel = v2n
        

def gravity():
    for ball in ball_set:
        ball.vel[0] = ball.vel[0]
        ball.vel[1] = ball.vel[1] + 0.2

     

# --- Initialize balls
ball_size = 10
for i in range(2):
    for j in range(2):
        x = random.uniform(ball_size, size[0]-ball_size)
        y = random.uniform(ball_size, size[1]-ball_size)
        v_x = random.uniform(0, 1)
        v_y = random.uniform(0, 1)

        ball = Ball((x,y),(v_x, v_y), (0, 0), 1, ball_size)
        ball_set.append(ball)

#ball_set.append(Ball((150, 200), (0, -8), (0, 0), 1, ball_size))



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
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            print (pos)


    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    e = 0
    m = 0
    mom = 0
    for ball in ball_set:
        ball.display()

        e = e + 0.5 * ball.m * (np.linalg.norm(ball.vel)**2)
        m = m + ball.m
        mom = mom + ball.m * np.linalg.norm(ball.vel)
    
    print (e, m, mom)


    

    # --- Detect collisions
    collisionDetectWalls()
    collisionDetectBalls()

    # --- Gravity
    gravity()


    # --- Update movement
    for ball in ball_set:
        ball.move()

                
    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
