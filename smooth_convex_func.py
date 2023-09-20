import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

def grad_f(x):
    return 2 * x

def hessian_f(x):
    return 2

x_point = 1

x_values = np.linspace(-3, 3, 400)
y_values = f(x_values)

y_tangent = f(x_point) + grad_f(x_point) * (x_values - x_point)


B = hessian_f(x_point)
y_upper_bound = f(x_point) + grad_f(x_point) * (x_values - x_point) + (B / 2) * (x_values - x_point)**2

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = x^2', linewidth=2)
plt.plot(x_values, y_tangent, label='Tangent Line at x=1', linestyle='--')
plt.plot(x_values, y_upper_bound, label='Quadratic Upper Bound at x=1', linestyle='--')
plt.scatter([x_point], [f(x_point)], color='red')  # point of tangency
plt.legend()
plt.title('Convex Function, Tangent Line, and Quadratic Upper Bound')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
