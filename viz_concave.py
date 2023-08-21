import numpy as np
import matplotlib.pyplot as plt

# Define the concave function
def f(x):
    return -x**2

# Generate x values
x = np.linspace(-2, 2, 400)

# Choose two points on the function to visualize the concavity
x1, x2 = -1.5, 1
y1, y2 = f(x1), f(x2)

# Calculate the line connecting these two points for visualization
lambda_values = np.linspace(0, 1, len(x))
line_y = lambda_values * y1 + (1 - lambda_values) * y2

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, f(x), label="f(x) = -x^2", color='blue')
plt.plot([x1, x2], [y1, y2], label='Line segment', linestyle='--', color='red')

# Highlight the chosen points
plt.scatter([x1, x2], [y1, y2], color='green', zorder=5)
plt.annotate(f'({x1},{y1})', (x1, y1), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(f'({x2},{y2})', (x2, y2), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Visualization of a Concave Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
