import pandas as pd
import matplotlib.pyplot as plt
import os
cwd = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(cwd, 'european_cities.csv')

df_pop = pd.read_csv(csv_file, delimiter = ',', encoding='utf-8', header=0)

print(df_pop.info())
print(df_pop.head())

df_pop['NumericPopulation'] = df_pop.Population.apply(lambda x: int(x.replace(',', '')))
states = df_pop['State'].values[:3] #contains extra white spaces
print(states)
df_pop['State'] = df_pop['State'].apply(lambda x: x.strip())
print(df_pop.head())
print(df_pop.dtypes)

df_pop2 = df_pop.set_index('City')
df_pop2 = df_pop2.sort_index()
print(df_pop2.head())

df_pop3 = df_pop.set_index(['State', 'City']).sort_index(level=0)
print(df_pop3.head(7))

df_pop.set_index('City').sort_values(['State', "NumericPopulation"], ascending=[False, True]).head()
print(df_pop)

city_counts = df_pop.State.value_counts()
print(city_counts.head())

df_pop3 = df_pop[["State", "City", "NumericPopulation"]].set_index(["State", "City"])
df_pop4 = df_pop3.sum(level="State").sort_values("NumericPopulation", ascending=False)
print(df_pop4.head())

df_pop5 = (df_pop.drop("Rank", axis=1).groupby("State").sum().sort_values("NumericPopulation", ascending=False))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
city_counts.plot(kind='barh', ax=ax1)
ax1.set_xlabel('# cities in top 105')
df_pop5.NumericPopulation.plot(kind='barh', ax=ax2)
ax2.set_xlabel("Total pop. in top 105 cities")
plt.show()