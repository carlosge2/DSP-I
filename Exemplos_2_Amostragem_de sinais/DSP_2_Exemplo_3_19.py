import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

# exemplo 3.19

# Sinal analógico
Dt = 0.00005
t = np.arange(-100,101)*Dt
xa = np.exp(-1000*np.abs(t))

# a. Sinal tempo-discreto  Fs = 5000 am/s
Ts = 0.0002
n = np.arange(-25,26)
x = np.exp(-1000*np.abs(n*Ts))

# Transformada de Fourier a tempo discreto
K = 500
k = np.arange(K+1)
w = k*np.pi/K
X = [x] @ np.exp(-1j*np.transpose([n])@[w])
X = np.real(X)

w = np.concatenate((-np.flip([w]),[w]),axis=1) 
w=w[0]
X = np.concatenate((np.flip(X),X),1)  
X=X[0]

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Sinal discreto, Ts = 0.2 ms")
axs[0].plot(t*1000,xa)
axs[0].stem(n*Ts*1000,x,'r')
axs[0].grid()
axs[0].set_xlabel("t in msec.")
axs[0].set_ylabel("x1[n]")

axs[1].set_title("Transformada de Fourier a tempo discreto")
axs[1].plot(w/np.pi,X)
axs[1].grid()
axs[1].set_xlabel("frequência em unidades de PI")
axs[1].set_ylabel("X1(W)")

fig.tight_layout()


# b. Sinal tempo-discreto  Fs = 1000 am/s
Ts = 0.001
n = np.arange(-5,6)
x = np.exp(-1000*np.abs(n*Ts))

# Transformada de Fourier a tempo discreto
K = 500
k = np.arange(K+1)
w = k*np.pi/K
X = [x] @ np.exp(-1j*np.transpose([n])@[w])
X = np.real(X)

w = np.concatenate((-np.flip([w]),[w]),axis=1) 
w=w[0]
X = np.concatenate((np.flip(X),X),1)  
X=X[0]

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Sinal discreto, Ts = 1 ms")
axs[0].plot(t*1000,xa)
axs[0].stem(n*Ts*1000,x,'r')
axs[0].grid()
axs[0].set_xlabel("t in msec.")
axs[0].set_ylabel("x2[n]")

axs[1].set_title("Transformada de Fourier a tempo discreto")
axs[1].plot(w/np.pi,X)
axs[1].grid()
axs[1].set_xlabel("frequência em unidades de PI")
axs[1].set_ylabel("X2(W)")
axs[1].axis([-1,1,0,2.5])

fig.tight_layout()

plt.show()