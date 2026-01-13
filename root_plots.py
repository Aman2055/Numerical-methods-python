import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)
y = x**3 - x - 2

plt.plot(x, y)
plt.axhline(0)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Root Visualization")
plt.grid()
plt.show()