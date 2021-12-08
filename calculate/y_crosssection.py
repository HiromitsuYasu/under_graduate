import matplotlib.pyplot as plt
import numpy as np
import ALLM
import math
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D

E_mu = 1.5
m_N = 0.94
m_pi = 0.14
a = 1.0 / 137.0
GeV_cm = 3.88 * 10**(-26.0)

#parameter dN/dt
rho = 1.0
N_A = 6.0 * 10**23
A = 1.0
Pb = 20 * 20 * 10

Q2_crosssection = [[]]
y_crosssection = [[]]
y_Q2_crosssection =[[]]
#j = Q2
j = 0.01
#k = y
k = 0.01
while j < 1.0:
    while k < 1.0:
        W = m_N **2 + 4 * m_N * E_mu * k - j
        E_gamma = (W **2 - m_N **2 + j) / (4 * m_N)
        Y = E_gamma / E_mu
        Q2_min = m_pi **2 * Y**2 / (1 - Y)
        x = j / (2 * m_N * E_gamma)
        
        if(Q2_min < j):
            #integrate
            #define sigma
            sigma_µN = lambda Q2, y: ( (4 * math.pi * a **2) / (y * Q2 **6 * (1 - x) ) ) * (Q2 **2 +4 * m_N **2 * x **2) * ((1 - y) * (1 - Q2_min / Q2) + y **2 / 2) * ALLM(x, j)
            
            val, err= integrate.dblquad(sigma_µN, j, j + 0.01, lambda y: k, lambda y: k + 0.01)
            print("oooooookkkkkkkkk")
            sigma = val * GeV_cm

            y_crosssection.append(k, sigma)
            Q2_crosssection.append(j, sigma)

            y_Q2_crosssection.append(k, j, sigma)
            #print(val)
        k += 0.01
    
    j += 0.01

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_wireframe(y_Q2_crosssection[0], y_Q2_crosssection[1],y_Q2_crosssection[2])
ax.xlabel('y')
ax.ylabel('Q^2 [GeV^2]')
ax.zlabel('sigma_µN [cm^2]')
ax.savefig('Q^2_dNdt.png', bbox_inches="tight", pad_inches=0.05)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

Q2 = y = np.arange(0.0001, 1.0, 1000)
X, Y = np.meshgrid(Q2, y)

sigma_µN = lambda Q2, y: ( (4 * math.pi * a **2) / (y * Q2 **6 * (1 - x) ) ) * (Q2 **2 +4 * m_N **2 * x **2) * ((1 - y) * (1 - Q2_min / Q2) + y **2 / 2) * ALLM.allm_f2(x, j)
            

z = np.exp(-(X**2 + Y**2))

ax.plot_wireframe(X,Y,z)
plt.show()

