import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import ALLM_num as ALLM 
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#GeV
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

def crosssection(Q2,y):
    E_mu_prime = E_mu * (1 - y)
    x = Q2 / (2 * m_N * (E_mu - E_mu_prime) )
    F1 = ALLM.allm_f2(x, Q2) / (2 * x)
    first_term = (8 * np.pi * alpha**2 * m_N * E_mu) / (Q2 **2)
    secound_term_1 = (1 + (1 - y)**2) / 2
    secound_term_2 = 2 * x * F1
    secound_term_3 = (1 - y) * (ALLM.allm_f2(x , Q2) - 2 * x * F1)
    secound_term_4 = (m_N * x * y * ALLM.allm_f2(x, Q2)) / (2 * E_mu)
    secound_term = (secound_term_1 * secound_term_2) + secound_term_3 - secound_term_4
    third_term = 2 * m_N * (E_mu - E_mu_prime)
    crosssection = first_term * secound_term / third_term
    return crosssection

Z = crosssection(X,Y)
"""
fig = plt.figure()
ax = Axes3D(fig)

c1, c2 ="blue", "green"
l1, l2 = "all", "non effective"

ax.plot_wireframe(np.log10(X), np.log10(Y), np.log10(Z), color=c1,label=l1)
ax.set_xlabel("log10(Q^2) [Gev^2]")
ax.set_ylabel("log10(y)")
ax.set_zlabel("log10(dsigma / dQ^2 dy) [ / GeV^4]")
ax.set_title("sturucture")
ax.grid()

cordinate1_wall = np.linspace(0.001, 1.0, 989)
cordinate2_wall = np.linspace(0.0519, 0.227, 989)

x_wall , y_wall = np.meshgrid(cordinate1_wall ,cordinate2_wall)        
Z_wall = crosssection(x_wall, y_wall)
ax.plot_wireframe(np.log10(x_wall), np.log10(y_wall), np.log10(Z_wall),color=c2, label=l2 )
ax.legend(loc=0)
ax.set_zlim(np.log10(10**(-5)) ,np.log10(10**4))
plt.show()
"""