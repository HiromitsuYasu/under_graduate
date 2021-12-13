import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
#import ALLM_num as ALLM
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

def Q2(y,cos):
    Y = 1 - y
    p_prime = np.sqrt(E_mu **2 * Y - m_mu **2)
    Q = 2 *(E_mu **2 * Y - (m_mu**2 + p_mu * p_prime * cos) )
    return Q

cordinate_1 = np.linspace(0.001, 0.99, 1000)
a = np.linspace(-1, 1.0, 1000)
X , Y = np.meshgrid(cordinate_1, a)

#wireframe

fig = plt.figure()
ax = Axes3D(fig)
c1, c2 ="blue", "green"
l1, l2 = "all", "non effective"
Z = Q2(X,Y)
ax.plot_wireframe(X, Y,Z, color=c1)
ax.set_xlabel("y")
ax.set_ylabel("cos")
ax.set_zlabel("Q^2 [GeV^2]")
ax.grid()
ax.legend(loc=0)
plt.show()
"""
#counter map
Z = Q2(X,Y)
fig, ax = plt.subplots()
cont_cl = ax.contour(X, Y, Z, 40, colors=['r', 'g', 'b'])
ax.clabel(cont_cl, inline=True, fontsize=8)
plt.xlabel('y', fontsize=14)
plt.ylabel('cos', fontsize=14)
plt.title('Q^2 [GeV^2]')
plt.show()
"""