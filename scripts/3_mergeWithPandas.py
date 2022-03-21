import pandas as pd

df_1 = pd.read_csv('sampleData_cleaned.csv')
df_2 = pd.read_csv('schoolURIs.csv')

merged = pd.merge(df_1, df_2, how="left", on="degree_grantor")
print(merged.head())

merged.to_csv('sampleData_cleaned2.csv', index=False)
