import matplotlib.pyplot as plt
import numpy as np

points = np.array([[0, 0], [1, 3], [4, 3], [5, 1], [2, 0]])

points = np.vstack([points, points[0]])

plt.figure()
plt.fill(points[:, 0], points[:, 1], 'b-', alpha=0.6, label='Convex Set')
plt.scatter(points[:, 0], points[:, 1], color='red')
plt.plot(points[:, 0], points[:, 1], 'r--')

point1 = np.array([1, 1])
point2 = np.array([3, 2])
plt.scatter([point1[0], point2[0]], [point1[1], point2[1]], color='green', zorder=5)
plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g-', linewidth=2, zorder=4)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Convex Set and Convex Combination')
plt.legend()
plt.grid(True)
plt.show()
