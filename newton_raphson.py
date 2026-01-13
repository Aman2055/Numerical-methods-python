def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            print(f"Root found at x = {x_new} after {i+1} iterations")
            return x_new
        x = x_new

    print("Max iterations reached")
    return x

newton_raphson(1.5)