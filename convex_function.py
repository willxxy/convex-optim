import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 400)

y = x**2

x1, x2 = -1.5, 1.5
y1, y2 = x1**2, x2**2

line_y = y1 + (y2 - y1)/(x2 - x1) * (x - x1)

plt.figure()
plt.plot(x, y, label='f(x) = x^2', linewidth=2)
plt.scatter([x1, x2], [y1, y2], color='red') 
plt.plot(x, line_y, 'r--', label='Line joining two points')
plt.fill_between(x, y, line_y, where=(y <= line_y), interpolate=True, color='grey', alpha=0.3, label='Region below line')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Convex Function')
plt.legend()
plt.grid(True)
plt.show()
