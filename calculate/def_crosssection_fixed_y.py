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

X_2 = cordinate_1
Y_01 = crosssection(X_2, 0.1)
Y_02 = crosssection(X_2, 0.2)
Y_03 = crosssection(X_2, 0.3)
Y_04 = crosssection(X_2, 0.4)
Y_05 = crosssection(X_2, 0.5)
Y_06 = crosssection(X_2, 0.6)
Y_07 = crosssection(X_2, 0.7)
Y_08 = crosssection(X_2, 0.8)
Y_09 = crosssection(X_2, 0.9)

plt.plot(X_2, np.log10(Y_01), label="y = 0.1")
plt.plot(X_2, np.log10(Y_02), label="y = 0.2")
plt.plot(X_2, np.log10(Y_03), label="y = 0.3")
plt.plot(X_2, np.log10(Y_04), label="y = 0.4")
plt.plot(X_2, np.log10(Y_05), label="y = 0.5")
plt.plot(X_2, np.log10(Y_06), label="y = 0.6")
plt.plot(X_2, np.log10(Y_07), label="y = 0.7")
plt.plot(X_2, np.log10(Y_08), label="y = 0.8")
plt.plot(X_2, np.log10(Y_09), label="y = 0.9")

plt.legend()
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel(' log10 (dsigma / dQ^2 dy ) [ 1 / GeV^4]' )
plt.title("flux")
plt.ylim(np.log10(10 **(-5)), np.log10(10 **2))
plt.grid()
plt.show()