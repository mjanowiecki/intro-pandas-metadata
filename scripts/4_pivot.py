import pandas as pd

filename = 'sampleDataYear.csv'
df = pd.read_csv(filename, header=0)

df_p = df.pivot(index='item_identifier', columns='year', values='title')
print(df_p.head)

df_p.to_csv('sampleDataYearPivoted.csv')
