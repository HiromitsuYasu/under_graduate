import numpy as np
import function_for_sigma

alpha = 1 / 137
m_p = 0.9382
mb_cm = 10**(-27)
GeV_cm = 3.88 * 10**(-28)

# GeV
E_mu = 1.5

Q2_range_min = 0.085
Q2_range_max = 0.643

E_gamma_range_min = 0.3
E_gamma_range_max = 0.5
division = 100

y_range_min = function_for_sigma.calculate_y_from_E_gamma(E_gamma_range_min)
y_range_max = function_for_sigma.calculate_y_from_E_gamma(E_gamma_range_max)
y = np.linspace(y_range_min, y_range_max, division)

# Q2 = [[Q^2_min(y_0) , ... , Q^2_max(y_0)], [Q^2_min(y_1), ..., Q^2_max(y_1)], ... ]
Q2 = np.linspace(function_for_sigma.calculate_Q2_min_from_y(y), function_for_sigma.calculate_Q2_max_from_y(y), division)

# y: 1 dimensional -> 2 dimensional
y_array = np.array([y] * division)

# d^2 sigma / dy dQ^2
d_sigma = function_for_sigma.calculate_sigma_flux(y_array, Q2) * GeV_cm

sigma_max = np.amax(d_sigma)
sigma_min = np.amin(d_sigma)
sigma_range  = np.log10(sigma_max) - np.log10(sigma_min)

# montecalro integration
def is_inner(y, Q2, z):
    
    return  z < function_for_sigma.calculate_sigma_flux(y, Q2)  * GeV_cm
 
inner_points_cnt = 0
all_points_cnt = 0

y_rand = y_range_min + (y_range_max - y_range_min) * np.random.rand(10**5)
Q2_rand = Q2_range_min + (Q2_range_max - Q2_range_min) * np.random.rand(10**5)
z_rand = 10 **(sigma_range * np.random.rand(10**5) - 30.18)
for x, y, z in zip(y_rand, Q2_rand, z_rand):
    all_points_cnt += 1
    if is_inner(x, y, z):
        inner_points_cnt += 1

sigma = (inner_points_cnt  / all_points_cnt) *  (Q2_range_max - Q2_range_min) * (y_range_max - y_range_min) * 10**sigma_range * GeV_cm

# dN / dt
rho = 1
N_A = 6.02 * 10**(23)
A =  1
GeV_cm = 3.894 * 10**(-28.0)
volume = 75 * 16 * 35 / 2
N = 1 / 100
cosmic_ray_ratio = 0.563

def dN_dt(sigma):
    dN_dt = rho * N_A * sigma * N * cosmic_ray_ratio * volume / A
    return dN_dt

dN_dt = dN_dt(sigma)
print("sigma", sigma ,"cm^2")
print("-dN / dt" ,dN_dt)