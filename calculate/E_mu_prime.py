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

def E_mu_prime(y):
    e = E_mu * (1 - y)
    return e

x_3 = np.arange(0.001, 1.0 ,0.001)
y_E_prime = E_mu_prime(x_3)
plt.xlabel('y')
plt.title('E_mu_prime')
plt.plot(x_3, y_E_prime)
plt.show()