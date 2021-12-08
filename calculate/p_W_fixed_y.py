import numpy as np
import math
import matplotlib.pyplot as plt
import W_cos_Phi
import W2

#GeV
E_mu = 1.5
m_N = 0.94
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

def p_W(Q2, y):
    p_W = np.sqrt(p_mu **2 - 2 * p_mu * W_cos_Phi.p_prime(y) * W_cos_Phi.cos_theta(Q2 , y) + W_cos_Phi.p_prime(y))
    return p_W

x = np.arange(0.001, 0.99, 0.001)

X_2 = x
Y_c_1 = p_W(X_2, 0.1)
Y_c_2 = p_W(X_2, 0.2)
Y_c_3 = p_W(X_2, 0.3)
Y_c_4 = p_W(X_2, 0.4)
Y_c_5 = p_W(X_2, 0.5)
Y_c_6 = p_W(X_2, 0.6)
Y_c_7 = p_W(X_2, 0.7)
Y_c_8 = p_W(X_2, 0.8)
Y_c_9 = p_W(X_2, 0.9)
plt.plot(X_2, Y_c_1, label="y = 0.1")
plt.plot(X_2, Y_c_2, label="y = 0.2")
plt.plot(X_2, Y_c_3, label="y = 0.3")
plt.plot(X_2, Y_c_4, label="y = 0.4")
plt.plot(X_2, Y_c_5, label="y = 0.5")
plt.plot(X_2, Y_c_6, label="y = 0.6")
plt.plot(X_2, Y_c_7, label="y = 0.7")
plt.plot(X_2, Y_c_8, label="y = 0.8")
plt.plot(X_2, Y_c_9, label="y = 0.9")
plt.legend()
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.title('p_W fixed y [GeV]')
plt.grid()
plt.show()
