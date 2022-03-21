import pandas as pd
filename = 'sampleData.csv'
df = pd.read_csv(filename)


df = df.dropna(axis=0, how='all')
df = df.dropna(axis=1, how='all')
df = df.drop_duplicates()
df['item_identifier'] = df['item_identifier'].apply(str)
df['item_identifier'] = df['item_identifier'].str.rstrip('.0')
df['item_identifier'] = df['item_identifier'].str.zfill(3)
df['title'] = df['title'].str.strip()

print(df.head)

df.to_csv('sampleData_cleaned.csv', index=False)
