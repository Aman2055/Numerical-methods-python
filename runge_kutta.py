import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def rk4(x0, y0, h, xn):
    x = np.arange(x0, xn+h, h)
    y = np.zeros(len(x))
    y[0] = y0

    for i in range(1, len(x)):
        k1 = h * f(x[i-1], y[i-1])
        k2 = h * f(x[i-1] + h/2, y[i-1] + k1/2)
        k3 = h * f(x[i-1] + h/2, y[i-1] + k2/2)
        k4 = h * f(x[i-1] + h, y[i-1] + k3)

        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6

    return x, y

x, y = rk4(0, 1, 0.1, 2)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Runge-Kutta 4th Order Solution")
plt.show()
