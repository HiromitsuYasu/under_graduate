import numpy as np
import math
import matplotlib.pyplot as plt

def Q2_min(y):
    Q2_min = 0.94**2 * y / (1 - y)
    return Q2_min

y = np.linspace(0.001, 0.99 , 1000)

#set upper limit y for Q2_min < 1.0 because Q2=[0.01, 0.99]
plt.plot(y, Q2_min(y))
plt.xlabel("y")
plt.ylabel("Q2_min(y)")
plt.xlim(0.52, 0.55)
plt.ylim(0.8,1.1)
plt.grid()
plt.show()