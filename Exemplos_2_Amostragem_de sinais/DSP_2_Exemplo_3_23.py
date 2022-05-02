import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

# exemplo 3.23

# Sinal tempo-discreto  Fs = 5000 am/s
Ts = 0.0002
Fs = 1/Ts
n = np.arange(-25,26)
nTs = n*Ts
x = np.exp(-1000*np.abs(nTs))

fig, axs = plt.subplots(nrows=2, ncols=1)
tt=np.concatenate((nTs*1000,np.array([1])),None)
axs[0].set_title("Sinal reconstruído de x1[n] usando ZOH")
axs[0].stairs(x,tt)
axs[0].stem(n*Ts*1000,x)
axs[0].grid()
axs[0].set_xlabel("t em msec.")
axs[0].set_ylabel("xa(t)")


# Sinal tempo-discreto  Fs = 1000 am/s
Ts = 0.001
Fs = 1/Ts
n = np.arange(-5,6)
nTs = n*Ts
x = np.exp(-1000*np.abs(nTs))

tt=np.concatenate((nTs*1000,np.array([1])),None)
axs[1].set_title("Sinal reconstruído de x2[n] usando ZOH")
axs[1].stairs(x,tt)
axs[1].stem(n*Ts*1000,x)
axs[1].grid()
axs[1].set_xlabel("t em msec.")
axs[1].set_ylabel("xa(t)")

fig.tight_layout()


# Sinal tempo-discreto  Fs = 5000 am/s
Ts = 0.0002
Fs = 1/Ts
n = np.arange(-25,26)
nTs = n*Ts
x = np.exp(-1000*np.abs(nTs))

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Sinal reconstruído de x1[n] usando FOH")
axs[0].plot(nTs*1000,x)
axs[0].stem(n*Ts*1000,x)
axs[0].grid()
axs[0].set_xlabel("t em msec.")
axs[0].set_ylabel("xa(t)")


# Sinal tempo-discreto  Fs = 1000 am/s
Ts = 0.001
Fs = 1/Ts
n = np.arange(-5,6)
nTs = n*Ts
x = np.exp(-1000*np.abs(nTs))


axs[1].set_title("Sinal reconstruído de x2[n] usando FOH")
axs[1].plot(nTs*1000,x)
axs[1].stem(n*Ts*1000,x)
axs[1].grid()
axs[1].set_xlabel("t em msec.")
axs[1].set_ylabel("xa(t)")

fig.tight_layout()


plt.show()