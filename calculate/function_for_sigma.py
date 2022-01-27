from matplotlib import units
import numpy as np
import ALLM_num as ALLM

E_mu  = 1.5  # GeV
m_p = 0.938 # GeV
m_pi = 0.14 # GeV
W_limit = m_p + m_pi
alpha = 1.0 / 137.0
division_number = 10

def calculate_y_from_E_gamma(E_gamma):
    y = E_gamma / E_mu
    return y

def calculate_Q2_min_from_y(y):
    Q2_min = (m_p**2 * y**2) / (1 - y)
    return Q2_min

def calculate_Q2_max_from_y(y):
    Q2_max = m_p**2 + 2 * m_p * E_mu * y - W_limit**2
    return Q2_max

def calculate_x_from_Q2(Q2, y):
    x = Q2 / (2 * E_mu * y * m_p)
    return x

def calculate_flux(Q2,y,Q2_min):
    flux = (alpha / (y * np.pi)) * (1 / Q2) * ( (1 - y) * (1 - (Q2_min / Q2) )  + (y **2 / 2) )
    return flux

def sigma_used_article(y, Q2, sigma_tot):
    Q2_min = calculate_Q2_min_from_y(y) 
    flux = calculate_flux(Q2,y,Q2_min)
    sigma_used_article = flux * sigma_tot
    return sigma_used_article

def calculate_sigma_tot(y, Q2):
    x = calculate_x_from_Q2(Q2, y)
    sigma_tot = ((4.0 * np.pi**2 * alpha) / (Q2 * (1 - x)) ) * ((Q2 + 4.0 * m_p**2 * x**2) / Q2) * ALLM.allm_f2(x, Q2)
    return sigma_tot

def calculate_sigma_flux(y,Q2):
    Q2_min = calculate_Q2_min_from_y(y) 
    flux = calculate_flux(Q2,y,Q2_min)
    sigma_tot = calculate_sigma_tot(y, Q2)
    sigma_flux = flux * sigma_tot
    return sigma_flux

def sigma_structure(y, x):
    Q2 = 2 * x * E_mu * y * m_p
    F1 = ALLM.allm_f2(x, Q2) / (2 * x)
    first_term = (8 * np.pi * alpha**2 * m_p * E_mu) / (Q2 **2)
    secound_term_1 = (1 + (1 - y)**2) / 2
    secound_term_2 = 2 * x * F1
    secound_term_3 = (1 - y) * (ALLM.allm_f2(x , Q2) - 2 * x * F1)
    secound_term_4 = (m_p * x * y * ALLM.allm_f2(x, Q2)) / (2 * E_mu)
    secound_term = (secound_term_1 * secound_term_2) + secound_term_3 - secound_term_4
    sigma_structure = first_term * secound_term 
    return sigma_structure
