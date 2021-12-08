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

def theta(Q2, y):
    Y = 1 - y
    a = np.arccos((-Q2 - 2 * m_mu **2 + 2 * E_mu **2 * Y) / (2 * p_mu * np.sqrt( (E_mu **2 * Y**2) - m_mu **2) ) )
    return a

cordinate_1 = np.arange(0.001, 0.99, 0.001)
"""
X_1 = cordinate_1
Y_1 = theta(cordinate_1, 0.1)
Y_2 = theta(cordinate_1, 0.2)
Y_3 = theta(cordinate_1, 0.3)
Y_4 = theta(cordinate_1, 0.4)
Y_5 = theta(cordinate_1, 0.5)
Y_6 = theta(cordinate_1, 0.6)
Y_7 = theta(cordinate_1, 0.7)
Y_8 = theta(cordinate_1, 0.8)
Y_9 = theta(cordinate_1, 0.9)
plt.plot(X_1, Y_1, label="y = 0.1")
plt.plot(X_1, Y_2, label="y = 0.2")
plt.plot(X_1, Y_3, label="y = 0.3")
plt.plot(X_1, Y_4, label="y = 0.4")
plt.plot(X_1, Y_5, label="y = 0.5")
plt.plot(X_1, Y_6, label="y = 0.6")
plt.plot(X_1, Y_7, label="y = 0.7")
plt.plot(X_1, Y_8, label="y = 0.8")
plt.plot(X_1, Y_9, label="y = 0.9")
plt.legend()
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.title('theta fixed y')
plt.show()
"""