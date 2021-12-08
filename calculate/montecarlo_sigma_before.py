import numpy as np
import math
import matplotlib.pyplot as plt
import def_crosssection_Q2 
import theta_y_fixed 

Q2_rand = 0.001 + (0.99 - 0.001) * np.random.rand(100000)
y_rand = 0.001 + (0.99 - 0.001) * np.random.rand(100000)
cross_section = def_crosssection_Q2.crosssection(y_rand, Q2_rand)
theta = theta_y_fixed.theta(y_rand, Q2_rand)

plt.hist(
    theta/np.pi,
    weights=cross_section,
    range=(0, 1),
    bins=30,
    )
plt.xlabel("theta [rad/pi]")
plt.ylabel("proportional to prob")
plt.title("before")
plt.show()