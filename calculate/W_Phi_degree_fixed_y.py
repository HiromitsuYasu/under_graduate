import numpy as np
import matplotlib.pyplot as plt
import function_for_angle_distribution
import function_for_sigma

E_gamma_range_min = 0.3
E_gamma_range_max = 0.5

division = 5
y_range_min = function_for_sigma.calculate_y_from_E_gamma(E_gamma_range_min)
y_range_max = function_for_sigma.calculate_y_from_E_gamma(E_gamma_range_max)
y = np.linspace(y_range_min, y_range_max, division)

fig = plt.figure()

for y_value in y:
    Q2_min = function_for_sigma.calculate_Q2_min_from_y(y_value)
    Q2_max = function_for_sigma.calculate_Q2_max_from_y(y_value)
    Q2 = np.linspace(Q2_min, Q2_max, division * 10)
    plt.plot(Q2, function_for_angle_distribution.Phi(y_value, Q2) * 180 / np.pi, label = "y = {:.2f}".format(y_value))

plt.legend()
plt.xlabel('Q^2 [Gev^2]')
plt.ylabel("degree")
plt.title('Phi fixed y')
plt.grid()
fig.savefig("./graph/Phi_degree_fixed_y.png")