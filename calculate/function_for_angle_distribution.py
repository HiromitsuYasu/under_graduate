import numpy as np

E_mu = 1.5
m_mu = 0.1057
p_mu = np.sqrt(E_mu**2 - m_mu**2)

def theta(y,Q2):
    theta = np.arccos((-Q2 - 2 * m_mu **2 + 2 * E_mu **2 * (1 - y)) / (2 * p_mu * np.sqrt( (E_mu **2 * (1 - y)**2) - m_mu **2) ) )
    return theta

def cos_Phi(y, Q2):
    inner = y * E_mu**2 + Q2 / 2
    norm = np.sqrt((E_mu**2 - m_mu**2) * (y**2 * E_mu**2 + Q2))
    cos_Phi = inner / norm
    return cos_Phi

def Phi(y, Q2):
    Phi = np.arccos(cos_Phi(y, Q2))
    return Phi
