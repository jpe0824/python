import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([1, 2, 2.5, 3, 4, 5])
y = np.array([1, 5, 7, 8, 2, 1])

cs_nat = CubicSpline(x, y, bc_type='natural')
cs_nan = CubicSpline(x, y, bc_type='not-a-knot')
x_new = np.linspace(1,5,50)

y_nat = cs_nat(x_new)
y_nan = cs_nan(x_new)

plt.plot(x, y, 'o', label='Data')
plt.plot(x_new, y_nat, label='Natural Cubic Spline')
plt.plot(x_new, y_nan, label='Cubic Spline with Not-a-Knot End Conditions')
plt.legend()
plt.show()