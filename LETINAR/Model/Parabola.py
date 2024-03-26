import numpy as np
from Model.Segment import Segment

class Parabola(Segment):
    # Parabola class
    def set_params(self, *args):
        if len(args) != 3:
            raise ValueError("Expected 3 arguments for a, b, and c.")
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
    
    def y(self, x):
        return self.a * x**2 + self.b * x + self.c
    
    def dy(self, x):
        return 2 * self.a * x + self.b
