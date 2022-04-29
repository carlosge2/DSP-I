import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold,conv_m
import numpy as np
from scipy import signal

#exemplo 2.11

a=np.array([1,-1,0.9])
b=np.array([1])
[x,n]=impseq(0,-20,120)
h=signal.lfilter(b,a,x)
plt.figure()
plt.stem(n,h)

[x,n]=stepseq(0,-20,120)
s=signal.lfilter(b,a,x)
plt.figure()
plt.stem(n,s)

print(sum(abs(h)))

z=np.roots(a)

print(abs(z))

plt.show()