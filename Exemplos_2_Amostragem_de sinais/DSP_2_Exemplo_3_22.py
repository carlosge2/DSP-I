import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

# exemplo 3.22

# Sinal tempo-discreto  Fs = 1000 am/s
Ts = 0.001
Fs = 1/Ts
n = np.arange(-5,6)
nTs = n*Ts
x = np.exp(-1000*np.abs(nTs))

# Reconstrução do sinal contínuo
Dt = 0.00005
t = np.arange(-100,101)*Dt
xa = [x] @ np.sinc(Fs*(np.ones((len(nTs),1))@[t]-np.transpose([nTs])@[np.ones((len(t)))]))
xa=xa[0]

# verificação
print("Erro =", max(abs(xa - np.exp(-1000*abs(t)))))

plt.title("Sinal reconstruido de x2[n] usando a função sinc")
plt.plot(t*1000,xa)
plt.stem(n*Ts*1000,x,'r')
plt.grid()
plt.xlabel("t em msec.")
plt.ylabel("xa(t)")

plt.show()