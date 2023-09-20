import numpy as np
import matplotlib.pyplot as plt

def f_strong(x):
    return x ** 2 + x ** 4

def f_convex(x):
    return x ** 2

x_point_strong = 1
x_point_convex = 1

x_values = np.linspace(-2, 2, 400)

y_strong = f_strong(x_values)
y_convex = f_convex(x_values)


y_lower_bound_strong = f_strong(x_point_strong) + 2 * x_point_strong * (x_values - x_point_strong) + 1 * (x_values - x_point_strong) ** 2
y_lower_bound_convex = f_convex(x_point_convex) + 2 * x_point_convex * (x_values - x_point_convex) + 0 * (x_values - x_point_convex) ** 2

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values, y_strong, label='Strongly Convex: $f(x) = x^2 + x^4$', linewidth=2)
plt.plot(x_values, y_lower_bound_strong, label='Lower Bound Parabola', linestyle='--')
plt.scatter([x_point_strong], [f_strong(x_point_strong)], color='red')
plt.legend()
plt.title('Strongly Convex Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x_values, y_convex, label='Convex: $f(x) = x^2$', linewidth=2)
plt.plot(x_values, y_lower_bound_convex, label='Tangent Line (no strong convexity)', linestyle='--')
plt.scatter([x_point_convex], [f_convex(x_point_convex)], color='red')
plt.legend()
plt.title('Convex but Not Strongly Convex Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.tight_layout()
plt.show()
