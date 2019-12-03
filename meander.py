# ------------------------------------------------------------------------------
# Meander
#
#
# Author: MArkos Frazzer    Date: 2019-11-25
#
# ------------------------------------------------------------------------------
#
# Meander a path
#
# ------------------------------------------------------------------------------
#
#
# ------------------------------------------------------------------------------
#

import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

SIZE = 10
CUBE_DEF = np.array([[SIZE, 0, 0, 0], [0, SIZE, 0, 0], [0, 0, SIZE, 0]])
NUM_STEPS = 50
PT_START = np.array([[round(SIZE / 2)], [round(SIZE / 2)], [round(SIZE / 2)]])

def main():
    # Declare some stuff
    
    # Setup the figure
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    fig.patch.set_facecolor('xkcd:mint green')
    ax.set_facecolor('xkcd:charcoal')
    
    print(CUBE_DEF)

    pts = drawCube()

    ax.plot3D([pts[0, 0], pts[0, 3]], [pts[1, 0], pts[1, 3]], [pts[2, 0], pts[2, 3]], 'xkcd:pumpkin')
    ax.plot3D([pts[0, 0], pts[0, 4]], [pts[1, 0], pts[1, 4]], [pts[2, 0], pts[2, 4]], 'xkcd:pumpkin')
    ax.plot3D([pts[0, 0], pts[0, 6]], [pts[1, 0], pts[1, 6]], [pts[2, 0], pts[2, 6]], 'xkcd:pumpkin')
    
    ax.plot3D([pts[0, 1], pts[0, 3]], [pts[1, 1], pts[1, 3]], [pts[2, 1], pts[2, 3]], 'xkcd:pumpkin')
    ax.plot3D([pts[0, 1], pts[0, 5]], [pts[1, 1], pts[1, 5]], [pts[2, 1], pts[2, 5]], 'xkcd:pumpkin')
    ax.plot3D([pts[0, 1], pts[0, 6]], [pts[1, 1], pts[1, 6]], [pts[2, 1], pts[2, 6]], 'xkcd:pumpkin')
    
    ax.plot3D([pts[0, 2], pts[0, 3]], [pts[1, 2], pts[1, 3]], [pts[2, 2], pts[2, 3]], 'xkcd:pumpkin')
    ax.plot3D([pts[0, 2], pts[0, 4]], [pts[1, 2], pts[1, 4]], [pts[2, 2], pts[2, 4]], 'xkcd:pumpkin')
    ax.plot3D([pts[0, 2], pts[0, 5]], [pts[1, 2], pts[1, 5]], [pts[2, 2], pts[2, 5]], 'xkcd:pumpkin')
    
    ax.plot3D([pts[0, 7], pts[0, 4]], [pts[1, 7], pts[1, 4]], [pts[2, 7], pts[2, 4]], 'xkcd:pumpkin')
    ax.plot3D([pts[0, 7], pts[0, 5]], [pts[1, 7], pts[1, 5]], [pts[2, 7], pts[2, 5]], 'xkcd:pumpkin')
    ax.plot3D([pts[0, 7], pts[0, 6]], [pts[1, 7], pts[1, 6]], [pts[2, 7], pts[2, 6]], 'xkcd:pumpkin')
    
    pts = 0
    pts = meander(NUM_STEPS)
    
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in pts]))
    
    ax.plot3D(pts[0, :], pts[1, :], pts[2, :], 'xkcd:reddish')
     
    
    ax.set_xlim(0, SIZE)
    ax.set_ylim(0, SIZE)
    ax.set_zlim(0, SIZE)

    plt.show()
    
# ------------------------------------------------------------------------------
def drawCube():
    # Plot the colourCube
    
    vertices = np.zeros((3, 8), dtype=int)
    vectors = np.zeros((2, 12), dtype=int)
    
    vertices[:, 0] = CUBE_DEF[:, 0]
    vertices[:, 1] = CUBE_DEF[:, 1]
    vertices[:, 2] = CUBE_DEF[:, 2]
    vertices[:, 3] = CUBE_DEF[:, 3]
    vertices[:, 4] = CUBE_DEF[:, 0] + CUBE_DEF[:, 2]
    vertices[:, 5] = CUBE_DEF[:, 1] + CUBE_DEF[:, 2]
    vertices[:, 6] = CUBE_DEF[:, 0] + CUBE_DEF[:, 1]
    vertices[:, 7] = CUBE_DEF[:, 0] + CUBE_DEF[:, 1] + CUBE_DEF[:, 2]
    
    print(vertices)
    
    return vertices
    
# ------------------------------------------------------------------------------
def meander(steps):
    path = np.zeros((3, steps), dtype=int)
    path[:, 0] = PT_START[:, 0]
    
   
    for i in range(1, steps):
        
        xDice = random.randint(-1, 1)
        yDice = random.randint(-1, 1)
        zDice = random.randint(-1, 1)
        
        path[0, i] = path[0, i - 1] + xDice
        path[1, i] = path[1, i - 1] + yDice
        path[2, i] = path[2, i - 1] + zDice
    
    return path
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()