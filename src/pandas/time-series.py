import pandas as pd
import numpy as np

date_range = pd.date_range('2015-1-1', periods=31)
print(date_range)

date_range1 = pd.date_range('2015-1-1 00:00', '2015-1-1 12:00', freq='H')
print(date_range1)

ts1 = pd.Series(np.arange(31), index=pd.date_range('2015-1-1', periods=31))
print(ts1.head())