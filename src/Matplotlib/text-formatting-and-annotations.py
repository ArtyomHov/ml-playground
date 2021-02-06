import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12, 4))

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.05, 0.25)
ax.axhline(0)

# text label
ax.text(0, 0.1, "Text label", fontsize=14, family="serif")

# annotation
ax.plot(1, 0, "o")
ax.annotate("Annotation", fontsize=14, family="serif", xy=(1, 0), xycoords="data",
xytext=(+20, +50), textcoords="offset points", arrowprops=dict(arrowstyle="->", connectionStyle="arc3, rad=.5"))

#equation
ax.text(2, 0.1, r"Equation: $i\hbar\partial_t \Psi = \hat{H}\Psi$", fontsize=14, family="serif")
plt.show()