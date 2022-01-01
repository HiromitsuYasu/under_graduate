import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm

m_W = 0.94 + 0.14
def W(y):
    W = np.sqrt(0.94 **2 + 2 * 0.94 * 1.5 * y - 0.01)
    return W

y = np.linspace(0.001, 0.99 , 1000)

#set lower limit of y for W limit
plt.plot(y, W(y))
plt.xlabel("y")
plt.ylabel("W")
plt.xlim(0.1,0.12)
plt.ylim(1.0,1.1)
plt.grid()
plt.show()