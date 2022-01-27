from __future__ import division
import numpy as np
import ALLM_num
from matplotlib import pyplot as plt
import function_for_sigma

alpha = 1.0 / 137.0
M = 0.938
Q2 = 0.11
GeV_cm = 3.894 * 10**(-28.0)
cm_mb = 10**27
E_mu = 1.5

division = 100

E_gamma_range_min = 0.2
E_gamma_range_max = 1.0
E_gamma = np.linspace(E_gamma_range_min, E_gamma_range_max, division)

fig = plt.figure()
plt.plot(E_gamma, function_for_sigma.calculate_sigma_tot(E_gamma / E_mu, Q2) * GeV_cm * cm_mb )
plt.xlabel("E_gamma[GeV]")
plt.ylabel("sigma_tot [mb]")
plt.xscale("log")
plt.yscale("log")
plt.grid(which="major")
plt.grid(which="minor")
fig.savefig("./graph/sigma_tot.png")