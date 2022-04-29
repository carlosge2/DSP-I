import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

#exemplo 2.1a
[x1,n1] = impseq(-2,-5,5) 
[x2,n2] = impseq(4,-5,5)
[y,n] = sigadd(2*x1,n1,-x2,n2)

plt.figure()
plt.stem(n,y)


#exemplo 2.1b
[x1,n1] = stepseq(0,0,20) 
[x2,n2] = stepseq(10,0,20)
[y11,n11] = sigadd(x1,n1,-x2,n2)
[y1,n1] = sigmult(y11,n11,n11,n11)

[x1,n1] = stepseq(10,0,20) 
[x2,n2] = stepseq(20,0,20)
[y11,n11] = sigadd(x1,n1,-x2,n2)
y21=10*np.exp(-0.3*(n11-10))
[y2,n2] = sigmult(y11,n11,y21,n11)

[y,n] = sigadd(y1,n1,y2,n2)

plt.figure()
plt.stem(n,y)


#exemplo 2.1c
n=np.array(range(50))
x1=np.cos(0.04*np.pi*n)
x2=0.2 * np.random.randn(len(n))
y=x1+x2

plt.figure()
plt.stem(n,y)

#exemplo 2.1d
n=np.arange(-10,10)
x=np.array([5,4,3,2,1])
y=np.tile(x,4)

plt.figure()
plt.stem(n,y)


plt.show()