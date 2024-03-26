import numpy as np
from Model.Segment import Segment

class Circular(Segment):
    # Circular class
    def set_params(self, *args):
        if len(args) != 2:
            raise ValueError("Expected 2 arguments for r and s")
        self.r = args[0]
        self.s = args[1]
    
    def y(self, x):
        return self.s * (self.r - np.sqrt(self.r**2 - x**2))
    
    def dy(self, x):
        return self.s * x / np.sqrt(self.r**2 - x**2)