class Calculate(object):
    def __init__(self, table):
        self.state = table.state
    def countNeighbors(self):   #Returns array of number of cells next to each cell
        state = self.state
        n = (state[0:-2,0:-2] + state[0:-2,1:-1] + state[0:-2,2:] +
            state[1:-1,0:-2] + state[1:-1,2:] + state[2:,0:-2] +
            state[2:,1:-1] + state[2:,2:])
        return n
    def applyRules(self):
        n = self.countNeighbors()   #Counts cells near each cell
        state = self.state
        birth = (n == 3) & (state[1:-1,1:-1] == 0)  #Cell born with 3 nearby and it is dead
        survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1)   #Cell survives if 2 or 3 neighbors and is alive
        state[...] = 0  #Clears entire board
        state[1:-1,1:-1][birth | survive] = 1   #Adds back surviving and new cells
        return state    #Returns binary "board" to be displayed