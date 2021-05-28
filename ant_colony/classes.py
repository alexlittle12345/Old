import random
import numpy as np
from pygame import Vector2, draw




class Ant:
    def __init__(self, pos : Vector2, dir : Vector2, color, size, change_dir_tend) -> None:
        self.pos = pos
        self.color = color
        self.size = size
        self.dir = dir
        self.change_dir_tend = change_dir_tend
 
        self.nearest_food_vec = Vector2(0,0)
        self.has_food = False
        self.food = 0
    
    def update(self, foods):
        self.move()
        self.detect_food(foods)
        self.trail.path.append(self.pos)

        #print(self.trail.path[-1])

        if self.pos.distance_to(Vector2(0,0)) < self.size/2 and self.has_food == True:
            self.has_food = False
            self.food.collected = True



    def move(self):


        if self.has_food == True:
            self.pos = self.pos - self.pos.normalize()
        else:
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

            if self.nearest_food_vec != Vector2(0, 0):
                self.dir = self.nearest_food_vec

            self.pos = self.pos + self.dir
            

      

    def detect_food(self, food_list : list):
        if self.has_food == False:
            food_list = [food for food in food_list if food.taken == False]
            
            foods = []
            food_vecs = []
            food_distances = []
            for food in food_list:
                if self.pos.distance_to(food.pos) < 50:
                    foods.append(food)
                    food_vecs.append(food.pos)
                    food_distances.append(self.pos.distance_to(food.pos))
            
            if food_distances != []:
                min_dist = min(food_distances)
                locate = [i for i, j in enumerate(food_distances) if j == min_dist][0]
                nearest_food_vec = (food_vecs[locate]-self.pos).normalize()
                self.take_food(foods[locate])
            else: nearest_food_vec = Vector2(0,0)

            self.nearest_food_vec = nearest_food_vec

        
    
    def take_food(self, food):
        if self.pos.distance_to(food.pos) <= 1:
            food.taken = True
            food.owner = self
            self.has_food = True
            self.food = food

 


class Food:
    def __init__(self, pos: Vector2):
        self.pos = pos
        self.taken = False
        self.collected = False

        self.owner = 0
    
    def update_pos(self):
        if self.owner != 0:
            self.pos = self.owner.pos
    

