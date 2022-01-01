import numpy as np
import math
import matplotlib.pyplot as plt

y = np.linspace(0.105, 0.535, 1000)

def E_gamma(y):
    E_gamma = 1500 * y
    return E_gamma

plt.plot(y, E_gamma(y))
plt.xlabel("y")
plt.ylabel("E_gamma [MeV]")
#plt.xlim(0.52, 0.55)
#plt.ylim(0.8,1.1)
plt.grid()
plt.show()