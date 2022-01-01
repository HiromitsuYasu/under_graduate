import numpy as np
import math
import matplotlib.pyplot as plt

alpha = 1 / 137
m_p = 0.9382
mb_cm = 10**(-27)
GeV_cm = 3.88 * 10**(-26.0)

Q2_range_min = 0.001
Q2_range_max = 0.12

rho = 1
N_A = 6.02 * 10**(23)
A =  1
GeV_cm = 3.894 * 10**(-28.0)
volume = 20 * 20 * 20

def dN_dt(sigma):
    dN_dt = rho * N_A * sigma * volume / A
    return dN_dt


Q2_range_min = 0.001
Q2_range_max = 0.12

def sigma_used_article(Q2, y, sigma_tot):
    Q2_min = (m_p **2 * y ** 2 ) / (1 - y) 
    flux = (alpha / (y * np.pi)) * (1 / Q2) * ( (1 - y) * (1 - (Q2_min / Q2) )  + (y **2 / 2))
    sigma = flux * sigma_tot
    return sigma

def is_inner(Q2, z):
    
    return  z < sigma_used_article(Q2, 0.2, 0.4 * mb_cm) 
 
inner_points_cnt = 0
all_points_cnt = 0
 
Q2_rand = Q2_range_min + (Q2_range_max - Q2_range_min) * np.random.rand(10**5)
z_rand = 10 **(3 * np.random.rand(10**5) - 31 )
for x, y in zip(Q2_rand, z_rand):
    all_points_cnt += 1
    if is_inner(x, y):
        inner_points_cnt += 1

sigma = (inner_points_cnt  / all_points_cnt) *  (Q2_range_max - Q2_range_min) * 10 **3  * GeV_cm
Q2 = np.linspace(0.001, 0.12, 1000)
#y = np.linspace(0.105, 0.535, 1000)

cz = sigma_used_article(Q2, 0.2, 0.4 * 10**(-27))

dN_dt = dN_dt(sigma)
print("sigma", sigma ,"cm^2")
print("-dN / dt" ,dN_dt)