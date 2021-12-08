import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
#import ALLM_num as ALLM
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

#[GeV]
E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)
m_N = 0.94

x_w = np.arange(0.001, 0.99, 0.001)
y_w = np.arange(0.001, 0.99, 0.001)

def W2(Q2,y):
    W2 = m_N **2 + 2 * m_N * (E_mu - E_mu * (1 - y) ) - Q2
    return W2

X, Y = np.meshgrid(x_w, y_w)
Z = W2(X,Y)
"""
fig, ax = plt.subplots()
cont_cl = ax.contour(X, Y, Z, 40, colors=['r', 'g', 'b'])
ax.clabel(cont_cl, inline=True, fontsize=8)
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('W^2 [GeV^2]')
plt.grid()
plt.show()
"""

"""
fig = plt.figure()
ax = Axes3D(fig)
c1, c2 ="blue", "green"
l1, l2 = "all", "non effective"
ax.plot_wireframe(X, Y,Z, color=c1)
ax.set_xlabel("Q^2 [GeV^2]")
ax.set_ylabel("y")
ax.set_zlabel("W^2 [GeV^2]")
ax.grid()
ax.legend(loc=0)
plt.show()
"""