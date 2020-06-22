import matplotlib.pyplot as plt
import numpy as np

X = np.arange(1, -0.1, -0.1)
U = np.array([3, 1.32, 0.9, 0.63, 0.49, 0.4, 0.33, 0.27, 0.2, 0.13, 0])

U2 = np.array([3, 2.44, 2.06, 1.7, 1.44, 1.18, 0.95, 0.72, 0.49, 0.23, 0])

plt.plot(X, U, '--', label = 'K=0.1')
plt.plot(X, U, 'r.')
plt.plot(X, U2, label = 'K=1')
plt.plot(X, U2, 'g.')
plt.title("Voltage Control", fontsize = 18)
plt.xlabel("R0/Rac", fontsize = 16)
plt.ylabel("Voltage/v", fontsize = 16)
plt.legend()

for x, u in zip(X, U):
	x = round(x,1)
	plt.text(x, u, (x,u), ha='center', va='bottom', fontsize = 7)
for x, u2 in zip(X, U2):
	x = round(x,1)
	plt.text(x, u2, (x,u2), ha='center', va='bottom', fontsize = 7)

plt.grid(True)

plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.arange(0, 3.2, 0.1))
plt.show()