import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import W_cos_Phi

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)
m_p = 0.94

cordinate_1 = np.arange(0.001, 0.99, 0.001)
cordinate_2 = np.arange(0.001, 0.99, 0.001)
X, Y = np.meshgrid(cordinate_1, cordinate_2)

X_2 = cordinate_1
Y_01 = W_cos_Phi.cos_Phi(X_2, 0.1)
Y_02 = W_cos_Phi.cos_Phi(X_2, 0.2)
Y_03 = W_cos_Phi.cos_Phi(X_2, 0.3)
Y_04 = W_cos_Phi.cos_Phi(X_2, 0.4)
Y_05 = W_cos_Phi.cos_Phi(X_2, 0.5)
Y_06 = W_cos_Phi.cos_Phi(X_2, 0.6)
Y_07 = W_cos_Phi.cos_Phi(X_2, 0.7)
Y_08 = W_cos_Phi.cos_Phi(X_2, 0.8)
Y_09 = W_cos_Phi.cos_Phi(X_2, 0.9)

plt.plot(X_2, Y_01, label="y = 0.1")
plt.plot(X_2, Y_02, label="y = 0.2")
plt.plot(X_2, Y_03, label="y = 0.3")
plt.plot(X_2, Y_04, label="y = 0.4")
plt.plot(X_2, Y_05, label="y = 0.5")
plt.plot(X_2, Y_06, label="y = 0.6")
plt.plot(X_2, Y_07, label="y = 0.7")
plt.plot(X_2, Y_08, label="y = 0.8")
#plt.plot(X_2, Y_09, label="y = 0.9")

plt.legend()
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel("cos(Phi)")
plt.title('cos(Phi) fixed y')
plt.grid()
plt.show()