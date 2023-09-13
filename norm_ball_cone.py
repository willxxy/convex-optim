import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 100)
r = 1.0  # Radius
xc, yc = [2.0, 2.0]  # Center of the ball
x_ball = r * np.cos(theta) + xc
y_ball = r * np.sin(theta) + yc

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d')

ax1.plot(x_ball, y_ball)
ax1.set_aspect('equal', 'box')
ax1.set_title('Norm Ball in R^2')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)

theta = np.linspace(0, 2*np.pi, 30)
r = np.linspace(0, 1, 30)
Theta, R = np.meshgrid(theta, r)

X = R * np.cos(Theta)
Y = R * np.sin(Theta)
Z = R

ax2.plot_surface(X, Y, Z, alpha=0.6)
ax2.set_title('Norm Cone in R^3')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('t')
ax2.grid(True)

plt.show()
