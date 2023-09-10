import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

ax.grid(True, linestyle='--')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Vector Space V and its Subspace W')

x_w = np.linspace(-5, 5, 100)
y_w = x_w

ax.plot(x_w, y_w, linewidth=2, label='Subspace W (Line y = x)', color='r')

vectors_in_w = np.array([[1, 1], [-2, -2], [3, 3]])
for vec in vectors_in_w:
    ax.arrow(0, 0, vec[0], vec[1], head_width=0.2, head_length=0.2, fc='blue', ec='blue')

ax.text(1, 1, 'u', fontsize=12, color='blue')
ax.text(-2, -2, 'v', fontsize=12, color='blue')
ax.text(3, 3, 'cu', fontsize=12, color='blue')

ax.legend()

plt.show()
