import numpy as np
from matplotlib import pyplot as plt

class grid:
    # Constructor method
    def __init__(self, region, Nx):
        self.region = region
        self.Nx = Nx
        self.xlim = region[0], region[1]
        self.ylim = region[2], region[3]

        x, dx = np.linspace(self.xlim[0], self.xlim[1], Nx, retstep=True)
        self.dx = dx*2

        y = np.arange(self.ylim[0], self.ylim[1], self.dx*np.sqrt(3)/6)

        X, Y = np.meshgrid(x, y)
        X[1::2, :] += self.dx/2
        #Y[1::2, :] += dy

        X = X.flatten()
        Y = Y.flatten()

        self.X = X[::2]
        self.Y = Y[::2]

        theta = np.linspace(0, 360, 7)
        self.hexagons = []
        f = 1/3

        for x,y in zip(self.X, self.Y):
            hexagon = x + f * self.dx * np.cos(np.deg2rad(theta)), y + f * self.dx * np.sin(np.deg2rad(theta))
            self.hexagons.append(hexagon)
        
        self.N = len(self.hexagons)
        
    def get_ihexagon(self, i):
        x, y = self.hexagons[i]
        return x,y

    def plot_grid(self, ax, **kwargs):
        ax.plot(self.X, self.Y, **kwargs)

    def plot_hexagons(self):
        for x,y in self.hexagons:
            plt.plot(x, y, 'r-')

if __name__ == '__main__':
    region = [0, 100, 0, 100]
    Nx = 40

    g = grid(region, Nx)

    #plt.plot(g.X, g.Y, 'ro')
    g.plot_hexagons()
    plt.show()
    pass





