# Teste para "provar" que um sistema Ã© invariante no tempo (TI)

import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

nx=np.array(range(101))
x=np.sqrt(10)*np.random.randn(len(nx))

# sistema sob teste: y[n] = x[n]*u[n]

[u,nu]=stepseq(0,0,100)
y=x*u
[y1,ny1]=sigshift(y,nx,1) #y[n-1]

[x1,nx1]=sigshift(x,nx,1) #x[n-1]
[y2,ny2]=sigmult(x1,nx1,u,nu) #T{x[n-1]}

[diff,ndiff]=sigadd(y1,ny1,-y2,ny2)
diff=sum(abs(diff))

if diff < 1e-5:
    print(' **** Sistema é Invariante no Tempo ***')
else:
    print(' **** Sistema não é Invariante no Tempo ***')