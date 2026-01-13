import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def euler(x0, y0, h, xn):
    x = np.arange(x0, xn+h, h)
    y = np.zeros(len(x))
    y[0] = y0

    for i in range(1, len(x)):
        y[i] = y[i-1] + h * f(x[i-1], y[i-1])

    return x, y

x, y = euler(0, 1, 0.1, 2)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler Method Solution")
plt.show()