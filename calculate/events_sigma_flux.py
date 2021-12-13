import numpy as np
import math
import matplotlib.pyplot as plt
import def_crosssection_Q2
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.cm as cm

rho = 1
N_A = 6.02 * 10**(23)
A =  1
GeV_cm = 3.88 * 10**(-26.0)
volume = 20 * 20 * 200

def dN_dt(Q2, y):
    dN_dt = rho * N_A * def_crosssection_Q2.crosssection(Q2, y) * GeV_cm * volume / A
    return dN_dt

x = np.arange(0.001, 0.99, 0.001)
y = np.arange(0.001, 0.99, 0.001)
X, Y = np.meshgrid(x, y)

Z = dN_dt(X, Y)

fig, ax = plt.subplots()
cont_cl = ax.contour(X, Y, np.log10(Z), 40, colors=['r', 'g', 'b'])
ax.clabel(cont_cl, inline=True, fontsize=8)
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('log10(dN/dt)')
plt.grid()
plt.show()