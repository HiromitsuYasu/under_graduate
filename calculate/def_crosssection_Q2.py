import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import ALLM_num as ALLM 
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

E_mu = 1.5
m_N = 0.94
m_pi = 0.14
alpha = 1.0 / 137.0
GeV_cm = 3.88 * 10**(-26.0)

#parameter dN/dt
rho = 1.0
N_A = 6.0 * 10**23
A = 1.0
Pb = 20 * 20 * 10

cordinate_1 = np.arange(0.001, 0.99, 0.001)
cordinate_2 = np.arange(0.001, 0.99, 0.001)
X, Y = np.meshgrid(cordinate_1, cordinate_2)

def crosssection(Q2, y):
    Q2_min = (m_pi **2 * y **2) / (1 - y)
    E_mu_prime = E_mu * (1 - y)
    x = Q2 / (2 * m_N * (E_mu - E_mu_prime))
    first_group = alpha / (np.pi * y * Q2)
    secound_group = (1 - y) * (1 - (Q2_min / Q2)) +(y**2 / 2)
    third_group_1 = 4 * np.pi **2 * alpha / (Q2 * (1 - x))
    third_group_2 = (Q2 + 4 * m_N **2 * x **2) / Q2
    third_group = third_group_1 * third_group_2 * ALLM.allm_f2(x, Q2)
    crosssection = first_group * secound_group * third_group
    return crosssection

Z = crosssection(X,Y)

fig = plt.figure()
ax = Axes3D(fig)

c1, c2 ="blue", "green"
l1, l2 = "all", "non effective"

ax.plot_wireframe(np.log10(X), np.log10(Y), np.log10(Z), color=c1,label=l1)
ax.set_xlabel("log10(Q^2) [Gev^2]")
ax.set_ylabel("log10(y)")
ax.set_zlabel("log10(sigma_dif) [GeV^2]")
ax.set_title("before")
ax.grid()

cordinate1_wall = np.linspace(0.001, 1.0, 989)
cordinate2_wall = np.linspace(0.0519, 0.227, 989)

x_wall , y_wall = np.meshgrid(cordinate1_wall ,cordinate2_wall)        
Z_wall = crosssection(x_wall, y_wall)
ax.plot_wireframe(np.log10(x_wall), np.log10(y_wall), np.log10(Z_wall),color=c2, label=l2 )
ax.legend(loc=0)
ax.set_zlim(np.log10(10**(-5)) ,np.log10(10**4))
plt.show()

