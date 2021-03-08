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

df = sm.datasets.get_rdataset('iris').data
print(df.info())

print(df.Species.unique())

df_subset = df[df.Species.isin(['versicolor', 'virginica'])].copy()

df_subset.Species = df_subset.Species.map({'versicolor': 1, 'virginica': 0})

df_subset.rename(columns={'Sepal.Length': 'Sepal_Length',
'Sepal.Width': 'Sepal_Width',
'Petal.Length': 'Petal_Length',
'Petal.Width': 'Petal_Width'},
inplace=True)

print(df_subset.head(3))

model = smf.logit('Species ~ Petal_Length + Petal_Width', data=df_subset)
result = model.fit()
print(result.summary())

print(result.get_margeff().summary())

df_new = pd.DataFrame({'Petal_Length': np.random.randn(20)*0.5 + 5,
'Petal_Width': np.random.randn(20)*0.5 + 1.7})
df_new['P-Species'] = result.predict(df_new)

print(df_new['P-Species'].head(3))
df_new['Species'] = (df_new['P-Species'] > 0.5).astype(int)

params = result.params
alpha0 = -params['Intercept'] / params['Petal_Width']
alpha1 = -params['Petal_Length'] / params['Petal_Width']

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
# Species virginica
ax.plot(df_subset[df_subset.Species == 0].Petal_Length.values, df_subset[df_subset.Species == 0].Petal_Width.values, 's', label='virginica')
ax.plot(df_new[df_new.Species == 0].Petal_Length.values, df_new[df_new.Species == 0].Petal_Width.values, 'o', markersize=10, color='steelblue', label='virginica(pred.)')

# Species versicolor
ax.plot(df_subset[df_subset.Species == 1].Petal_Length.values, df_subset[df_subset.Species == 1].Petal_Width.values, 's', label='versicoolor')
ax.plot(df_new[df_new.Species == 1].Petal_Length.values, df_new[df_new.Species == 1].Petal_Width.values, 'o', markersize=10, color='green', label='versicolor(pred.)')

# Boundary line
_x = np.array([4.0, 6.1])
ax.plot(_x, alpha0 + alpha1 * _x, 'k')
ax.set_xlabel('Petal length')
ax.set_ylabel('Petal width')
ax.legend()
plt.show()