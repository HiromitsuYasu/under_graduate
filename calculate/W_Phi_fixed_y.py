import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import W_Phi

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

cordinate_1 = np.arange(0.001, 0.99, 0.001)

X_2 = cordinate_1
Y_01 = W_Phi.Phi(X_2, 0.1)
Y_02 = W_Phi.Phi(X_2, 0.2)
Y_03 = W_Phi.Phi(X_2, 0.3)
Y_04 = W_Phi.Phi(X_2, 0.4)
Y_05 = W_Phi.Phi(X_2, 0.5)
Y_06 = W_Phi.Phi(X_2, 0.6)
Y_07 = W_Phi.Phi(X_2, 0.7)
Y_08 = W_Phi.Phi(X_2, 0.8)
Y_09 = W_Phi.Phi(X_2, 0.9)

plt.plot(X_2, Y_01, label="y = 0.1")
plt.plot(X_2, Y_02, label="y = 0.2")
plt.plot(X_2, Y_03, label="y = 0.3")
plt.plot(X_2, Y_04, label="y = 0.4")
plt.plot(X_2, Y_05, label="y = 0.5")
plt.plot(X_2, Y_06, label="y = 0.6")
plt.plot(X_2, Y_07, label="y = 0.7")
plt.plot(X_2, Y_08, label="y = 0.8")
plt.plot(X_2, Y_09, label="y = 0.9")

plt.legend()
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.title('Phi fixed y')
plt.grid()
plt.show()
