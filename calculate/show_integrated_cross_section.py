import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import ALLM_num as ALLM
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import itertools
import matplotlib.animation as animation

E_mu = 1.5
m_N = 0.94
m_pi = 0.14
a = 1.0 / 137.0
GeV_cm = 3.88 * 10**(-26.0)

#parameter dN/dt
rho = 1.0
N_A = 6.0 * 10**23
A = 1.0
Pb = 20 * 20 * 10

def f(Q2,y):
    W = (m_N **2 + 4 * m_N * E_mu * y - Q2)**(-1/2)
    E_gamma = (W **2 - m_N **2 + Q2) / (4 * m_N)
    Q2_min = m_pi **2 * y**2 / (1 - y)
    x = Q2 / (2 * m_N * E_gamma)
    sigma_µN =  ( (4 * math.pi * a **2) / (y * Q2 **6 * (1 - x) ) ) * (Q2 **2 + 4 * m_N **2 * x **2) * ((1 - y) * (1 - Q2_min / Q2) + y **2 / 2) * ALLM.allm_f2(x, Q2)
    return sigma_µN

N = 10**5
x_mc_range = 1
y_mc_range = 1
z_mc_range = 10**(-24)
x = x_mc_range * np.random.rand(N)
y = y_mc_range * np.random.rand(N)
z = z_mc_range * np.random.rand(N)


left_grid = 0.001
right_grid = 1.0
division_number = 100
delta_gird = (right_grid - left_grid) / division_number
grid_x = np.linspace(left_grid, right_grid, division_number)
grid_y = np.linspace(left_grid, right_grid, division_number)

result =[]

flag_z = (0 < z) * (z < y)
for x_i, y_i in itertools.product(grid_x, grid_y):
    flag_x = (x_i < x) * (x < x_i + delta_gird) 
    flag_y = (y_i < y) * (y < y_i + delta_gird) 
    n_point = np.sum(flag_x * flag_y * flag_z)
    vol = (x_mc_range * y_mc_range * z_mc_range) * (n_point / N)
    result.append([x_i, y_i, vol])
"""
result = np.array(result).T
fig1 = plt.figure()
#ax1 = Axes3D(fig1)
ax1 = fig1.add_subplot(111, projection='3d')

ax1.set_xlabel("log_10(Q^2_initial)")
ax1.set_ylabel("log_10(y_initial)")
ax1.set_zlabel("log_10(sigma)")

x_mesh, y_mesh = np.meshgrid(grid_x, grid_y)
z_reshape = result[2].reshape([division_number, division_number])
#ax1.plot(result[0], result[1], np.log(result[2] * GeV_cm) ,marker = 'o', linestyle ='None')
ax1.plot_surface(np.log10(x_mesh), np.log10(y_mesh), np.log10(z_reshape * GeV_cm), cmap='bwr', linewidth =0)
#fig1.colorbar(surf)
fig = plt.figure()
ani = animation.ArtistAnimation(fig, ax, interval =100 )
plt.show()
"""