import numpy as np
import matplotlib.pyplot as plt
from calculate import Calculate

class Table(object):
    def __init__(self, size):
        self.state = np.random.randint(2, size = size)
        self.calculate = Calculate(self)
        self.iteration = 0
    def animate(self):
        i = self.iteration
        im = None
        plt.title("Game of Life")
        while i < 600:
            if i == 0:
                plt.ion()
                im = plt.imshow(self.state, vmin = 0, vmax = 1, cmap = plt.cm.gray)
            else:
                im.set_data(self.state)
            i += 1
            self.calculate.applyRules()
            plt.pause(0.05)
            yield self