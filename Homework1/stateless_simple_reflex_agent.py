# Author: Patrick Blanchard
# Descprition: An example of a simple reflex agent that cannot remember the state of a cell
#

import matplotlib.pyplot as plt
import numpy as np
import environment
import random

class Stateless_SRA():

    def __init__(self):
        self.points = 0

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
        return env.State[curIndex]

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
        self.points += 10
        print("SUCK")

    def clean(self, env):
        if self.status(env) == "Dirty":
            self.suck(env)
        elif(self.loc(env) == 'A'):
            self.right(env)
        elif(self.loc(env) == 'C'):
            self.left(env)
        else:
            choice = random.randrange(0,2)
            if choice == 0: self.right(env)
            else: self.left(env)

if __name__ == "__main__":
    WORLD = environment.environment()
    CLEANER = Stateless_SRA()
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
    plt.title("Stateless Simple Reflex Agent")
    plt.grid(True)
    plt.show()
