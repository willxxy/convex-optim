from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# 2D Simplex (Triangle) in R^2
v0_2D = np.array([0, 0])
v1_2D = np.array([1, 0])
v2_2D = np.array([0.5, 0.866])

theta_2D = np.linspace(0, 1, 20)
simplex_2D = np.array([t1*v0_2D + t2*v1_2D + (1-t1-t2)*v2_2D for t1 in theta_2D for t2 in theta_2D if t1 + t2 <= 1])

# 3D Simplex (Tetrahedron) in R^3
v0_3D = np.array([0, 0, 0])
v1_3D = np.array([1, 0, 0])
v2_3D = np.array([0.5, 0.866, 0])
v3_3D = np.array([0.5, 0.2887, 0.8165])

theta_3D = np.linspace(0, 1, 10)
simplex_3D = np.array([t1*v0_3D + t2*v1_3D + t3*v2_3D + (1-t1-t2-t3)*v3_3D 
                       for t1 in theta_3D for t2 in theta_3D for t3 in theta_3D if t1 + t2 + t3 <= 1])

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 2D Simplex
ax1.scatter(simplex_2D[:, 0], simplex_2D[:, 1], c='blue', alpha=0.6)
ax1.set_title('2D Simplex (Triangle) in R^2')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)

# 3D Simplex
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(simplex_3D[:, 0], simplex_3D[:, 1], simplex_3D[:, 2], c='red', alpha=0.6)
ax2.set_title('3D Simplex (Tetrahedron) in R^3')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.grid(True)

plt.show()
