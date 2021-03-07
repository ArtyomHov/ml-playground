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

dataset = sm.datasets.get_rdataset('Icecream', 'Ecdat')
print(dataset.title)
print(dataset.data.info())

model = smf.ols("cons ~ -1 + price + temp", data=dataset.data)
result = model.fit()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
smg.plot_fit(result, 0, ax=ax1)
smg.plot_fit(result, 1, ax=ax2)
plt.show()