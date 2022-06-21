#!/usr/bin/env python
# coding: utf-8

# (reshape-pd)=
# # 4. Reshape with pandas
# 
# This lesson is going to cover some basic ways that pandas can help you reshape your `DataFrame`. If you work frequently with Excel and VBA, these functions might look pretty familiar.
# 
# ## Exploding! 
# 
# One helpful way to reshape your `DataFrame` is through the pandas function `explode()`. This function "explodes" or expands each element of a list to a row, replicating the index values.
# 
# ```{admonition} New function
# [`df.explode()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html): Transform each element of a list-like to a row, replicating index values.
# ```
# 
# Let's look at the example below. In this example, we have a `DataFrame` with two columns, `item_identifier` and `committee_member`.  The `committee_member` column contains lists of committee members for each thesis. 
# 
# If we wanted to evaluate the names individually, but don't want to lose their relationship to the item identifiers, `explode()` is a great option.
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download sampleDataCommitteeMembers.csv here<./sampleDataCommitteeMembers.csv>`.
# ```
# 
# **sampleDataCommitteeMembers (not exploded)**
# 
# | item_identifier | committee_member                                             |
# | :-------------- | :----------------------------------------------------------- |
# | thesis_001      | Leung, Anthony K. L.\|Matunis, Michael J.\|Dinglasan, Rhoel R.\|Goodlett, David |
# | thesis_002      | Leek, Jeffrey T.\|Hansen, Kasper D.\|Battle, Alexis\|Jaffe, Andrew |
# | thesis_003      | West, Keith P., Jr.\|Talegawkar, Sameera\|Fanzo, Jessica C.  |
# | thesis_004      | Kass, Nancy E.\|Saloner, Brendan\|Bodurtha, Joann N.\|Taylor, Holly A. |
# 
# ```{toggle} Click to see the exploded DataFrame!
# 
# **sampleDataCommitteeMembers (exploded)**
# 
# | item_identifier | committee_member     |
# | :-------------- | :------------------- |
# | thesis_001      | Leung, Anthony K. L. |
# | thesis_001      | Matunis, Michael J.  |
# | thesis_001      | Dinglasan, Rhoel R.  |
# | thesis_001      | Goodlett, David      |
# | thesis_002      | Leek, Jeffrey T.     |
# | thesis_002      | Hansen, Kasper D.    |
# | thesis_002      | Battle, Alexis       |
# | thesis_002      | Jaffe, Andrew        |
# | thesis_003      | West, Keith P., Jr.  |
# | thesis_003      | Talegawkar, Sameera  |
# | thesis_003      | Fanzo, Jessica C.    |
# | thesis_004      | Kass, Nancy E.       |
# | thesis_004      | Saloner, Brendan     |
# | thesis_004      | Bodurtha, Joann N.   |
# | thesis_004      | Taylor, Holly A.     |
# 
# ```
# 
# Let's explore the code that makes this possible.

# In[1]:


import pandas as pd

filename = 'sampleDataCommitteeMembers.csv'
df = pd.read_csv(filename, header=0)

df['committee_member'] = df['committee_member'].str.split('|')
df = df.explode('committee_member')

print(df.head())
df.to_csv('explodedSampleDataCommitteeMembers.csv', index=False)


