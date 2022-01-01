import numpy as np
from matplotlib import pyplot as plt

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu**2 - m_mu**2)

def Q2(y):
    Q2 = 2 * E_mu **2 * (1 - y) - 2 * m_mu**2 - 2 * p_mu * np.sqrt(E_mu**2 * (1 - y) - m_mu**2) * 0
    return Q2

y = np.linspace(0.105, 0.535, 1000)

plt.plot(y, Q2(y))
plt.xlabel("y")
plt.ylabel("Q^2")
plt.grid()
plt.show()