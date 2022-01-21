import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import W2

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu **2 - m_mu **2)

Q2_range_min = 0.143
Q2_range_max = 0.99
cordinate_1 = np.linspace(Q2_range_min, Q2_range_max, 1000)

X_2 = cordinate_1
Y_02 = np.sqrt(W2.W2(X_2, 0.2))
Y_025 = np.sqrt(W2.W2(X_2, 0.25))
Y_03 = np.sqrt(W2.W2(X_2, 0.3))
Y_033 = np.sqrt(W2.W2(X_2, 0.33))


fig = plt.figure()
plt.plot(X_2, Y_02, label="y = 0.2")
plt.plot(X_2, Y_025, label = "y = 0.25" )
plt.plot(X_2, Y_03, label="y = 0.3")
plt.plot(X_2, Y_033, label="y = 0.33")
plt.hlines(1.08, 0, 1, label = "W = 1.08 GeV")

plt.ylim(1.0, 1.3)

plt.legend()
plt.xlabel('Q^2 [Gev^2]', fontsize=14)
plt.ylabel("W [GeV]")
plt.title('W fixed y')
plt.grid()

fig.savefig("./graph/W2_fixed_y.png")