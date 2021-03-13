import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg
import patsy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

dataset = sm.datasets.get_rdataset("discoveries")
df = dataset.data.set_index('time').rename(columns={'values': 'discoveries'})
print(df.head(10).T)

fig, ax = plt.subplots(1, 1, figsize = (16, 4))
df.plot(kind='bar', ax=ax)
plt.show()
model = smf.poisson("df.values ~ 1", data=df)

result = model.fit()
print(result.summary())

lmbda = np.exp(result.params)
X = stats.poisson(lmbda)
print(result.conf_int)

X_ci_l = stats.poisson(np.exp(result.conf_int().values)[0,0])
X_ci_u = stats.poisson(np.exp(result.conf_int().values)[0,1])

v, k = np.histogram(df.values, bins=12, range=(0, 12), normed=True)
fig, ax = plt.subplots(1, 1, figsize=(12, 4))
ax.bar(k[:-1], v, color='steelblue', align='center', label='Discoveries per year')
ax.bar(k-0.125, X_ci_l.pmf(k), color='red', alpha=0.5, align='center', width=0.25, label='Poisson fit (CI, lower)')
ax.bar(k, X.pmf(k), color='green', align='center', width=0.5, label='Poisson fit')
ax.bar(k+0.125, X_ci_u.pmf(k), color='red', alpha=0.5, align='center', width=0.25, label='Poisson fit (CI, upper)')
ax.legend()
plt.show()