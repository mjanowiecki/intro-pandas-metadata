#!/usr/bin/env python
# coding: utf-8

# (merging-pd)=
# # 3. Merge with pandas
# 
# Pandas has a lot of helpful ways to merge spreadsheets based on identifiers. In this lesson, we are going to learn how to use the pandas function `merge()` and the four basic merge types:
# 
# - left
# - right
# - outer
# - inner 
# 
# ```{admonition} New function
# [`pd.merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html): Merge DataFrame or named Series objects with a database-style join.</a>
# ```
# 
# ## Types of merges
# 
# First, let's talk about the type of merges. I find it really helpful to visualize the different types of merges, so we are going to discuss the four different types through examples. In these examples, we will merge two `DataFrames` that we are calling `frame_1` (the left frame) and `frame_2` (the right frame) using the four main types of merges: left, right, outer, and inner.
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download frame_1.csv here<./frame_1.csv>`.<br>
# You can {Download}`download frame_2.csv here<./frame_2.csv>`.
# ```
# 
# ```{attention}
# For now, we are just going to focus on the concepts and leave the coding for later in the lesson.
# ```
# 
# In pandas merges, which mimic traditional database merges in SQL, there will be a spreadsheet (or `DataFrame`) we consider the "left" frame and a spreadsheet that we consider the "right" frame. 
# 
# Selecting a frame to be "right" or "left" is arbitrary, we just have to be consistent as we consider our merges. 
# 
# `frame_1` (the left frame)
# 
# |title                                                                           | subject_id  | 
# |:-------------------------------------------------------------------------------|:------------|
# |Overcoming Data Challenges in Machine Translation                               | subject_001 |
# |Experimental Methods Towards Controlling the Glycoform                          | subject_002 |
# |Interactions of DNA Polymerase Theta and Ku70/80 with Oxidative DNA Damage      | subject_003 |
# |Control and Learning of Dynamics in Human Movement                              | subject_004 |
# |Local Public Health Performance and its Impact on Population Health             | subject_005 |
# |THz and microwave spectroscopy on strongly correlated conductors                | subject_007 |
# |Subjectivity in Flux: Youth in Latin American and Latino Literature             | subject_009 |
# 
# `frame_2` (the right frame)
# 
# | subject_id  | subject              |
# | :---------- | :--------------------|
# | subject_001 | Machine learning     |
# | subject_002 | Biochemistry         |
# | subject_003 | DNA polymerases      |
# | subject_004 | Dynamics             |
# | subject_006 | Surgical emergencies |
# | subject_007 | Superconductivity    |
# | subject_008 | Social conditions    |
# 
# ### Left merge
# 
# A left merge only uses keys (i.e. identifiers) from the left frame. Similar to a SQL left outer join. What identifiers will be in the merged `DataFrame`?

# ```{toggle}
# In other words, the left merge only matches on the identifiers found in the left frame:
# 
# - subject_001
# - subject_002
# - subject_003
# - subject_004
# - subject_005
# - subject_007
# - subject_009
# 
# Here's the frames merged together using a left merge.
# 
# | title                                                        | subject_id  | subject           |
# | :----------------------------------------------------------- | :---------- | :---------------- |
# | Overcoming Data Challenges in Machine Translation            | subject_001 | Machine learning  |
# | Experimental Methods Towards Controlling the Glycoform       | subject_002 | Biochemistry      |
# | Interactions of DNA Polymerase Theta and Ku70/80 with Oxidative DNA Damage | subject_003 | DNA polymerases   |
# | Control and Learning of Dynamics in Human Movement           | subject_004 | Dynamics          |
# | Local Public Health Performance and its Impact on Population Health | subject_005 |                   |
# | THz and microwave spectroscopy on strongly correlated conductors | subject_007 | Superconductivity |
# | Subjectivity in Flux: Youth in Latin American and Latino Literature | subject_009 |                   |
# ```

# ### Right merge
# 
# A right merge only uses keys (i.e. identifiers) from the right frame. Similar to a SQL right outer join. What identifiers will be in the merged `DataFrame`?

