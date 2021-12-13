import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import W2

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

cordinate_1 = np.arange(0.001, 0.99, 0.001)
cordinate_2 = np.arange(0.001, 0.99, 0.001)
X, Y = np.meshgrid(cordinate_1, cordinate_2)

def cos_theta(Q2, y):
    c = np.cos((-Q2 -(2 * m_mu **2) + 2 * E_mu **2 * (1 - y)) / (2 * p_mu * np.sqrt( (E_mu **2 * (1-y)**2) - m_mu **2) ))
    return c

def p_prime(y):
    p = np.sqrt((E_mu **2 * (1-y)**2) - m_mu**2)
    return p

def cos_Phi(Q2, y):
    inner = y * E_mu**2 + Q2 / 2
    norm = np.sqrt((E_mu**2 - m_mu**2) * (y**2 * E_mu**2 + Q2))
    cos_Phi = inner / norm
    return cos_Phi

Z = cos_Phi(X, Y)
"""
fig, ax = plt.subplots()
cont_cl = ax.contour(X, Y, Z, 25, colors=['r', 'g', 'b'])
ax.clabel(cont_cl, inline=True, fontsize=8)
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('cos(Phi)')
plt.show()
"""
"""
fig = plt.figure()
ax = Axes3D(fig)

ax.plot_wireframe(X, Y, Z)
ax.set_xlabel("Q^2 [Gev^2]")
ax.set_ylabel("y")
ax.set_zlabel("cos(Phi)")
ax.set_zlim([0,10])
ax.grid()
plt.show()
"""