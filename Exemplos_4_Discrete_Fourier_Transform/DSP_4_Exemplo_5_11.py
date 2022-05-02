# Exemplo 5.11: Circular shift graphical display

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


# a) plot x((n+4))11

n = np.arange(11)
x = 10*(0.8) ** n

n1 = np.arange(-11,22)
zeros = np.zeros(11)
x1 = np.concatenate((zeros,x))
x1 = np.concatenate((x1,zeros))

x2 = np.concatenate((x,x))
x2 = np.concatenate((x2,x))

x3 = np.concatenate((x2[4:33], x[:4]))


zeros = np.zeros(11)
ones = np.ones(11)
mx = np.concatenate((zeros,ones))
mx = np.concatenate((mx,zeros))
x4 = x3 * mx

fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0,0].set_title('x[n] original')
axs[0,0].stem(n1, x1)
axs[0,0].grid()
axs[0,0].set_xlabel("n")
axs[0,0].axis([-6,17,-1,11])

axs[1,0].set_title("Extensão periodica")
axs[1,0].stem(n1,x2)
axs[1,0].grid()
axs[1,0].set_xlabel("n")
axs[1,0].axis([-6,17,-1,11])

axs[0,1].set_title("Deslocamento periodico")
axs[0,1].stem(n1,x3)
axs[0,1].grid()
axs[0,1].set_xlabel("n")
axs[0,1].axis([-6,17,-1,11])

axs[1,1].set_title("Deslocamento circular")
axs[1,1].stem(n1,x4)
axs[1,1].grid()
axs[1,1].set_xlabel("n")
axs[1,1].axis([-6,17,-1,11])

fig.tight_layout()



# b) plot x((n-3))15


n = np.arange(11)
x = 10*(0.8) ** n
zeros = np.zeros(4)
x = np.concatenate((x,zeros))

n1 = np.arange(-15,30)
zeros = np.zeros(15)
x1 = np.concatenate((zeros,x))
x1 = np.concatenate((x1,zeros))

x2 = np.concatenate((x,x))
x2 = np.concatenate((x2,x))

x3 = np.concatenate((x2[42:45], x2[:42]))

zeros = np.zeros(15)
ones = np.ones(15)
mx = np.concatenate((zeros,ones))
mx = np.concatenate((mx,zeros))
x4 = x3 * mx


fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0,0].set_title('x[n] original')
axs[0,0].stem(n1, x1)
axs[0,0].grid()
axs[0,0].set_xlabel("n")
axs[0,0].axis([-9,25,-1,11])

axs[1,0].set_title("Extensão periodica")
axs[1,0].stem(n1,x2)
axs[1,0].grid()
axs[1,0].set_xlabel("n")
axs[1,0].axis([-9,25,-1,11])

axs[0,1].set_title("Deslocamento periodico")
axs[0,1].stem(n1,x3)
axs[0,1].grid()
axs[0,1].set_xlabel("n")
axs[0,1].axis([-9,25,-1,11])

axs[1,1].set_title("Deslocamento circular")
axs[1,1].stem(n1,x4)
axs[1,1].grid()
axs[1,1].set_xlabel("n")
axs[1,1].axis([-9,25,-1,11])

fig.tight_layout()


plt.show()