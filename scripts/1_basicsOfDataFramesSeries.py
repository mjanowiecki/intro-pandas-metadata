import pandas as pd


filename = 'sampleData.csv'
df = pd.read_csv(filename)
print(df.head())
print(df.tail(12))

print(df.columns)
print(df.shape)
print(df.empty)


row_11 = df.loc[10]
print(row_11)

row_11 = df.iloc[10]
print(row_11)

print(df.iloc[30:41])
print(df.iloc[[0, 30, 60]])

rowsToGrab = [0, 30, 60]
print(df.iloc[rowsToGrab])

degree_discipline = df.degree_discipline
print(degree_discipline)

degree_discipline = df['degree_discipline']
print(degree_discipline)

print(df.loc[9, 'degree_discipline'])

print(df.iloc[9, 5])

print(df.at[9, 'degree_discipline'])
print(df.iat[9, 5])

department_unique = df['degree_department'].unique()
print(department_unique)

unique_list = list(department_unique)
print(unique_list)

department_counts = df['degree_department'].value_counts()
print(department_counts)
