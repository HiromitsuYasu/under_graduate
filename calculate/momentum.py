import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import ALLM_num as ALLM
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from numpy import linalg as LA

#[GeV]
E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

def theta(Q2, y):
    Y = 1 - y
    a = np.arccos((Q2 + 2 * m_mu **2 - E_mu **2 * Y) / (p_mu * np.sqrt( (E_mu **2 * Y) - m_mu **2) ) )
    return a


cordinate_1 = np.arange(0.001, 0.1, 0.01)
cordinate_2 = np.arange(0.001, 0.1, 0.01)
X, Y = np.meshgrid(cordinate_1, cordinate_2)
Z = theta(X, Y)

cont = plt.contour(X, Y, Z)
cont = plt.contour(np.log10(X), np.log10(Y),Z,colors=['r', 'g', 'b'])
cont.clabel(fmt='%1.1f', fontsize=14)
plt.xlabel('log10(Q^2) [Gev^2]', fontsize=14)
plt.ylabel('log10(y)', fontsize=14)
plt.show()