import gym
import numpy as np
from gym.spaces import Discrete, Box
import random

class Action():
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class SimpleMazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # ACTION SPACE
        self.action_space = gym.spaces.Discrete(4)

        # OBSERVATION SPACE
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(4, 4))

        # CREATE GRID
        self.grid = np.zeros((4, 4))

        global x_coor_1
        global y_coor_1
        x_coor_1 = random.randrange(0, 3)
        y_coor_1 = random.randrange(0, 3)
        self.grid[x_coor_1, y_coor_1] = 1

        global x_coor_2
        global y_coor_2
        x_coor_2 = random.randrange(0, 3)
        y_coor_2 = random.randrange(0, 3)
        self.grid[x_coor_2, y_coor_2] = 1

    def move_agent1(self, action_1):
        global x_coor_1, y_coor_1
        self.grid[x_coor_1, y_coor_1] = 0
        if action_1 == "UP":
            y_coor_1 = y_coor_1 + 1
        elif action_1 == "RIGHT":
            x_coor_1 = x_coor_1 + 1
        elif action_1 == "DOWN":
            y_coor_1 = y_coor_1 - 1
        else:
            x_coor_1 = x_coor_1 - 1
        if x_coor_1==-1 or y_coor_1==-1:
            self.grid[x_coor_1, y_coor_1] = 0
        else:
            self.grid[x_coor_1, y_coor_1] = 1
        return self.grid

    def move_agent2(self, action_2):
        global x_coor_2, y_coor_2
        self.grid[x_coor_2, y_coor_2] = 0
        if action_2 == "UP":
            y_coor_2 = y_coor_2 + 1
        elif action_2 == "RIGHT":
            x_coor_2 = x_coor_2 + 1
        elif action_2 == "DOWN":
            y_coor_2 = y_coor_2 - 1
        else:
            x_coor_2 = x_coor_2 - 1
        if x_coor_2==-1 or y_coor_2==-1:
            self.grid[x_coor_2, y_coor_2] = 0
        else:
            self.grid[x_coor_2, y_coor_2] = 1
        return self.grid

    def off_grid(self):
        count = 0
        for i in range(0,3):
            for j in range(0,3):
                if self.grid[i,j]==1:
                    count += 1
        if count==2:
            return False
        else:
            return True

    def step(self, a):
        done = False
        action_1 = a[0]
        action_2 = a[1]
        self.move_agent1(action_1)
        self.move_agent2(action_2)
        if self.off_grid() == True:
            done = True
            reward = -5
        reward = 1
        info={}
        return self.grid, reward, done, info

    def render(self, mode="human"):
        print(self.grid)

    def reset(self):
        # ACTION SPACE
        self.action_space = gym.spaces.Discrete(4)

        # OBSERVATION SPACE
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(4, 4))

        # CREATE GRID
        self.grid = np.zeros((4, 4))

        global x_coor_1
        global y_coor_1
        x_coor_1 = random.randrange(0, 3)
        y_coor_1 = random.randrange(0, 3)
        self.grid[x_coor_1, y_coor_1] = 1

        global x_coor_2
        global y_coor_2
        x_coor_2 = random.randrange(0, 3)
        y_coor_2 = random.randrange(0, 3)
        self.grid[x_coor_2, y_coor_2] = 1

        return self.grid