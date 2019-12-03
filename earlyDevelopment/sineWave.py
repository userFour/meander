# ------------------------------------------------------------------------------
# Draw Wave
#
#
# Author: MArkos Frazzer    Date: 2019-10-10
#
# ------------------------------------------------------------------------------
#
# Draw a sine wave
#
# ------------------------------------------------------------------------------
#
#
# ------------------------------------------------------------------------------
#

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Declare some variables
n = 2048;
t = np.linspace(0, 10, n)
angle = 2 * np.pi / 3
pts = np.zeros([2, n], dtype=float)

fig, ax = plt.subplots()

i = 0;
while i <= 2:
    pts[0, :] = t[:]
    pts[1, :] = np.sin(t[:] + (i * angle))

    ax.plot(pts[0, :], pts[1, :])
    
    i = i + 1

fig.suptitle('DESCRIPTIVE TITLE', fontsize=12, fontname='Courier New')
plt.xlabel('X AXIS', fontsize=12, fontname='Courier New')
plt.ylabel('Y AXIS', fontsize=12, fontname='Courier New')
ax.grid()

for tick in ax.get_xticklabels():
    tick.set_fontname("Courier New")
    tick.set_fontsize(8) 
for tick in ax.get_yticklabels():
    tick.set_fontname("Courier New")
    tick.set_fontsize(8) 

ax.set_xlim()
ax.set_ylim(-1, 1)

fig.patch.set_facecolor('xkcd:mint green')
ax.set_facecolor('xkcd:charcoal')

plt.show()

# ------------------------------------------------------------------------------