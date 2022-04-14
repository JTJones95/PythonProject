import numpy as np
import matplotlib.pyplot as plt
from calculate import Calculate

class Table(object):
    def __init__(self, size, seed = "Random"):
        if seed == 'Random':
            self.state = np.random.randint(2, size = size)
        self.calculate = Calculate(self)
        self.iteration = 0
    def animate(self):
        i = self.iteration
        im = None
        plt.title("Game of Life")
        while i < 50:
            plt.ion()
            im = plt.imshow(self.state, vmin = 0, vmax = 1, cmap = plt.cm.gray)
            i += 1
            print(i)
            plt.pause(0.05)
            yield self