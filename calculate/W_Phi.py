import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import W_cos_Phi

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

cordinate_1 = np.arange(0.001, 0.99, 0.001)
cordinate_2 = np.arange(0.001, 0.99, 0.001)
X, Y = np.meshgrid(cordinate_1, cordinate_2)

def Phi(Q2,y): 
    Z = np.arccos(W_cos_Phi.cos_Phi(Q2,y))
    return Z

Z = Phi(X,Y)
"""
fig, ax = plt.subplots()
cont_cl = ax.contour(X, Y, Z, 25, colors=['r', 'g', 'b'])
ax.clabel(cont_cl, inline=True, fontsize=8)
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('Phi')
plt.show()
"""