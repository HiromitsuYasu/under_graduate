import numpy as np
from matplotlib import pyplot as plt

alpha = 1 / 137
m_p = 0.9382
mb_cm = 10**(-27)
GeV_cm = 3.88 * 10**(-26.0)

Q2_range_min = 0.001
Q2_range_max = 0.12

def sigma_used_article(Q2, y, sigma_tot):
    Q2_min = (m_p **2 * y ** 2 ) / (1 - y) 
    flux = (alpha / (y * np.pi)) * (1 / Q2) * ( (1 - y) * (1 - (Q2_min / Q2) )  + (y **2 / 2))
    sigma = flux * sigma_tot
    return sigma

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

Q2 = np.linspace(0.001, 0.12, 1000)

plt.plot(Q2, sigma_used_article(Q2, 0.2, 0.1 * mb_cm / GeV_cm ), label = "y = 0.2")
plt.plot(Q2, sigma_used_article(Q2, 0.3, 0.4 * mb_cm / GeV_cm ), label = "y = 0.3")
plt.plot(Q2, sigma_used_article(Q2, 0.4, 0.3 * mb_cm / GeV_cm ), label = "y = 0.4")
plt.plot(Q2, sigma_used_article(Q2, 0.5, 0.2 * mb_cm / GeV_cm ), label = "y = 0.5")
plt.legend()
ax.set_xlabel("Q^2 [Gev^2]")
ax.set_ylabel("dsigma / dQ^2 [1 / GeV^2]")
#ax.set_yscale("log")
plt.grid()
fig.savefig("./graph/integrate_flux_used_artile_fixed_y.png")

#plt.show()