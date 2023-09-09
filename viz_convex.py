import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-2, 2, 400)

x1, x2 = -1, 1
y1, y2 = f(x1), f(x2)

line_y = np.linspace(y1, y2, len(x))

plt.figure(figsize=(8,6))
plt.plot(x, f(x), label='f(x) = x^2', color='blue')
plt.plot(x, line_y, label='Line connecting (-1,1) and (1,1)', linestyle='--', color='red')

plt.scatter([x1, x2], [y1, y2], color='green', zorder=5)
plt.scatter(0, f(0), color='magenta', zorder=5)

plt.annotate('(-1,1)', (x1, y1), textcoords="offset points", xytext=(-10,-10), ha='center')
plt.annotate('(1,1)', (x2, y2), textcoords="offset points", xytext=(10,-10), ha='center')
plt.annotate('(0,0)', (0, 0), textcoords="offset points", xytext=(0,-20), ha='center')

plt.title("Visualization of Convexity for f(x) = x^2")
plt.legend()

plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
