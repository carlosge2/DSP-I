# Exemplo 6.4

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

b=np.array([1,0,0,0,16+1/16,0,0,0,1])
a=np.array([1,0])

sos = signal.tf2sos(b,a)
print(sos)