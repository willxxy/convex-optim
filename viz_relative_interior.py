import matplotlib.pyplot as plt
import numpy as np

x_line = np.linspace(-5, 5, 100)
y_line = x_line
point_in_C = np.array([2, 2])


fig, ax = plt.subplots(figsize=(8, 8))

ax.plot(x_line, y_line, label='Set C (Line in R^2)', linewidth=2)

segment_x = np.linspace(1.5, 2.5, 10)
segment_y = segment_x

ax.scatter(point_in_C[0], point_in_C[1], color='red', s=100, zorder=5, label='Point in C (Relative Interior)')
ax.plot(segment_x, segment_y, color='green', linewidth=5, alpha=0.5, label='Segment in aff C')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.set_title('Relative Interior of a Set C in R^2')
ax.legend()

plt.show()
