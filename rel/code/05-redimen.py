import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

def func( x, y ):
    return np.sin(x*12.0)*np.sin(y*20.0)

points = np.random.rand(1000, 2)
values = func(points[:,0], points[:,1])

grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')

plt.imshow(grid_z.T, extent=(0,1,0,1), origin='lower')
plt.scatter(points[:,0], points[:,1], c='k')

plt.show()