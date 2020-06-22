import matplotlib.pyplot as plt
import numpy as np

X = np.arange(0, 1.1, 0.1)
I = np.array([38.3, 18.6, 13, 9.4, 7.7, 6.4, 5.5, 4.8, 4.2, 3.8, 3.4])

I2 = np.array([38.3, 34.4, 31.6, 28.8, 26.9, 25.0, 23.4, 21.8, 20.5, 19.3, 18.3])

plt.plot(X, I, '--', X, I, 'r.', label = 'K=0.1')
plt.plot(X, I2, X, I2, 'g.', label = 'K=1')
plt.title("Current Control", fontsize = 18)
plt.xlabel("R0/Rac", fontsize = 16)
plt.ylabel("Current/mA", fontsize = 16)
plt.legend()

for x, i in zip(X, I):
	x = round(x,1)
	plt.text(x, i, (x,i), ha='center', va='bottom', fontsize = 7)
for x, i2 in zip(X, I2):
	x = round(x,1)
	plt.text(x, i2, (x,i2), ha='center', va='bottom', fontsize = 7)

plt.grid(True)

plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.arange(0, 40, 1.5))
plt.show()