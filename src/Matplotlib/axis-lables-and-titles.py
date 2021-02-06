import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 50, 500)
y = np.sin(x) * np.exp(-x/10)

fig, ax = plt.subplots(figsize=(8, 2), subplot_kw={'facecolor':"#ebf5ff"})

ax.plot(x, y, lw=2)

ax.set_xlabel("x", labelpad=5, fontsize=18, fontname='serif', color="blue")
ax.set_ylabel("f(x)", labelpad=15, fontsize=15, fontname='serif', color="blue")
ax.set_title("axis labels and title example", fontsize=16, fontname='serif', color="blue")
plt.show()