import numpy as np
import matplotlib.pyplot as plt
import math

f = np.array([200, 400, 600, 800, 1000])
F = np.array([200, 800, 1500, 3000, 5000, 10000, 15000, 30000, 80000])
t = 1/f
T = 1/F
del_t = np.array([-0.8, -0.25, -0.13, -0.08, -0.05])
del_T = np.array([-2.2, -0.4, -0.14, -0.028, 0, 0.014, 0.014, 0.011, 0.0052])

F0 =5033

print(F/F0-F0/F)

# print(del_t/t/1000*2)
# print('\n')
# print(del_T/T/1000*2)
