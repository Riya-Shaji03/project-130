import pandas as pd

df=pd.read_csv('total_stars.csv')

#print(df)
#print(df.columns)
'''
del df['Luminosity']
del df['Star_name.1']
del df['Distance.1']
del df['Mass.1']
del df['Radius.1']
'''
df.drop(['Luminosity','Star_name.1','Mass.1','Radius.1','Distance.1','Unnamed: 0','Unnamed: 5'],axis=1, inplace=True)
print(df)

change=df.dropna()
change.reset_index(drop=True,inplace=True)
change.to_csv('main.csv')

print(change.dtypes)
print(change.head(5))
print(change.describe())
print(change.info())
