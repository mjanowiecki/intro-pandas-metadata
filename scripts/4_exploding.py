import pandas as pd

filename = 'sampleDataCommitteeMembers.csv'
df = pd.read_csv(filename, header=0)

df['committee_member'] = df['committee_member'].str.split('|')
df = df.explode('committee_member')

print(df.head())
df.to_csv('explodedSampleDataCommitteeMembers.csv', index=False)
