import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
from numpy.random import uniform
from copy import deepcopy

class grid:
    class hexagon:
        def __init__(self, x, y, id, value=None):
            self.x = x
            self.y = y
            self.value = value
            self.id = id
        
        def get_xy(self):
            return hexagon.x, hexagon.y
        
        def __repr__(self):
            return f"hexagon(x={self.x}, y={self.y}, id={self.id}, value={self.value})"
    # Constructor method
    def __init__(self, region, Nx):
        self.region = region
        self.xlim = region[0], region[1]
        self.ylim = region[2], region[3]

        if Nx % 2 == 1:
            Nx += 1
            Warning("Nx must be even. Nx was increased by 1")

        _x, _dx = np.linspace(self.xlim[0], self.xlim[1], Nx, retstep=True)
        self._dx = _dx*2

        _y = np.arange(self.ylim[0], self.ylim[1], self._dx*np.sqrt(3)/6)

        self.Nx = len(_x)
        self.Ny = len(_y)//2

        _X, _Y = np.meshgrid(_x, _y)
        _X[1::2, :] += self._dx/2
        #Y[1::2, :] += dy

        _X = _X.flatten()
        _Y = _Y.flatten()

        self._X = _X[::2]
        self._Y = _Y[::2]

        _theta = np.linspace(0, 360, 7)
        _f = 1/3
        self.hexagons = []

        for _id, (_x, _y) in enumerate(zip(self._X, self._Y)):
            _x_hex, _y_hex = _x + _f * self._dx * np.cos(np.deg2rad(_theta)), _y + _f * self._dx * np.sin(np.deg2rad(_theta))
            _hexagon = self.hexagon(_x_hex, _y_hex, _id, value=0)
            self.hexagons.append(_hexagon)
        
        self.N = len(self.hexagons)
    
    def copy(self):
        return deepcopy(self)

    def __len__(self):
        return self.N
        
    def get_ihexagon(self, i):
        x, y = self.hexagons[i]
        return x,y
    

    def plot_grid(self, ax, **kwargs):
        ax.plot(self.X, self.Y, **kwargs)

    def plot_hexagons(self, ids=False):
        for hexagon in self.hexagons:
            x, y = hexagon.x, hexagon.y
            plt.plot(x, y, 'r-')
            if ids:
                plt.text(np.mean(x), np.mean(y), f"{hexagon.id}", horizontalalignment='center', verticalalignment='center')
        return plt.gca()
    
    def find_hexagon(self, x, y):
        point = Point(x, y)
        for hexagon in self.hexagons:
            polygon = Polygon(list(zip(hexagon.x, hexagon.y)))
            if polygon.contains(point):
                return hexagon
        return None
    
    def find_hexagon_id(self, x, y):
        point = Point(x, y)
        for hexagon in self.hexagons:
            polygon = Polygon(list(zip(hexagon.x, hexagon.y)))
            if polygon.contains(point):
                return hexagon.id
        return None
    
    def __repr__(self):
        return f"grid(region={self.region}, Nx={self.Nx}, Ny = {self.Ny}, N = {self.N})"

if __name__ == '__main__':
    region = [0, 100, 0, 100]
    Nx = 10

    x_random = uniform(0, 100, 1)
    y_random = uniform(0, 100, 1)

    #x_random = 10
    #y_random = -5

    g = grid(region, Nx)
    hexagon = g.find_hexagon(x_random, y_random)
    print(g)

    #plt.plot(g.X, g.Y, 'ro')
    grid_plot = g.plot_hexagons(ids=True)
    grid_plot.plot(x_random, y_random, 'bo')
    grid_plot.plot(hexagon.x, hexagon.y,color='b', linewidth=2)
    id = g.find_hexagon_id(x_random, y_random)
    print(f"Point ({x_random}, {y_random}) is inside hexagon {id}")



    plt.show()
    pass





