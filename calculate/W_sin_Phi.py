import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

cordinate_1 = np.arange(0.001, 0.99, 0.001)
cordinate_2 = np.arange(0.001, 0.99, 0.001)
X, Y = np.meshgrid(cordinate_1, cordinate_2)

theta = np.arccos((2 * E_mu **2 * (1-Y) - X - 2 * m_mu **2 ) / (2 * p_mu * np.sqrt( (E_mu **2 * (1-Y)**2 ) - m_mu **2) ) )

def p_prime(y):
    p = np.sqrt((E_mu **2 * (1-y)**2) - m_mu**2)
    return p

def sin(Q2, y):
    sin = np.sin((p_prime(y) * np.sin(theta) )/ np.sqrt(Q2))
    return sin

Z = sin(X, Y)

fig, ax = plt.subplots()
cont_cl = ax.contour(X, Y, Z, 25, colors=['r', 'g', 'b'])
ax.clabel(cont_cl, inline=True, fontsize=8)
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('sin(Phi)')
plt.show()