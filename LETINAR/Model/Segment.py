import numpy as np

# this is parent class for all segments
class Segment:
    def __init__(self, origin, axis, x1, x2):
        self.origin = origin
        self.axis = axis/np.linalg.norm(axis)
        self.rot = np.array([[self.axis[0], self.axis[1]], [-self.axis[1], self.axis[0]]])
        self.x1 = x1
        self.x2 = x2
    
    def set_params(self, *args):
        # varargin is a list of parameters
        pass
    
    def y(self, x):
        # returns y value for given x
        pass
    
    def dy(self, x):
        # returns derivative of y for given x
        pass
    
    def tangent(self, x):
        # returns tangent vector for given x
        slope = self.dy(x)
        return np.array([1, slope])/np.linalg.norm(np.array([1, slope]))
    
    def get_pos(self, n, type = 'ref'):
        # returns position
        x = np.linspace(self.x1, self.x2, n)
        if type == 'ref':
            return self.origin.reshape((2,1)) + np.matmul(self.rot.T, np.array([x, self.y(x)]))
        else:
            return np.array([x, self.y(x)])