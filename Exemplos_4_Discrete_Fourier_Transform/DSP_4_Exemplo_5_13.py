# Exemplo 5.13: convolução circular versus linear

import numpy as np

def cirshftt(x,m,N):
    
    # Circular shift of m samples wrt size N in sequence x: (time domain)
    # -------------------------------------------------------------------
    # [y] = cirshftt(x,m,N)
    # y = output sequence containing the circular shift
    # x = input sequence of length <= N
    # m = sample shift
    # N = size of circular buffer
    # Method: y(n) = x((n-m) mod N)
    # Check for length of x
    if len(x) > N:
        print("error: N must be >= the length of x")
    zeros = np.zeros(N-len(x))
    x = np.concatenate((x,zeros))
    n = np.arange(N)
    n = np.mod(n-m,N)
    y = x[n]
    return [y]


def circonvt(x1,x2,N):
    
    # N-point circular convolution between x1 and x2: (time-domain)
    # -------------------------------------------------------------
    # [y] = circonvt(x1,x2,N)
    # y = output sequence containing the circular convolution
    # x1 = input sequence of length N1 <= N
    # x2 = input sequence of length N2 <= N
    # N = size of circular buffer
    # Method: y(n) = sum (x1(m)*x2((n-m) mod N))
    # Check for length of x1
    if len(x1) > N:
        print("error: N must be >= the length of x1")
    # Check for length of x2
    if len(x2) > N:
        print("error: N must be >= the length of x2")
    zeros = np.zeros(N-len(x1))
    x1 = np.concatenate((x1,zeros))
    zeros = np.zeros(N-len(x2))
    x2 = np.concatenate((x2,zeros))    
    m = np.arange(N)
    n2 = np.mod(-m,N)
    x2 = x2[n2]
    H = np.zeros((N,N))
    for n in range(N):
        [HL] = cirshftt(x2,n,N)
        H[n,:] = HL
    [y] = [x1]@(np.conj(np.transpose(H)))
    return [y]
    

x1 = np.array([1,2,2])
x2 = np.array([1,2,3,4])
print("x1 =",x1)
print("\nx2 =",x2)

# convolução linear
y = np.convolve(x1,x2)
print("\nConvolução linear:",y)

# convolução circular N = 4
[y] = circonvt(x1, x2, 4)
print("\nConvolução circular (N=4):",y)

# convolução circular N = 5
[y] = circonvt(x1, x2, 5)
print("\nConvolução circular (N=5):",y)

# convolução circular N = 6
[y] = circonvt(x1, x2, 6)
print("\nConvolução circular (N=6):",y)

# convolução circular N = 7
[y] = circonvt(x1, x2, 7)
print("\nConvolução circular (N=7):",y)