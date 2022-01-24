import numpy as np
import ALLM_num
from matplotlib import pyplot as plt

alpha = 1.0 / 137.0
M = 0.938
Q2 = 0.11
GeV_cm = 3.894 * 10**(-28.0)
cm_mb = 10**27

def W(E_gamma):
    W = np.sqrt(M**2 + 2 * M * E_gamma - Q2)
    return W

def x(E_gamma):
    x = Q2 / (2 * E_gamma * M)
    return x

# return [mb]
def sigma_tot(E_gamma):
    first_term = (4.0 * alpha * np.pi**2) / (Q2 * (1.0 - x(E_gamma) ) )
    secound_term = (Q2**2 + 4 * M**2 * x(E_gamma)**2) / Q2
    third_term = ALLM_num.allm_f2(x(E_gamma), Q2)
    sigma_tot = first_term * secound_term * third_term * GeV_cm * cm_mb
    return sigma_tot

E_gamma_range_min = 0.2
E_gamma_range_max = 1.0
E_gamma = np.linspace(0.2, 1.0, 1000)

fig = plt.figure()
plt.plot(E_gamma, sigma_tot(E_gamma) )
plt.xlabel("E_gamma[MeV]")
plt.ylabel("sigma_tot [mb]")
plt.xscale("log")
plt.yscale("log")
plt.grid(which="major")
plt.grid(which="minor")
fig.savefig("./graph/sigma_tot.png")