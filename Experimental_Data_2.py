import matplotlib.pyplot as plt
import numpy as np

I = np.array([27.5, 43.1, 56.3, 67.5, 79.2])
U = np.array([0.21, 0.81, 1.3, 1.99, 2.67])

plt.plot(I, U, '--', I, U, 'r.', label = "V/A")
plt.title("Lamp's V/A", fontsize = 18)
plt.xlabel("Current/mA", fontsize = 16)
plt.ylabel("Voltage/V", fontsize = 16)
plt.legend()

for i, u in zip(I, U):
	plt.text(i, u, (i,u), ha='center', va='bottom', fontsize = 10)

plt.grid(True)

plt.xticks(np.arange(0, 85, 5))
plt.yticks(np.arange(0, 2.8, 0.1))
plt.show()