import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def Q2_min(y):
    Q2_min = 0.94**2 * y / (1 - y)
    return Q2_min

Q2 = np.linspace(0.001, 0.99 , 1000)

# set limit Q2, for Q2 - Q2_min > 0
plt.plot(Q2, Q2 - Q2_min(Q2))
plt.xlabel("Q2")
plt.ylabel("Q2 - Q2_min(Q2)")
plt.xlim(0, 0.15)
plt.ylim(-0.001,0.001)
plt.grid()
plt.show()