# ```{toggle}
# In other words, the right merge only matches on the identifiers found in the right frame:
# 
# - subject_001
# - subject_002
# - subject_003
# - subject_004
# - subject_006
# - subject_007
# - subject_008
# 
# Here's the frames merged together using a right merge.
# 
# | title                                                        | subject_id  | subject              |
# | ------------------------------------------------------------ | ----------- | -------------------- |
# | Overcoming Data Challenges in Machine Translation            | subject_001 | Machine learning     |
# | Experimental Methods Towards Controlling the Glycoform       | subject_002 | Biochemistry         |
# | Interactions of DNA Polymerase Theta and Ku70/80 with Oxidative DNA Damage | subject_003 | DNA polymerases      |
# | Control and Learning of Dynamics in Human Movement           | subject_004 | Dynamics             |
# |                                                              | subject_006 | Surgical emergencies |
# | THz and microwave spectroscopy on strongly correlated conductors | subject_007 | Superconductivity    |
# |                                                              | subject_008 | Social conditions    |
# ```

# ### Outer merge
# 
# An outer merge uses union of keys from both frames. Similar to a SQL full outer join. In other words, the outer merge combines information from all identifiers in the frames. What identifiers will be in the merged `DataFrame`?

# ```{toggle}
# All of them!
# 
# - subject_001
# - subject_002
# - subject_003
# - subject_004
# - subject_005
# - subject_006
# - subject_007
# - subject_008
# - subject_009
# 
# Here's the frames merged together using an outer merge.
# 
# | title                                                        | subject_id  | subject              |
# | :----------------------------------------------------------- | :---------- | :------------------- |
# | Overcoming Data Challenges in Machine Translation            | subject_001 | Machine learning     |
# | Experimental Methods Towards Controlling the Glycoform       | subject_002 | Biochemistry         |
# | Interactions of DNA Polymerase Theta and Ku70/80 with Oxidative DNA Damage | subject_003 | DNA polymerases      |
# | Control and Learning of Dynamics in Human Movement           | subject_004 | Dynamics             |
# | Local Public Health Performance and its Impact on Population Health | subject_005 |                      |
# | THz and microwave spectroscopy on strongly correlated conductors | subject_007 | Superconductivity    |
# | Subjectivity in Flux: Youth in Latin American and Latino Literature | subject_009 |                      |
# |                                                              | subject_006 | Surgical emergencies |
# |                                                              | subject_008 | Social conditions    |
# ```

# ### Inner merge
# 
# An inner merge uses intersection of keys from both frames. Similar to a SQL inner join. In other words, the inner merge only matches on the identifiers found in **both** frames. What identifiers will be in the merged `DataFrame`?

# ```{toggle}
# - subject_001
# - subject_002
# - subject_003
# - subject_004
# - subject_007
# 
# Here's the frames merged together using an inner merge.
# 
# | title                                                        | subject_id  | subject           |
# | :----------------------------------------------------------- | :---------- | :---------------- |
# | Overcoming Data Challenges in Machine Translation            | subject_001 | Machine learning  |
# | Experimental Methods Towards Controlling the Glycoform       | subject_002 | Biochemistry      |
# | Interactions of DNA Polymerase Theta and Ku70/80 with Oxidative DNA Damage | subject_003 | DNA polymerases   |
# | Control and Learning of Dynamics in Human Movement           | subject_004 | Dynamics          |
# | THz and microwave spectroscopy on strongly correlated conductors | subject_007 | Superconductivity |
# ```

# Here's another way to visual these types of merges:
# 
# <img src="https://gitlab.com/mjanowiecki/python-lessons-for-librarians/-/raw/main/img/mergeTypes.png" alt="visual of merges as venn diagrams" width="450"/>

