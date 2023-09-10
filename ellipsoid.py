import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# P = [[9, 0, 0], [0, 4, 0], [0, 0, 1]]
# P^(1/2) can be represented as diag([3, 2, 1])
x_transformed = 3 * x
y_transformed = 2 * y
z_transformed = 1 * z

ax.plot_surface(x_transformed, y_transformed, z_transformed, color='b', alpha=0.6)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Ellipsoid')

plt.show()
