import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 5)
y = np.ones_like(x)

def axes_settings(fig, ax, title, ymax):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, ymax+1)
    ax.set_title(title)

fig, axes = plt.subplots(1, 4, figsize=(16, 3))

# Line width
linewidths = [0.5, 1.0, 2.0, 4.0]
for n, linewidth in enumerate(linewidths):
    axes[0].plot(x, y + n, color='blue', linewidth=linewidth)
axes_settings(fig, axes[0], 'linewidth', len(linewidths))

# Line style
linestyles = ['-', '-.', ':']
for n, linestyle in enumerate(linestyles):
    axes[1].plot(x, y + n, color='blue', lw=2, linestyle=linestyle)
#Custom dash style
line, = axes[1].plot(x, y + 3, color='blue', lw=2)
length1, gap1, length2, gap2 = 10, 7, 20, 7
line.set_dashes([length1, gap1, length2, gap2])
axes_settings(fig, axes[1], 'linetypes', len(linestyles) + 1)

# marker types
markers = ['o', 's', '.', '1', '2', '3', '4']
for n, marker in enumerate(markers):
    # lw - shorthand for linewidth, ls - shorthand for linestyle
    axes[2].plot(x, y + n, color='blue', lw=2, ls='dotted', marker=marker)
axes_settings(fig, axes[2], 'markers', len(markers))

# Marker size and color
markersizecolors = [(4, 'white'), (0, 'red'), (12, 'yellow'), (16, 'lightgreen')]
for n, (markersize, markerfacecolor) in enumerate(markersizecolors):
    axes[3].plot(x, y + n, color='blue', lw=1, ls='-', marker='o', markersize=markersize, markerfacecolor=markerfacecolor, markeredgewidth=2)
axes_settings(fig, axes[3], 'marker size/color', len(markersizecolors))
plt.show()