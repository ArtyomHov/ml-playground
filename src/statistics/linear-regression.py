import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg
import patsy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


N = 100
x1 = np.random.randn(N)
x2 = np.random.randn(N)
data = pd.DataFrame({'x1': x1, 'x2': x2})
def y_true(x1, x2):
    return 1 + 2 * x1 + 3 * x2 + 4 * x1 * x2
data["y_true"] = y_true(x1, x2)

e = 0.5 * np.random.randn(N)
data["y"] = data["y_true"] + e

model = smf.ols("y ~ x1 + x2", data)
result = model.fit()
print(result.summary())

z, p = stats.normaltest(result.fittedvalues.values)
print(p)

fig, ax = plt.subplots(figsize=(8, 4))
smg.qqplot(result.resid, ax=ax)
plt.show()

model = smf.ols("y ~ x1 + x2 + x1*x2", data)
result = model.fit()
print(result.summary())

z, p = stats.normaltest(result.fittedvalues.values)
print(p)

fig, ax = plt.subplots(figsize=(8, 4))
smg.qqplot(result.resid, ax=ax)
plt.show()

x = np.linspace(-1, 1, 50)
X1, X2 = np.meshgrid(x, x)
new_data = pd.DataFrame({'x1': X1.ravel(), 'x2': X2.ravel()})

y_pred = result.predict(new_data)

print(y_pred.shape)
y_pred = y_pred.values.reshape(50, 50)

fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey = True)
def plot_y_contour(ax, Y, title):
    c = ax.contourf(X1, X2, Y, 15, cmap=plt.cm.RdBu)
    ax.set_xlabel(r"$x_1$", fontsize=20)
    ax.set_ylabel(r"$x_2$", fontsize=20)
    ax.set_title(title)
    cb = fig.colorbar(c, ax=ax)
    cb.set_label(r"$y$", fontsize=20)
    

plot_y_contour(axes[0], y_true(X1, X2), "true_relation")
plot_y_contour(axes[1], y_pred, "fitted model")
plt.show()