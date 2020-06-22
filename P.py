import matplotlib.pyplot as plt
import numpy as np

Ur = np.array([0.8, 1.0, 1.2, 1.3, 1.6, 1.8, 2.1, 2.5, 2.8, 3.2, 3.7, 4.2, 4.7, 5.2, 5.7, 6.1, 6.4, 6.6, 6.6, 6.4, 6.0, 5.6, 5.1, 4.6, 4.1])
Ul = np.array([4.0, 4.5, 5.0, 5.5, 6.0, 6.3, 6.5, 6.5, 6.4, 6.1, 5.7, 5.2, 4.7, 4.2, 3.7, 3.2, 2.8, 2.4, 2.1, 1.8, 1.6, 1.3, 1.2, 1.0, 0.9])
Um = np.array([5.0, 5.7, 6.3, 7.0, 7.7, 8.2, 8.7, 9.1, 9.3, 9.4, 9.5, 9.5, 9.5, 9.5, 9.5, 9.4, 9.4, 9.1, 8.7, 8.3, 7.7, 7.1, 6.4, 5.7, 5.0])

X = np.arange(-12, 13, 1)

w = 0.103
Br = Ur*w
Bl = Ul*w
Bm = Um*w

print(np.around(Br,2))
print('\n')
print(np.around(Bl,2))
print('\n')
print(np.around(Bm,2))

plt.plot(X, Br, '--', label = 'Single Coile(right)')
plt.plot(X, Br, 'b.')
plt.plot(X, Bl, label = 'Single Coile(left)')
plt.plot(X, Bl, 'y.')
plt.plot(X, Bm, 'y-.', label = 'Helmholtz Coile')
plt.plot(X, Bm, 'g.')

plt.title("Magnetic Field Strength", fontsize = 18)
plt.xlabel("Distance/cm", fontsize = 16)
plt.ylabel("Magnetic/T", fontsize = 16)

plt.legend()

plt.grid()
plt.xticks(np.arange(-12, 13, 1))
plt.yticks(np.around(np.arange(0, 9.6*w, 0.5*w), 2))
plt.show()