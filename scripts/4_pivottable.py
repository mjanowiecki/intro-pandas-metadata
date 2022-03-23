import pandas as pd

filename = 'explodedSampleDataCommitteeMembers.csv'
df_1 = pd.read_csv(filename, header=0)
pivot = pd.pivot_table(df_1, index='committee_member',
                       values='item_identifier',
                       aggfunc=lambda x: '|'.join(str(v) for v in x))

df_p = pd.DataFrame(pivot)
df_p = df_p.reset_index()
print(df_p.head())

df_p.to_csv('pivotedByCommitteeMembers.csv', index=False)