# ## Repeating keys and merges
# 
# Here's a fun question. What happens during a merge when a key appears more than once in a `DataFrame`?
# 
# Let's find out by merging on `department_id` for these two example `DataFrames`. 
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download frame_3.csv here<./frame_3.csv>`.<br>
# You can {Download}`download frame_4.csv here<./frame_4.csv>`.
# ```
# 
# `frame_3` (the left frame)
# 
# | local_id   | name           | department_id  |
# | :--------- | :------------- | :------------- |
# | person_001 | Ahuja, Allie   | department_003 |
# | person_002 | Petrov, Stella | department_003 |
# | person_003 | Chen, Rachel   | department_002 |
# | person_004 | Smith, Amber   | department_004 |
# 
# `frame_4` (the right frame)
# 
# | department_id  | department_name      | school                          |
# |:-------------- | :------------------- |:--------------------------------|
# | department_001 | Cognitive Science    |Krieger School of Arts & Sciences|
# | department_002 | Near Eastern Studies |Krieger School of Arts & Sciences|
# | department_003 | English              |Krieger School of Arts & Sciences|
# | department_004 | Public Health        |Bloomberg School of Public Health|
# 
# ### Left merge
# 
# In the left merge, the identifiers from `frame_3`  (department_003, department_003, department_002, department_004) are all matched, in order, with the information from `frame_4`.
# 
# | local_id   | name           | department_id  | department_name      | school                            |
# |:-----------|:-------------- | :------------- | :------------------- | :-------------------------------- |
# | person_001 | Ahuja, Allie   | department_003 | English              | Krieger School of Arts & Sciences |
# | person_002 | Petrov, Stella | department_003 | English              | Krieger School of Arts & Sciences |
# | person_003 | Chen, Rachel   | department_002 | Near Eastern Studies | Krieger School of Arts & Sciences |
# | person_004 | Smith, Amber   | department_004 | Public Health        | Bloomberg School of Public Health |
# 
# ### Right merge
# 
# In the right merge, the identifiers from `frame_4`  (department_001, department_002, department_003, department_004) are all matched, in order, with the information from `frame_3`. However, you'll notice that department_003 repeats here too, to capture both of the matches of department_003 in `frame_3`.
# 
# | local_id   | name           | department_id  | department_name      | school                            |
# | :--------- | :------------- | :------------- | :------------------- | :-------------------------------- |
# |            |                | department_001 | Cognitive Science    | Krieger School of Arts & Sciences |
# | person_003 | Chen, Rachel   | department_002 | Near Eastern Studies | Krieger School of Arts & Sciences |
# | person_001 | Ahuja, Allie   | department_003 | English              | Krieger School of Arts & Sciences |
# | person_002 | Petrov, Stella | department_003 | English              | Krieger School of Arts & Sciences |
# | person_004 | Smith, Amber   | department_004 | Public Health        | Bloomberg School of Public Health |
# 
# ### Outer merge
# 
# In the outer merge, the identifiers from `frame_3` (department_003, department_003, department_002, department_004) are all matched, in order, with the information from `frame_4`. Then, the remaining identifier from `frame_4` (department_001) is added to spreadsheet but doesn't match with anything.
# 
# | local_id   | name           | department_id  | department_name      | school                            |
# | :--------- | :------------- | :------------- | :------------------- | :-------------------------------- |
# | person_001 | Ahuja, Allie   | department_003 | English              | Krieger School of Arts & Sciences |
# | person_002 | Petrov, Stella | department_003 | English              | Krieger School of Arts & Sciences |
# | person_003 | Chen, Rachel   | department_002 | Near Eastern Studies | Krieger School of Arts & Sciences |
# | person_004 | Smith, Amber   | department_004 | Public Health        | Bloomberg School of Public Health |
# |            |                | department_001 | Cognitive Science    | Krieger School of Arts & Sciences |
# 
# ### Inner merge
# 
# In the inner merge,  the identifiers found in both `frame_3` and `frame_4` are matched together. This happens to be the same results as the left merge.
# 
# | local_id   | name           | department_id  | department_name      | school                            |
# | :--------- | :------------- | :------------- | :------------------- | :-------------------------------- |
# | person_001 | Ahuja, Allie   | department_003 | English              | Krieger School of Arts & Sciences |
# | person_002 | Petrov, Stella | department_003 | English              | Krieger School of Arts & Sciences |
# | person_003 | Chen, Rachel   | department_002 | Near Eastern Studies | Krieger School of Arts & Sciences |
# | person_004 | Smith, Amber   | department_004 | Public Health        | Bloomberg School of Public Health |
# 