# First, we read our `DataFrame` as the variable `df`. 
# 
# Next, we read converted the strings in the `committee_member` `Series` into Python lists using the `Series.str.split()` function.
# 
# ```{admonition} New function
# [`Series.str.split()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html): Splits string into a list around given separator/delimiter.
# ```
# Once Python understands our `committee_member` `Series` values as lists, we use the pandas function `explode()` to expand each element of a list to a row while keeping the element associated with the list's original identifier.
# 
# Finally, we printed a sample of the exploded DataFrame and saved it as a CSV called explodedSampleDataCommitteeMembers.csv.
# 
# ## Pivot!
# 
# Before pandas, I had no conceptualization of what pivoting meant. How could you pivot a table? Are you turning it? What is going on? 
# 
# In this section, we are going to cover two different types of pivot functions offered by pandas and how they can help you reshape your `DataFrame`.
# 
# ### `pivot()`
# 
# First, let's talk about the pandas `pivot()` function, which provides general purpose pivoting for your `DataFrame`.
# 
# ```{admonition} New function
# [`pivot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html): Reshape data (produce a “pivot” table) based on column values.</a>
# ```
# 
# Because `pivot()` has so much flexbility in how it can reshape your `DataFrame`, I find it helpful to think about what pivot can do rather than focus on a definition.
# 
# - `pivot()` can transform *`Series` values* → *`Series` headers/labels*
# - `pivot()` can change what values acts as the `DataFrame` index
# - `pivot()` can select what `Series` values will populate the pivoted `DataFrame`
# 
# Let's use the example below. Let's say you want to restructure your spreadsheet so you can easily view the theses by year. You can use the three `pivot()` parameters of `columns`, `index` and `values` to: 
# 
# 1. Organize the `DataFrame` by year
# 2. Use item_identifier as the index
# 3. Fill the `DataFrame` with title values
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download sampleDataYear.csv here<./sampleDataYear.csv>`.
# ```
# 
# Written as code, this means we want our `pivot()` function to look like this:
# 
# ```python
# pivot = df.pivot(index='item_identifier', columns='year', values='title')
# ```
# 
# **sampleDataYear (not pivoted)**
# 
# | item_identifier    | year | title                                                        | degree_grantor                                              |
# | ---------- | ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
# | thesis_001 | 2015 | Characterization of the ADP-ribosylated proteome by mass spectrometry | Johns Hopkins University. Bloomberg School of Public Health |
# | thesis_002 | 2016 | Annotation-Agnostic Differential Expression and Binding Analyses | Johns Hopkins University. Bloomberg School of Public Health |
# | thesis_003 | 2016 | Child diet over three seasons in rural Zambia: Assessments of usual nutrient intake adequacy, components of intake variation and dietary diversity score performance | Johns Hopkins University. Bloomberg School of Public Health |
# | thesis_004 | 2017 | Exploring Parental Involvement in Rare Disease Research and Advocacy | Johns Hopkins University. Bloomberg School of Public Health |
# 
# Here's what our new `DataFrame` will look like. As you can see, the years are now acting as the Series labels, the item_identifiers are serving as the index, and values of title have been filled in where applicable. 
# 
# ```{toggle} Click to see the pivoted DataFrame!
# **sampleDataYear (pivoted)**
# 
# | item_identifier | 2013 | 2014 | 2015                                                         | 2016                                                         | 2017                                                         | 2018 | 2019 | 2020 | 2021 |
# | --------------- | ---- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- | ---- | ---- | ---- |
# | thesis_001      |      |      | Characterization of the ADP-ribosylated proteome by mass spectrometry |                                                              |                                                              |      |      |      |      |
# | thesis_002      |      |      |                                                              | Annotation-Agnostic Differential Expression and Binding Analyses |                                                              |      |      |      |      |
# | thesis_003      |      |      |                                                              | Child diet over three seasons in rural Zambia: Assessments of usual nutrient intake adequacy, components of intake variation and dietary diversity score performance |                                                              |      |      |      |      |
# | thesis_004      |      |      |                                                              |                                                              | Exploring Parental Involvement in Rare Disease Research and Advocacy |      |      |      |      |
# ```
# You'll notice that we lost some information doing this pivot -- we no longer have the degree_grantor information. That's because we only selected the title `Series` to fill in our `DataFrame`. We could select more columns, but then we will get hierarchical columns within our `DataFrame`. We won't get into hierarchical columns in this lesson (or ever, honestly, they are horrible), but it's another fun layer of complexity to explore if you want.
# 
# Let's explore the code that makes this possible.

# In[2]:


import pandas as pd

