import numpy as np
import math
import matplotlib.pyplot as plt
import def_crosssection_Q2 
import theta_y_fixed 
import ROOT as r
from copy import copy
r.gROOT.SetBatch()
from mpl_toolkits.mplot3d.axes3d import Axes3D

def is_inner(Q2, y, z):
    
    return  z < def_crosssection_Q2.crosssection(Q2, y) 
 
inner_points_cnt = 0
all_points_cnt = 0
 
Q2_rand = 0.001 + (0.12 - 0.001) * np.random.rand(10**5)
y_rand = 0.125 + (0.535 - 0.125) * np.random.rand(10**5)
z_rand = 10 **(4 * np.random.rand(10**5) - 3 )
for x, y, z in zip(Q2_rand, y_rand, z_rand):
    all_points_cnt += 1
    if is_inner(x, y, z):
        inner_points_cnt += 1
 
sigma = (inner_points_cnt / all_points_cnt) * ( (0.12 - 0.001) * (0.535 - 0.125) * 10**(4) )
print(sigma)


#以下plot
# ランダムに配置した点のプロット
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(Q2_rand, y_rand, np.log10(z_rand))

cordinate_1 = np.linspace(0.001, 0.125, 1000)
cordinate_2 = np.linspace(0.12, 0.535, 1000)
X, Y = np.meshgrid(cordinate_1, cordinate_2)

cz = def_crosssection_Q2.crosssection(X, Y) 
ax.plot_wireframe(X, Y, np.log10(cz) , color ="red")
ax.set_xlabel("Q^2 [Gev^2]")
ax.set_ylabel("y")
ax.set_zlabel("dsigma / dQ^2 dy[1 / GeV^4]")
ax.grid()

plt.show()
