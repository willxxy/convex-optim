import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)
x, y = np.meshgrid(x, y)

p_values = [0, 0.5, 1, 2, np.inf]
titles = ['$L_0$', '$L_1/2$', '$L_1$', '$L_2$', '$L_{\infty}$']

fig, axes = plt.subplots(1, 5, figsize=(18, 6))

for p, title, ax in zip(p_values, titles, axes):
    if p == np.inf:
        norm = np.maximum(np.abs(x), np.abs(y))
    elif p == 0:
        ax.axhline(0, color='blue', linewidth=2)
        ax.axvline(0, color='blue', linewidth=2)
    else:
        norm = (np.abs(x)**p + np.abs(y)**p)**(1/p)
    if p != 0:
        ax.contour(x, y, norm, levels=[1], colors='blue')

    ax.set_title(title)
    ax.set_aspect('equal', 'box')
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.grid(True)

plt.suptitle('Visualization of $L_p$ Balls for Different $p$')
plt.show()
