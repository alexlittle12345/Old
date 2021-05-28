import copy
import numpy as np
from math import inf



class TicTacToe():
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.state = [0]*9
        self.turn = 1
        return self.state
    
    def matrix(self, s):
        matrix_rep = []
        for i in range(3):
            a = []
            for j in range(3):
                a.append(s[3*i+j])
            matrix_rep.append(a)
        return matrix_rep
    
    def print(self):
        s = self.matrix(env.state)
        print(str(s).replace('],', ']\n'))
    
    def observation_space(self):
        self.shape = (9,)

    def action_space(self):
        self.n = 9
        return self.n
    
    def iswinner(self, player):
        s = self.state
        for i in range(3):
            # Check rows
            if all([x == player for x in s[3*i:3*i+3]]):
                return True
            # Check cols
            if all([x == player for x in [s[i], s[3+i], s[6+i]]]):
                return True
        # Check diagonals
        if all([x == player for x in [s[0], s[4], s[8]]]):
            return True
        if all([x == player for x in [s[2], s[4], s[6]]]):
            return True
        return False
    
    def who_won(self):
        s = self.state
        winner = 0
        for i in range(3):
            # Check rows
            if all([x == 1 for x in s[3*i:3*i+3]]):
                winner = 1
            # Check cols
            if all([x == 1 for x in [s[i], s[3+i], s[6+i]]]):
                winner = 1
        # Check diagonals
        if all([x == 1 for x in [s[0], s[4], s[8]]]):
            winner = 1
        if all([x == 1 for x in [s[2], s[4], s[6]]]):
            winner = 1

        for i in range(3):
            # Check rows
            if all([x == -1 for x in s[3*i:3*i+3]]):
                winner = -1
            # Check cols
            if all([x == -1 for x in [s[i], s[3+i], s[6+i]]]):
                winner = -1
        # Check diagonals
        if all([x == -1 for x in [s[0], s[4], s[8]]]):
            winner = -1
        if all([x == -1 for x in [s[2], s[4], s[6]]]):
            winner = -1

        return winner
    
    def done(self):
        if self.who_won() == 0 and env.state.count(0) == 0:
            return False
        elif self.who_won() == 0:
            return False
        else:
            return True
    
    def evaluate(self, state):
        if self.iswinner(1) == True:
            score = +1
        elif self.iswinner(-1) == True:
            score = -1
        else: score = 0

        return score

    def step(self, pos, player):
        if self.state[pos] != 0:
            return self.state
        else:
            self.state[pos] = player
            
        return self.state

def minimax(env, depth, player):
    pos_moves = [i for i, x in enumerate(env.state) if x == 0]
    if player == 1:
        best = [-1, -inf]
    else:
        best = [-1, inf]
    
    if depth == 0 or env.done() == True:
        score = env.evaluate(env.state)
        return [-1, score]

    
    for i in pos_moves:
        new_env = copy.deepcopy(env)
        new_env.step(i, player)
        score = minimax(new_env, depth - 1, -player)
        score[0] = i

        if player == 1:
            if score[1] > best[1]:
                best = score # Max value
        else:
            if score[1] < best[1]:
                best = score # Min value
    return best


env = TicTacToe()
def play_game(first_player):
    

    if first_player == 'Y':
        user_inp = int(input('Your move (0 - 8): '))
        env.step(user_inp, 1)

    done = False
    move_count = 9 - env.state.count(0)
    while done == False:

        move_count = move_count + 1
        if move_count % 2 == 1:
            player = 1
        else: player = -1

        if env.iswinner(player) == True:
            done = True
            break
        elif env.state.count(0) == 0:
            done = True
            break
        else:
            done = False

        depth = len([i for i, x in enumerate(env.state) if x == 0])
        move = minimax(env, depth, player)
        env.step(move[0], player)
        env.print()

        if env.iswinner(player) == True:
            done = True
            break
        elif env.state.count(0) == 0:
            done = True
            break
        else:
            done = False

        user_inp = int(input('Your move (0 - 8): '))
        env.step(user_inp, -player)
        move_count = move_count + 1


user_inp = input('Do you want to go first (Y/N)?: ')
play_game(user_inp)

print (env.who_won())


