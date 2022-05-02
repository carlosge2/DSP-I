from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np
from scipy import signal

# Exemplo 4.6

b=np.array([0,0,0,0.25,-0.5,0.0625])
a=np.array([1,-1,0.75,-0.25,0.0625])
[delta,n]=impseq(0,0,7)
print("delta =",delta)
print("n =",n)

x=signal.lfilter(b,a,delta)
print("x[n](lfilter) =",x)

[x1,n1]=stepseq(2,0,7)
x2=[(n-2)*(1/2)**(n-2)*np.cos(np.pi*(n-2)/3)]
[x,nx]=sigmult(x1,n1,x2,n)
print("x[n] = ",x)
