import numpy as np

def f(x):
    return x**3 - x - 2

def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            print(f"Root found at x = {c} after {i+1} iterations")
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Max iterations reached")
    return c

bisection(1, 2)