import matplotlib.pyplot as plt
import numpy as np

a, b, c, d = 1, 1, -1, 3

x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
Z = (d - a * X - b * Y) / c

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100)

ax.quiver(0, 0, 0, a, b, c, color='red', label='Normal Vector (a)')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Hyperplane in 3D')
ax.legend()

plt.show()
