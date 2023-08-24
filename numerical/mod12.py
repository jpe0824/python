import numpy as np
import math

def find_intregral(n):
    x, y = np.zeros(n), np.zeros(n)
    x1 = np.random.uniform(-1, 1, n)
    y1 = np.random.uniform(-1, 1, n)

    count = -1
    while (1):
        for i in range(n):
            if x1[i]*x1[i]+y1[i]*y1[i] < 1:
                count +=1
                x[count] = x1[i]
                y[count] = y1[i]
                if count == (n-1): break
        if count == (n-1): break
        x1 = np.random.uniform(-1,1,n)
        y1 = np.random.uniform(-1,1,n)
    funcSum = 0.
    for i in range(n):
        funcSum += math.exp(x[i]*x[i]*y[i]*y[i])
    integral = funcSum*math.pi/n
    return integral

print(find_intregral(1))