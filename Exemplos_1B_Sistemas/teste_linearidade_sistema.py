#Teste para "provar" que um sistema Ã© linear

import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

n=np.array(range(101))
x1=np.random.rand(len(n))
x2=np.sqrt(10)*np.random.randn(len(n))

# sistema sob teste: y[n] = x[n]*u[n]

[u,n]=stepseq(0,0,100)
y1=x1*u
y2=x2*u

y=(x1+x2)*u

diff = sum (abs(y - (y1 + y2)))

if diff < 1e-5:
    print(' **** Sistema é linear ***')
else:
    print(' **** Sistema não é linear ***')