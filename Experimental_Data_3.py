import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline as spline

U = np.array([0, 0.15, 0.24, 0.3, 0.41, 0.51, 0.6, 0.7, 0.75, 0.76, 0.78])
I = np.array([0, 0, 0, 0, 0, 0.02, 1.9, 13.9, 46.7, 59.1, 98.1])

# U_smooth = np.linspace(U.min(), I.max(), 300)
# I_smooth = spline(U, I)(U_smooth)

plt.plot(U, I, '--', U, I, 'r.', label = "V/A")
plt.title("Diode's Positive V/A", fontsize = 18)
plt.xlabel("Voltage/V", fontsize = 16)
plt.ylabel("Current/mA", fontsize = 16)
plt.legend()

# for u, i in zip(U, Iv):
# 	plt.text(u, i, (u,i), ha='right', va='bottom', fontsize = 5)

plt.grid(True)

plt.xticks(np.arange(0, 0.9, 0.1))
plt.yticks(np.arange(0, 105, 5))
plt.show()