filename = 'sampleDataYear.csv'
df = pd.read_csv(filename, header=0)

df_p = df.pivot(index='item_identifier', columns='year', values='title')
print(df_p.head())

df_p.to_csv('sampleDataYearPivoted.csv')


# First, we read our `DataFrame` as the variable `df`. Next, we pivoted `df` and created a variable `df_p` to represent our pivoted `DataFrame`. We printed out a sample of `df_p` and then created a CSV of `df_p` called sampleDataYearPivoted.csv.
# 
# ### `pivot_table()`
# 
# To make this even more fun, pandas has a related function called `pivot_table()` which is basically a specific-type of `pivot()` that can aggregate values together according to specified functions. 
# 
# ```{admonition} New function
# [`pd.pivot_table()`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html): Create a spreadsheet-style pivot table as a DataFrame.</a>
# ```
# Because that's quite a mouthful, here's a more casual way to think about the differences:
# 
# ````{panels}
# `pivot()`
# ^^^
# - reshapes a `DataFrame`
# 
# ---
# 
# `pivot_table()` 
# ^^^
# - reshapes a `DataFrame`
# - squishes or aggregates values together if needed
# 
# ````
# The `pivot_table()` function has 10 parameters, 4 of which we are going to focus on here. Some will look familiar from `pivot()`.
# 
# - `data`: the `DataFrame` to pivot
# - `values`: column to aggregate
# - `index `: column that will act as the index
# - `aggfunc`: the function applied to values
# 
# So let's take a look at explodedSampleDataCommitteeMembers.csv, which we created through the melt function earlier. What if we wanted a list of all the unique `committee_members` with all of their associated `item_identifiers`? With `pivot_table()`, we can easily reshape the spreadsheet to create a new view of the data.
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download explodedSampleDataCommitteeMembers.csv here<./explodedSampleDataCommitteeMembers.csv>`.
# ```
# 
# **explodedSampleDataCommitteeMembers (not pivoted)**
# 
# | item_identifier | committee_member     |
# | :-------------- | :------------------- |
# | thesis_001      | Leung, Anthony K. L. |
# | thesis_001      | Matunis, Michael J.  |
# | thesis_001      | Dinglasan, Rhoel R.  |
# | thesis_001      | Goodlett, David      |
# | thesis_002      | Leek, Jeffrey T.     |
# | thesis_002      | Hansen, Kasper D.    |
# | thesis_002      | Battle, Alexis       |
# | thesis_002      | Jaffe, Andrew        |
# | thesis_003      | West, Keith P., Jr.  |
# | thesis_003      | Talegawkar, Sameera  |
# | thesis_003      | Fanzo, Jessica C.    |
# | thesis_004      | Kass, Nancy E.       |
# | thesis_004      | Saloner, Brendan     |
# | thesis_004      | Bodurtha, Joann N.   |
# | thesis_004      | Taylor, Holly A.     |
# 
# ```{toggle} Click to see the pivoted DataFrame!
# **explodedSampleDataCommitteeMembers (pivoted)**
# 
# | committee_member     | item_identifier                                |
# | :------------------- | :--------------------------------------------- |
# | Achinstein, Sharon   | thesis_036                                     |
# | Allan, Bentley B.    | thesis_019                                     |
# | Angelini, Alessandro | thesis_049                                     |
# | Arora, Raman         | thesis_087\|thesis_087                         |
# | Athreya, Avanti      | thesis_072                                     |
# | Bah, Ibrahima        | thesis_038                                     |
# | Basu, Amitabh        | thesis_038\|thesis_050\|thesis_083\|thesis_086 |
# ```
# 
# Here's a type of `pivot_table()` I use all the time, which aggregates string values together into a single column using `lambda` and `join()`.
# 
# ```python
# pivot = pd.pivot_table(df, index='committee_member',
#                        values='item_identifier',
#                        aggfunc=lambda x: '|'.join(str(v) for v in x))
# ```
# 
# Let's explore the code that makes this possible.

