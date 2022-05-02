# Exemplo 6.1

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

b=np.array([1.0, -3, 11, -27, 18])
a=np.array([16.0, 12, 2, -4, -1])

sos = signal.tf2sos(b,a)
print(sos)

x = signal.unit_impulse(30)
y_tf = signal.lfilter(b, a, x)
y_sos = signal.sosfilt(sos, x)

plt.plot(y_tf, 'r', label='TF')
plt.plot(y_sos, 'k', label='SOS')
plt.legend(loc='best')
plt.grid()

plt.show()