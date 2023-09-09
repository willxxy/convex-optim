import matplotlib.pyplot as plt
import numpy as np

# Define three non-collinear points in C
points = np.array([[1, 1], [4, 1], [2, 4]])

# Calculate the affine combinations of these points
theta_values = np.linspace(0, 1, 50)
affine_hull = []

for theta1 in theta_values:
    for theta2 in np.linspace(0, 1 - theta1, 50):
        theta3 = 1 - theta1 - theta2
        combination = theta1 * points[0] + theta2 * points[1] + theta3 * points[2]
        affine_hull.append(combination)

affine_hull = np.array(affine_hull)


### There is a point on 1.0, 1.0
plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], c='red', label='Points in C')
plt.scatter(affine_hull[:, 0], affine_hull[:, 1], c='blue', alpha=0.2, label='Affine Hull (aff C)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Affine Hull of a Set of Points')
plt.legend()
plt.grid(True)
plt.show()