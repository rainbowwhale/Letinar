import numpy as np
from Model.Segment import Segment

class Hyperbola(Segment):
    # Hyperbola class
    def set_params(self, *args):
        if len(args) != 3:
            raise ValueError("Expected 3 arguments for a, b, and c.")
        self.a = args[0]**2
        self.b = (args[0]**2) / (args[1]**2)
        self.c = args[2]
    
    def y(self, x):
        return self.c * (np.sqrt(self.a + self.b * x**2) - np.sqrt(self.a))
    
    def dy(self, x):
        return self.c * self.b * x / np.sqrt(self.a + self.b * x**2)