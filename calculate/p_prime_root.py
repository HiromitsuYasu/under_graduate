import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
#import ALLM_num as ALLM
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

#p' in root
def pp(y):
    p = (E_mu **2 * (1-y)**2) - m_mu**2
    return p
y_prrrrrr = np.linspace(0.001 , 0.99, 1000)
a = pp(y_prrrrrr)
plt.plot(y_prrrrrr, a)
plt.grid()
plt.xlabel('y', fontsize=14)
plt.title('p_prime in root')
plt.show()