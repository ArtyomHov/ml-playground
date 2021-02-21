import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sns.set(style='darkgrid')
import os
cwd = os.path.dirname(os.path.abspath(__file__))
outdoor_file = os.path.join(cwd, 'temperature_outdoor_2014.tsv')
indoor_file = os.path.join(cwd, 'temperature_indoor_2014.tsv')


df1 = pd.read_csv(outdoor_file, delimiter='\t', names=['time', 'outdoor'])
df1.time = (pd.to_datetime(df1.time.values, unit='s').tz_localize('UTC').tz_convert('Europe/Stockholm'))
df1 = df1.set_index('time').resample('10min').mean()

df2 = pd.read_csv(indoor_file, delimiter='\t', names=['time', 'indoor'])
df2.time = (pd.to_datetime(df2.time.values, unit='s').tz_localize('UTC').tz_convert('Europe/Stockholm'))
df2 = df2.set_index('time').resample('10min').mean()
df_temp = pd.concat([df1, df2], axis=1)
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
df_temp.resample('D').mean().plot(y=['outdoor', 'indoor'], ax=ax)
plt.show()

sns.distplot(df_temp.to_period('M')['outdoor']['2014-04'].dropna().values, bins=50)
sns.distplot(df_temp.to_period('M')['indoor']['2014-04'].dropna().values, bins=50)
plt.show()

sns.kdeplot(df_temp.resample('H').mean()['outdoor'].dropna().values,df_temp.resample('H').mean()['indoor'].dropna().values, shade=False)
with sns.axes_style('white'):
    sns.jointplot(df_temp.resample('H').mean()['outdoor'].values, df_temp.resample('H').mean()['indoor'].values, kind='hex')
plt.show()

df_temp['month'] = df_temp.index.month
df_temp['hour'] = df_temp.index.hour
table = pd.pivot_table(df_temp, values='outdoor', index=['month'], columns=['hour'], aggfunc=np.mean)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
sns.heatmap(table, ax=ax)
plt.show()