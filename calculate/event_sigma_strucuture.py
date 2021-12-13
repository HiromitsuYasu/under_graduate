import numpy as np
import math
import matplotlib.pyplot as plt
import sigma_used_book 
import theta_y_fixed 
import ROOT as r
from copy import copy
r.gROOT.SetBatch()
from mpl_toolkits.mplot3d.axes3d import Axes3D

rho = 1
N_A = 6.02 * 10**(23)
A =  1
GeV_cm = 3.894 * 10**(-28.0)
volume = 20 * 20 * 20

def dN_dt(sigma):
    dN_dt = rho * N_A * sigma * volume / A
    return dN_dt

def is_inner(Q2, y, z):
    
    return  z < sigma_used_book.crosssection(Q2, y) 
 
inner_points_cnt = 0
all_points_cnt = 0
 
Q2_rand = 0.001 + (0.12 - 0.001) * np.random.rand(10**5)
y_rand = 0.125 + (0.54 - 0.125) * np.random.rand(10**5)
z_rand = 10 **(4 * np.random.rand(10**5) - 3 )
for x, y, z in zip(Q2_rand, y_rand, z_rand):
    all_points_cnt += 1
    if is_inner(x, y, z):
        inner_points_cnt += 1

sigma = (inner_points_cnt  / all_points_cnt) * ( (0.12 - 0.001) * (0.54 - 0.125) * 10**(4) ) * GeV_cm

dN_dt = dN_dt(sigma)
print("sigma" ,sigma ,"cm^2")
print("-dN / dt" ,dN_dt)