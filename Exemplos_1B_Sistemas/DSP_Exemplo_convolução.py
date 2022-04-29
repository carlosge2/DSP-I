import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold,conv_m
import numpy as np


[x1,n]=stepseq(0,-5,50)
[x2,n]=stepseq(10,-5,50)
[x,n] =sigadd(x1,n,-x2,n)

h1=0.9**n
[h,n] = sigmult(h1,n,x1,n)

[y,n]=conv_m(x,n,h,n)

plt.figure()
plt.stem(n,y)
plt.axis([-5, 50, 0 ,8])

plt.show()