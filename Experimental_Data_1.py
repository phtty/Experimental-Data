import matplotlib.pyplot as plt
import numpy as np

I = np.array([63, 39.8, 30.3, 23.6, 20.1, 17.2, 15, 13.3, 11.9, 10.7, 9.7])
U = np.array([3.05, 1.93, 1.47, 1.14, 0.97, 0.83, 0.72, 0.64, 0.57, 0.52, 0.47])

I2 = np.array([63, 40, 30.7, 24.1, 20.2, 17.2, 15, 13.1, 11.8, 10.8, 9.7])
U2 = np.array([2.97, 1.88, 1.45, 1.13, 0.95, 0.81, 0.71, 0.62, 0.56, 0.5, 0.46])

plt.plot(I, U, '--', I, U, 'r.', label = "External")
plt.plot(I2, U2, I2, U2, 'g.', label = "Inside")
plt.title("V/A Characteristic", fontsize = 18)
plt.xlabel("Current/mA", fontsize = 16)
plt.ylabel("Voltage/V", fontsize = 16)
plt.legend()

plt.grid(True)

plt.xticks(np.arange(0, 70, 5))
plt.yticks(np.arange(0, 3.2, 0.1))
plt.show()