# ## Trying a merge
# 
# Let's try a merge using pandas. For this exercise, we are going to use the `sampleData_cleaned.csv` that we cleaned up previously and a spreadsheet with name authority URIs for the different Hopkins schools called `schoolURIs.csv`.
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download sampleData_cleaned.csv here<./sampleData_cleaned.csv>`.<br>
# You can {Download}`download schoolURIs.csv here<./schoolURIs.csv>`.
# ```
# 
# | degree_grantor      | viaf             | lcnaf                                            |
# | :------------------| :---------------| :----------------------------------------------- |
# | Johns Hopkins University. School of Medicine  | http://viaf.org/viaf/124344829   | http://id.loc.gov/authorities/names/n81070677    |
# | Johns Hopkins University. Krieger School of Arts and Sciences | http://viaf.org/viaf/130409033 | http://id.loc.gov/authorities/names/n2007184404  |
# | Johns Hopkins University. Whiting School of Engineering      | http://viaf.org/viaf/4816164191747718740000 | http://id.loc.gov/authorities/names/no2022000309 |
# | Johns Hopkins University. Bloomberg School of Public Health  | http://viaf.org/viaf/142356070              | http://id.loc.gov/authorities/names/nr2001039005 |
# 
# ### Deciding on the type of merge
# 
# First, lets decide on the type of merge. If we want a spreadsheet that has all of the information from `sampleData_cleaned` with the additional location details from `schoolURIs`, what type of merge should we do? What identifier should we use?
# 
# If we treat `sampleData_cleaned` as the left frame and `schoolURIs` as the right frame, we should do a **left merge** using the `degree_grantor` as the key.
# 
# Why is this the best option? Let's think through the results of the other merging options.
# 
# **Right merge**: If there are identifiers in the right frame that aren't in the left frame, a right merge would *include* them and their associated data. However, we don't need this data to meet our goal. Moreover, if there are identifiers in the left frame that aren't in the right frame, an right merge would *exclude* them. Since we want to keep all of the data from `sampleData_cleaned`,  this isn't a good option.
# 
# **Outer merge**: If there are identifiers in the right frame that aren't in the left frame, an outer merge would *include* them  and their associated data. However, we don't need this data to meet our goal. 
# 
# **Inner merge**:  If there are identifiers in the left frame that aren't in the right frame, an inner merge would *exclude* them. However, we want to keep all of the data from `sampleData_cleaned` so this isn't a good option.
# 
# ### Writing the code
# 
# Let's look more closely at the `merge()` function. The first two parameters are the left and rights objects to merge; this is where we want to put our `DataFrames`. The next parameter is the `how` parameter, and this is where we indicate what type of merge we want (`"left"`, `"right"`, `"inner"`, or `"outer"`). We want `how="left"` for this merge. 
# 
# Next, we need to use the `on` parameter to tell the function what identifier (aka column/Series) we want to merge on. We need to set this to `degree_grantor`.  
# 
# Finally, lets set the suffixes. These are suffixes like `_x` and `_y` that are added to your column names if you have matching column names in your two `DataFrames`. So, if you have a `Name` column in `df_1` and a `Name` column in `df_2`, the merged `DataFrame` will have columns named `Name_x` and `Name_y`. I like to set these suffixes as `_1` and `_2`.
# 
# Great! Now let's create a new CSV with our merged data.

# In[1]:


import pandas as pd

df_1 = pd.read_csv('sampleData_cleaned.csv')
df_2 = pd.read_csv('schoolURIs.csv')

merged = pd.merge(df_1, df_2, how="left", on="degree_grantor")
print(merged.head())

merged.to_csv('sampleData_cleaned2.csv', index=False)

