import numpy as np

from calculate import Calculate

class Table(object):
    def __init__(self, size, seed = "Random"):
        if seed == 'Random':
            self.state = np.random.randint(2, size = size)
        self.calculate = Calculate(self)
        self.iteration = 0