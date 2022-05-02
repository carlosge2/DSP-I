import numpy as np
from scipy import signal

# Exemplo 4.7

b=np.array([0,1])
a=np.array([3,-4,1])

[R,p,C]=signal.residuez(b,a)
print("R =",R)
print("p =",p)
print("C =",C)
