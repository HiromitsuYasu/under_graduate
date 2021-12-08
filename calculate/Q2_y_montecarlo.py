import ALLM
import math
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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

yokojiku =[]
tatejiku =[]
zjiku = []

#j = Q2
j = 0.001
#k = y
k = 0.001
while j < 1.0:
    while k < 1.0:
        W = m_N **2 + 4 * m_N * E_mu * k - j
        E_gamma = (W **2 - m_N **2 + j) / (4 * m_N)
        Y = E_gamma / E_mu
        Q2_min = m_pi **2 * Y**2 / (1 - Y)
        x = j / (2 * m_N * E_gamma)
        
        if(Q2_min < j and Q2_min > 0.0):
            #integrate
            #define sigma
            sigma_µN = lambda Q2, y: ( (4 * math.pi * a **2) / (y * Q2 **6 * (1 - x) ) ) * (Q2 **2 +4 * m_N **2 * x **2) * ((1 - y) * (1 - Q2_min / Q2) + y **2 / 2) * ALLM.allm_f2(x, j)
            val, err= integrate.dblquad(sigma_µN, Q2_min, j , lambda y: k, lambda y: k + 0.1)
            sigma = val * GeV_cm
            yokojiku.append(k)
            tatejiku.append(j)
            zjiku.append(sigma)
            #print(k)
            #print(j)
            #print(sigma)
        k += 0.1
    
    j += 0.1

yokojiku, tatejiku = np.mgrid[0.001:1.0:0.1, 0.001:1.0:0.1]

fig, ax = plt.subplots()
im = ax.pcolormesh(yokojiku, tatejiku, sigma, cmap='inferno',vmin=10**-32,vmax=10**-28)
ax.set_xlabel("y")
ax.set_ylabel("Q^2")
cbar = fig.colorbar(im)
cbar.set_label("sigma [cm^2]")
plt.show()

#ax.savefig('Q^2_dNdt.png', bbox_inches="tight", pad_inches=0.05)
plt.show()
print("ok")
np.savetxt("2Dhist-array.txt", H[0], fmt = "%s")
print("unti")
