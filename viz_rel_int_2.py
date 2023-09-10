import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

x1 = np.linspace(-1, 1, 30)
x2 = np.linspace(-1, 1, 30)
X1, X2 = np.meshgrid(x1, x2)
X3 = np.zeros_like(X1)

ax.plot_surface(X1, X2, X3, alpha=0.5, color='b')

relint_x1 = np.linspace(-0.9, 0.9, 10)
relint_x2 = np.linspace(-0.9, 0.9, 10)
relint_X1, relint_X2 = np.meshgrid(relint_x1, relint_x2)
relint_X3 = np.zeros_like(relint_X1)

ax.scatter(relint_X1, relint_X2, relint_X3, color='r', label='Relative Interior')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('X3')
ax.set_title('Square C in R3 and its Relative Interior')
ax.legend()

plt.show()
