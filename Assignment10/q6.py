import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    updates = []
    iter_count = 0
    
    while iter_count < max_iter:
        c = (a + b) / 2
        updates.append(c)
        
        if f(c) == 0 or (b - a) / 2 < tol:
            break
        iter_count += 1
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    return c, updates

a = 2
b = 4

root, updates = bisection_method(f, a, b)

print(f"Root found at: {root}")

updates = np.array(updates)

x = np.linspace(a - 1, b + 1, 1000)
y = f(x)

plt.plot(x, y, label="f(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(root, color='r', linestyle='--', label=f"Root at {root:.5f}")
plt.scatter(updates, f(updates), color='g', label="Midpoints")
plt.legend()

plt.title("Bisection Method Root Finding")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()