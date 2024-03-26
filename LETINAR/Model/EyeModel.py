import numpy as np


class EyeModel:
    # EyeModel class
    def __init__(self, segments):
        self.segments = segments
    
    def set_params(self, *args):
        for i in range(len(self.segments)):
            self.segments[i].set_params(*args[i])
    
    def get_pos(self, n, type = 'ref'):
        pos = self.segments[0].get_pos(n, type)
        for i in range(1, len(self.segments)):
            pos = np.concatenate((pos, self.segments[i].get_pos(n, type)), axis = 1)
        return pos