# In[3]:


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


# #### What is lambda?
# 
# ```{admonition} New function
# [`lambda`](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions): An anonymous (unnamed) function that applies arguments to various parameters and returns an expression (outcome).
# ```
# 
# Let's take a closer look at what lambda is doing in the example above. In particular, let's look at the line below.
# 
#     
# ```python
# lambda x: '|'.join(str(v) for v in x)
# ```
# 
# This line of code is essentially a small function to transform a list into a string. In plain language, this function says:
# ```
#     For a list named x:
#         Loop through x and convert individual list components (named v) into strings
#         Convert list x into one string with components separated by '|' (pipes)
# ```    
#     
# If we wrote it out it as a regular function, it would look like this:
# 
# ```python
# def lambda(x):  
#    new_x = []
#    for v in x:
#     v = str(v)
#     new_x.append(v)
#   '|'.join(new_x)
#   x = new_x
#   return x
# ```
# We can also imagine it as a list comprehension. 
# 
# ```python
# x = [str(v) for v in x]
# ```
# 
# ## Melting!
# 
# Another great way to reshape a `DataFrame` is through the `melt()` function. This function (which serves as a type of un-pivoting) changes your `DataFrame` from a "wide" to "long" format, reducing your `DataFrame` to only two non-identifier columns: a *variable* column and a *value* column. 
# 
# ```{admonition} New function    
# [`melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html): Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.
# ```
# 
# (For Linked Data geeks: Maybe this is nonsense, but I find it helpful to visualize a melted `DataFrame` as "What if each row in my spreadsheet was a triple?" )
# 
# It's easiest to understand this through an example.
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download marylandPlaces.csv here<./marylandPlaces.csv>`.
# ```
# 
# **marylandPlaces (not melted)**
# 
# | local_identifier | name                | fast                                | geonames                         | viaf                           |
# | ---------------- | ------------------- | ----------------------------------- | -------------------------------- | ------------------------------ |
# | geo_001          | Maryland            | http://id.worldcat.org/fast/1204739 | http://sws.geonames.org/4361885/ | http://viaf.org/viaf/151255387 |
# | geo_002          | Maryland--Annapolis | http://id.worldcat.org/fast/1206088 | http://sws.geonames.org/4347242/ | http://viaf.org/viaf/123791303 |
# | geo_003          | Maryland--Baltimore | http://id.worldcat.org/fast/1204292 | http://sws.geonames.org/4347778/ | http://viaf.org/viaf/235452840 |
# 
# ```{toggle} Click to see the melted DataFrame!
# **marylandPlaces (melted)**
# 
# | local_identifier | variable | value                               |
# | ---------------- | -------- | ----------------------------------- |
# | geo_001          | name     | Maryland                            |
# | geo_001          | fast     | http://id.worldcat.org/fast/1204739 |
# | geo_001          | geonames | http://sws.geonames.org/4361885/    |
# | geo_001          | viaf     | http://viaf.org/viaf/151255387      |
# | geo_002          | name     | Maryland--Annapolis                 |
# | geo_002          | fast     | http://id.worldcat.org/fast/1206088 |
# | geo_002          | geonames | http://sws.geonames.org/4347242/    |
# | geo_002          | viaf     | http://viaf.org/viaf/123791303      |
# | geo_003          | name     | Maryland--Baltimore                 |
# | geo_003          | fast     | http://id.worldcat.org/fast/1204292 |
# | geo_003          | geonames | http://sws.geonames.org/4347778/    |
# | geo_003          | viaf     | http://viaf.org/viaf/235452840      |
# ```
# 
# Let's explore the code that makes this possible.

# In[4]:


import pandas as pd

filename = 'marylandPlaces.csv'
df_1 = pd.read_csv(filename, header=0)

df_1 = df_1.melt(id_vars=['local_identifier'])
print(df_1.head())

df_1.to_csv('meltedMarylandPlaces.csv')


# In[ ]:




