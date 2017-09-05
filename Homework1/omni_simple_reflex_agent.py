# Author: Patrick Blanchard
# Descprition: An example of a simple reflex agent that knows the state of all cells in the world.
#

import matplotlib.pyplot as plt
import numpy as np
import environment
import random

class OSRA():

    def __init__(self, env):
        self.points = 0
        self.mem = [1 if x == 'Clean' else 0  for x in env.State]

    def loc(self, env):
        curIndex = env.Location.index(1)
        if curIndex == 0:
            return 'A'
        elif curIndex == 1:
            return 'B'
        else:
            return 'C'


    def status(self, env):
        curIndex = env.Location.index(1)
        state = env.State[curIndex]
        return state

    def left(self, env):
        curIndex = env.Location.index(1)
        env.Location[curIndex] = 0
        env.Location[curIndex - 1] = 1
        self.points -= 1
        print("LEFT")

    def right(self, env):
        curIndex = env.Location.index(1)
        env.Location[curIndex] = 0
        env.Location[curIndex + 1] = 1
        self.points -= 1
        print("RIGHT")

    def suck(self, env):
        curIndex = env.Location.index(1)
        env.State[curIndex] = "Clean"
        self.mem[curIndex] = 1
        self.points += 10
        print("SUCK")

    def Noop(self):
        print("NOOP")

    def clean(self, env):
        curIndex = env.Location.index(1)
        location = self.loc(env)
        if self.mem.count(1) == 3:
            self.Noop()
        elif self.status(env) == "Dirty":
            self.suck(env)
        elif location == 'A':
            self.right(env)
        elif location == 'C':
            self.left(env)
        else:
            if self.mem[0] == 0:
                self.left(env)
            else:
                self.right(env)

if __name__ == "__main__":
    WORLD = environment.environment()
    CLEANER = OSRA(WORLD)
    x_axis = np.arange(0, 100, 1)
    y_axis = []

    print(WORLD.Location)
    print(WORLD.State)
    for t in range(0,100):
        print("Time:"+str(t), end=', ')
        print("Location:"+str(CLEANER.loc(WORLD)), end=', ')
        print("State:"+CLEANER.status(WORLD), end=', Action:')
        CLEANER.clean(WORLD)
        y_axis.append(CLEANER.points)
    print("Points: " + str(CLEANER.points))

    plt.plot(x_axis, y_axis)
    plt.xlabel("time")
    plt.ylabel("points")
    plt.title("Omni Simple Reflex Agent")
    plt.grid(True)
    plt.show()
