import numpy as np
import matplotlib.pyplot as plt

Req = 524
Ul = np.array([1.308, 3.975, 5.326, 5.990, 6.386])
Rl = np.array([100, 510, 1000, 1510, 2000])

Uoc = np.array([0, 8.011])
Isc = np.array([15.282, 0])

plt.plot(Uoc, Isc, 'r-.')
plt.show()
