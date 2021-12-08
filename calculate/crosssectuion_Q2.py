import ALLM
import math
import numpy as np
import matplotlib.pyplot  as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2

E_mu = 1.5
m_N = 0.94
m_pi = 0.14
a = 1.0 / 137.0
W = 1.25
E_gamma = W * W / (2 * m_N)
y = E_gamma / E_mu
Q2_min = m_pi **2 * y**2 / (1 - y)
z = y + 0.3
teisu = a / math.pi
GeV_cm = 3.88 * 10**(-26.0)

logy = np.log(z / y)
y_minus = z - y
y2_minus = (z **2) - (y **2)

division_number = 1000

#parameter dN/dt
rho = 1.0
N_A = 6.0 * 10**23
A = 1.0
Pb = 20 * 20 * 10

part_sigma = []
Q_variable = []
sigma_Q = []
sigma_Q_variable = []
dNdt = []

#define j = Q2, larger than Q2_min
j = Q2_min + 0.001
while j < 1.0:
    total_logQ2 = 0.0
    total_Q2_minus = 0.0
    total_sigma_µN_cm = 0.0
    #integrate by Q^2
    for i  in range(0, division_number):
        x = j / (2 * E_gamma * m_N)

        sigma_tot = ( (4 * math.pi **2 * a ) / ( j * (1 - x)) )  * ((j + 4 * m_N **2 * x **2) / j ) * ALLM.allm_f2(x, j)
        logQ = np.log(j / Q2_min)
        Q_minus = Q2_min * ((1 / j) - (1 / Q2_min) ) 

        #difine range of integration
        Q2_differnce = j - Q2_min
        left_range_Q = Q2_min + ( i * Q2_differnce / division_number )
        right_range_Q =  Q2_min + ( (i + 1)  * Q2_differnce / division_number)
       
       #integrate from i to i+1
        temp_logQ2 = np.log(right_range_Q / left_range_Q)
        temp_Q2_minus = Q2_min * ((1 / right_range_Q) - (1/ left_range_Q) )

        #integrate from i to i+1  + integrate from i+1 to i+2 +... + integrate from division-1 to division 
        total_logQ2 += temp_logQ2
        total_Q2_minus += temp_Q2_minus

    #interate by y
    for i in range(0, division_number):
        y_difference = z - y
        #difine range
        left_range_y = y + ( i * y_difference / division_number)
        right_range_y = y + ( (i + 1) * y_difference / division_number)

        #integrate from i to i+1
        temp_logy = np.log(right_range_y / left_range_y)
        temp_y_minus = right_range_y - left_range_y
        temp_y2_minus = (right_range_y **2) - (left_range_y **2)
        partially_sigma_µN_GeV = sigma_tot * teisu * (((total_logQ2 + total_Q2_minus) * temp_logy) - ((total_logQ2 + total_Q2_minus) * temp_y_minus) + (total_logQ2 * temp_y2_minus / 4.0) )
        temp_partially_sigma_µN_cm = partially_sigma_µN_GeV * GeV_cm

        part_sigma.append(temp_partially_sigma_µN_cm)
        #integrate from i to i+1  + integrate from i+1 to i+2 +... + integrate from division-1 to division
        total_sigma_µN_cm += temp_partially_sigma_µN_cm  
         
        #not integrate
        sigma_µN_GeV = sigma_tot * teisu * ( ( (logQ + Q_minus) * logy) - ((logQ + Q_minus) * y_minus) + (logQ * y2_minus /4) )
        sigma_µN_cm = sigma_µN_GeV * GeV_cm

        dNdt_rough =  -rho * N_A * sigma_µN_cm * Pb / A

    dNdt_integation = -rho * N_A * total_sigma_µN_cm * Pb / A
        
    Q_variable.append(j)
    sigma_Q.append(sigma_µN_cm)
    sigma_Q_variable.append(total_sigma_µN_cm)
    dNdt.append(dNdt_integation)

    j += 0.001

#print(Q2_min)
#print(Q_variable)
#print(sigma_Q_variable)

#plt.plot(Q_variable, sigma_Q_variable, label='Q^2_sigma_integrated')
#plt.xlabel('Q^2 [GeV^2]')
#plt.ylabel('sigma_µN [cm^2]')
#plt.savefig('Q^2_sigma.png', bbox_inches="tight", pad_inches=0.05)

plt1.plot(Q_variable, dNdt, '--')
plt1.xlabel('Q^2 [cm^2]')
plt1.ylabel('dN/dt')
plt1.savefig('Q^2_dNdt.png', bbox_inches="tight", pad_inches=0.05)

#plt2.plot(Q_variable, sigma_Q, label='Q^2_sigma_approximation')
#plt2.xlabel('Q^2 [GeV^2]')
#plt2.ylabel('sigma_µN [cm^2]')
#plt2.savefig('Q^2_sigma_absruct.png', bbox_inches="tight", pad_inches=0.05)
#plt2.legend()
plt2.show()
#plt1.show()