import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm

m_N = 0.94

y = np.linspace(0.001, 0.99, 1000)

def Q_min(y):
    a = (m_N * y)**2 / (1 - y)
    return a
Q2_min = Q_min(y)
plt.plot(y, Q2_min,label="f(y) = Q2_min")
#plt.plot(y, y,label= "f(y) = y")
plt.grid()
plt.xlabel('y', fontsize=14)
plt.xlim(0, 0.6)
plt.ylim(0,1)
#plt.title('Q^2_min [GeV^2]')
plt.legend()
plt.show() 