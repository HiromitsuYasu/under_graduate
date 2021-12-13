import numpy as np
import math
import W_cos_Phi
import W2
from matplotlib import pyplot as plt

#GeV
E_mu = 1.5
m_N = 0.94
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

def p_W(Q2, y):
    p_W = np.sqrt(p_mu **2 - 2 * p_mu * W_cos_Phi.p_prime(y) * W_cos_Phi.cos_theta(Q2 , y) + W_cos_Phi.p_prime(y) **2)
    return p_W

def E_W(Q2, y):
    p_W = np.sqrt(p_mu **2 - 2 * p_mu * W_cos_Phi.p_prime(y) * W_cos_Phi.cos_theta(Q2 , y) + W_cos_Phi.p_prime(y) **2)
    E_W = np.sqrt(W2.W2(Q2, y) + p_W **2)
    return E_W

def beta(Q2, y):
    beta = p_W(Q2 , y) / E_W(Q2, y)
    return beta

x = np.arange(0.001, 0.99, 0.001)
y = np.arange(0.001, 0.99, 0.001)
X ,Y = np.meshgrid(x, y)

beta = beta(X, Y)
p_W = p_W(X, Y)
E_W = E_W(X, Y)


fig, ax = plt.subplots()
cont_cl = ax.contour(X, Y, E_W, 25, colors=['r', 'g', 'b'])
ax.clabel(cont_cl, inline=True, fontsize=8)
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('E_W')
plt.show()