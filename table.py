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
        plt.title("It's a thing!")
        plt.plot(self.state)
        plt.ylabel("Numbers!")
        plt.show()