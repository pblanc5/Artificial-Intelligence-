# Author: Patrick Blanchard
# Descprition: An example of a simple reflex agent that does not know it's current location
#

import matplotlib.pyplot as plt
import numpy as np
import environment
import random

class RSRA():

    def __init__(self, env):
        self.points = 0
        self.mem = [1 if x == 'Clean' else 0  for x in env.State]


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
        self.points += 10
        print("SUCK")

    def Noop(self):
        print("NOOP")

    def clean(self, env):
        curIndex = env.Location.index(1)
        if self.mem.count(1) == 3:
            self.Noop()
        elif self.status(env) == "Dirty":
            self.suck(env)
            self.mem[curIndex] = 1
        else:
            self.mem[curIndex] = 1
            choice = random.randrange(0,2)
            if choice == 0 and curIndex != 2:
                self.right(env)
            elif choice == 1 and curIndex != 0:
                self.left(env)
            else:
                self.Noop()

if __name__ == "__main__":
    WORLD = environment.environment()
    CLEANER = RSRA(WORLD)
    x_axis = np.arange(0, 100, 1)
    y_axis = []

    print (WORLD.Location)
    print(WORLD.State)
    for t in range(0,100):
        print("Time:"+str(t), end=', ')
        print("State:"+CLEANER.status(WORLD), end=', Action:')
        CLEANER.clean(WORLD)
        y_axis.append(CLEANER.points)
    print("Points: " + str(CLEANER.points))

    plt.plot(x_axis, y_axis)
    plt.xlabel("time")
    plt.ylabel("points")
    plt.title("Random Simple Reflex Agent")
    plt.grid(True)
    plt.show()
