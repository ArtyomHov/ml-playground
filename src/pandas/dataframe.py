import pandas as pd

df = pd.DataFrame([
    [909976, 'Sweden'],
    [8615246, 'United Kingdom'],
    [2872086, 'Italy'],
    [2273305, 'France']
])

print(df)

df.index = ['Stockholm', 'London', 'Rome', 'Paris']
df.columns = ['Population', 'State']

print(df)

df1 = pd.DataFrame([
    [909976, 'Sweden'],
    [8615246, 'United Kingdom'],
    [2872086, 'Italy'],
    [2273305, 'France']
], index = ['Stockholm', 'London', 'Rome', 'Paris'],
columns = ['Population', "State"])

print(df1)

df2 = pd.DataFrame({
    'Population': [909976, 8615246, 2872086, 2273305],
    'State': ['Sweden', 'United Kingdom', 'Italy', 'France']
}, index = ['Stockholm', 'London', 'Rome', 'Paris'])

print(df2)

print(df.Population)

print(df.loc['Stockholm'])

print(df.loc[['Paris', 'Rome']])

print(df.mean())

print(df.info())