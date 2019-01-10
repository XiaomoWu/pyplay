import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'a': [1, 0], 'b': [3, 4]})
df.all()
df.any()
df.isnull().all()

df.a
df['c'] = 111
df.d = 222
df