# Author: Patrick Blanchard
# Descprition: An environment to test simple reflex agents
#

import random

class environment():
    STATES = ["Clean", "Dirty"]
    State = ["Clean","Clean","Clean"]
    Location = [0,0,0]

    def __init__(self):
        for i in range(0, len(self.State)):
            self.State[i] = random.choice(self.STATES)
        self.Location[random.randrange(0, len(self.Location))] = 1

if __name__ == "__main__":
    env = environment()
    print (env.State)
    print (env.Location)
