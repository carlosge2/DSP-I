import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

n = np.arange(-2,11)
x = np.array(list(range(1,8))+list(range(6,0,-1)))

#exemplo 2.2a
[x11,n11] = sigshift(x,n,5)
[x12,n12] = sigshift(x,n,-4)
[x1,n1] = sigadd(2*x11,n11,-3*x12,n12)

plt.figure()
plt.stem(n1,x1)

#exemplo 2.2b
[x21,n21] = sigfold(x,n)
[x21,n21] = sigshift(x21,n21,3)
[x22,n22] = sigshift(x,n,2)
[x22,n22] = sigmult(x,n,x22,n22)
[x2,n2] = sigadd(x21,n21,x22,n22)

plt.figure()
plt.stem(n2,x2)


plt.show()