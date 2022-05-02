import matplotlib.pyplot as plt
import numpy as np


N = 6
n = np.arange(N)
x = np.cos(2*np.pi*n/6)

plt.figure()
plt.stem(n, x, 'r')
plt.title('cos(2*pi*n/6), N = 6')
plt.ylabel('Amplitude')
plt.xlabel('n')

X = np.fft.fft(x,N)
#w=n*(2*np.pi/N)

plt.figure()
plt.stem(n, abs(X), 'b')
plt.xlabel('k')
plt.ylabel('|X(k)|')
plt.title('DFT Amplitude, N = 6')

N = 12
n = np.arange(N)
x = np.cos(2*np.pi*n/6)

plt.figure()
plt.stem(n, x, 'r')
plt.title('cos(2*pi*n/6), N = 12')
plt.ylabel('Amplitude')
plt.xlabel('n')

X = np.fft.fft(x,N)
#w=n*(2*np.pi/N)

plt.figure()
plt.stem(n, abs(X), 'b')
plt.xlabel('k')
plt.ylabel('|X(k)|')
plt.title('DFT Amplitude, N = 12')

N = 16
n = np.arange(N)
x = np.cos(2*np.pi*n/6)

plt.figure()
plt.stem(n, x, 'r')
plt.title('cos(2*pi*n/6), N = 16')
plt.ylabel('Amplitude')
plt.xlabel('n')

X = np.fft.fft(x,N)
#w=n*(2*np.pi/N)

plt.figure()
plt.stem(n, abs(X), 'b')
plt.xlabel('k')
plt.ylabel('|X(k)|')
plt.title('DFT Amplitude, N = 16')

plt.show()



