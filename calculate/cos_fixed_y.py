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

cordinate_1 = np.arange(0.001, 0.99, 0.001)

def cos(Q2, y):
    Y = 1 - y
    c = (2 * (Y * E_mu**2) - Q2 - (2 * m_mu **2) ) / (2 * p_mu * np.sqrt( (E_mu * Y)**2 - m_mu**2) )
    return c

X_2 = cordinate_1
Y_c_1 = cos(cordinate_1, 0.1)
Y_c_2 = cos(cordinate_1, 0.2)
Y_c_3 = cos(cordinate_1, 0.3)
Y_c_4 = cos(cordinate_1, 0.4)
Y_c_5 = cos(cordinate_1, 0.5)
Y_c_6 = cos(cordinate_1, 0.6)
Y_c_7 = cos(cordinate_1, 0.7)
Y_c_8 = cos(cordinate_1, 0.8)
Y_c_9 = cos(cordinate_1, 0.9)
plt.plot(X_2, Y_c_1, label="y = 0.1")
plt.plot(X_2, Y_c_2, label="y = 0.2")
plt.plot(X_2, Y_c_3, label="y = 0.3")
plt.plot(X_2, Y_c_4, label="y = 0.4")
plt.plot(X_2, Y_c_5, label="y = 0.5")
plt.plot(X_2, Y_c_6, label="y = 0.6")
plt.plot(X_2, Y_c_7, label="y = 0.7")
plt.plot(X_2, Y_c_8, label="y = 0.8")
#plt.plot(X_2, Y_c_9, label="y = 0.9")
plt.legend()
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.title('cos fixed y')
plt.show()
