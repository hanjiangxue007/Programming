import pandas as pd
import numpy as np

#create Dataframe:
df = pd.DataFrame({ 'A' : [ 1.0, 2.0, 3.0],
		            'B' : range(3),
		            'C' : np.linspace(1,10,num=3)
		          })
#print(df)
#print(df.dtypes)
#print(df.head(3))
#print(df.index)
#print(df.columns)
#print(df.values)
#print(df.describe())
#print(df.T)
#print(df.sort_index(axis=1, ascending=False))
#print(df.sort_values(by='B'))


#print(df['A'])
#print(df[0:3])
print(df.loc[:,['A','B']])
