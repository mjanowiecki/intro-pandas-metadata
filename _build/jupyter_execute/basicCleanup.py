#!/usr/bin/env python
# coding: utf-8

# (clean-up)=
# # 2. Clean up with pandas
# 
# 
# ## Drop blank columns or rows
# 
# Someone once asked if I could help clean-up an ArchivesSpace export with approximately 8000 blank rows and 70 blank columns randomly throughout the spreadsheet. Anyways, luckily pandas came to the rescue! 
# 
# In this example, we are first going to drop any blank column or rows from our `sampleData.csv` spreadsheet. First, let's read our CSV as `DataFrame`.
# 

# In[1]:


import pandas as pd
filename = 'sampleData.csv'
df = pd.read_csv(filename)
print(df.head())


# Next, we are going to use a pandas function called `dropna()` to remove the blank columns and rows.
# 
# ```{admonition} New function
# [`df.dropna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html#): Removes missing values from the DataFrame.
# ```
# 
# In pandas, 'na' refers to missing values in a `DataFrame` or `Series.` This includes:
# - blanks (This is the equivalent of a blank cell in a spreadsheet.)
# - `None`
# - `NaN` or `nan` (This means *Not a Number*.)
# 
# 'na'  does not include:
# 
# - `False`
# - `""` (empty strings)
# - 0
# 
# In this script, we are using the function `isna()` to show us which values are 'na'. If the value is 'na', we will see `True` printed. If the value is not 'na', we will see `False` printed. There is also a function called `notna()`which returns the inverse values of `isna()`. 
# 
# ```{admonition} New function
# [`pd.isna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html#pandas.isna): Detects missing values for an array-like object.
# ```
# ```{admonition} New function
# [`pd.notna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.notna.html#pandas.notna): Detects non-missing values for an array-like object.
# ```

# In[2]:


print(df.isna())


# While this is helpful, it doesn't show all of our rows. To see all of our data, let's loop through the rows in our `DataFrame`. To do this, we will use a function called `iterrows()`. For each loop, this function returns the `index` and the `row` as a `Series`. 
# 
# 
# ```{admonition} New function
# [`df.iterrows()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html): Iterates over DataFrame rows as (index, Series) pairs.
# ```

# In[3]:


for index, row in df.iterrows():
    print(row.notna())


# This is more helpful! In the snippet above, we see that `contributor_author` `Series` in rows 0 and 1 are `False` or  doesn't have a value. If we look through the rest of our  results, it seems like the entire `contributor_author` `Series` is empty. We'll want to drop this column. Also, in our terminal results we'll notice that all of the values in row 51 are `False` or empty. We'll want to drop that row as well.
# 
# So in `df.dropna()`, we are asking to drop (or remove) all of empty rows and columns from our `DataFrame`. 
# 
# If you look at the function [guidelines](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html), you can see there are parameters to customize our use of the function. 
# 
# First, we can pick what axis we want to `df.dropna()` from. 
# 
# - `axis=0` refers to the rows
# - `axis=1` refers to the columns/`Series`
# 
# Second, we can decide when we want to drop a row or a column from a `DataFrame`. We can delete a row or column when:
# 
# - `how='any'` (At least one 'na' value is in the column or row.)
# - `thresh=x` (At least *x* number of 'na' are in the column or row.)
# - `how='all'`(All the values in the column or row are 'na'.) 
# 
# Since we want to delete only columns and rows that are **completely** blank or empty, let's run the function twice with the parameter `how='all'`. Once for the blank rows, and once for the blank columns. 

# In[4]:


df = df.dropna(axis=0, how='all')
df = df.dropna(axis=1, how='all')
print(df.head())
print(df.shape)


# Let's check our terminal results. We should have a `DataFrame` with 89 rows and 9 columns.

# ## Drop duplicate rows
# 
# Another common problem in metadata work is duplicate rows. Sometimes, exports will produce duplicated rows and it can be really laborious to remove these manually.
# 
# That's where `drop_duplicates()` comes in. This wonderful little pandas function deletes any rows with the same exact information. 
# 
# ```{admonition} New function
# [`df.drop_duplicates()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html): Removes duplicate rows from DataFrame.
# ```
# 
# But, first let's remind ourselves what our spreadsheet `'sampleData.csv'`currently looks like.
# 

# In[5]:


print(df.head())
print(df.shape)


# Awesome! It currently has 89 rows and 9 columns.
# 
# Ok, let's take care of any duplicates! To start, we will check to see if our spreadsheet has duplicate rows by using the pandas function `duplicate()`. 
# 
# ```{admonition} New function
# [`df.duplicated()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html): Returns boolean Series denoting duplicate rows.
# ```
# 
# This function returns `Series` with the results for each row, identifying any duplicated rows as `True` and any unique rows as `False`.
# 
# Let's try it out. We are setting the parameter `keep` to `False` to mark all duplicated rows, but you can also set this to `"first"` or `"last"` to mark the first or last instance of duplicate row as `True`. 
# 
# Since this function returns a `Series`, we can look the results for all of the rows by looping through the `Series` (we named it `duplicates`) like a simple list using the `enumerate()` function.
# 
# ```{admonition} New function
# [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate): Returns a count (starting from zero) and associated value while iterating through a list-like object.
# ```
# 
# This loop prints the `count` (equivalent to our row index) and then the `row` value of the `Series`. 

# In[6]:


duplicates = df.duplicated(keep=False)
for count, row in enumerate(duplicates):
    print(count, row)


# From this, we can see that row 85 and row 86 are both `True` or duplicated. This means we need to drop one of these rows to get rid of our duplicates.
# 
# If you were especially curious, you could print out these rows to see their values.

# In[7]:


print(df.iloc[85])
print(df.iloc[86])


# Yep, these rows are totally the same! So let's get rid of that pesky extra row using `drop_duplicates()`! 

# In[8]:


df = df.drop_duplicates()

print(df.shape)


# Here you can see that we now have 88 rows, not 89. Hooray!
# 
# ## String handling
# 
# You can also apply different functions to your DataFrame and your `Series` by using string handling. (Here's a [full list](https://pandas.pydata.org/docs/reference/series.html#string-handling) of functions from the API documentation).
# 
# Let's try using the following on our DataFrame.
# 
# ```{admonition} New function
# [`Series.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html): Invoke function on values of Series.
# ```
# ```{admonition} New function
# [`Series.str.rstrip()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rstrip.html): Removes trailing characters.
# ```
# ```{admonition} New function
# [`Series.str.zfill(width)`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html#pandas.Series.str.zfill): Pads strings with zeros.
# ```
# ```{admonition} New function
# [`Series.str.strip()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas.Series.str.strip): Strips whitespaces from strings.
# ```

# In[9]:


print(df['item_identifier'].head())

df['item_identifier'] = df['item_identifier'].apply(str)
print(df['item_identifier'].head())

df['item_identifier'] = df['item_identifier'].str.rstrip('.0')
print(df['item_identifier'].head())

df['item_identifier'] = df['item_identifier'].str.zfill(3)

print(df['item_identifier'].head())


# In[10]:


print(df['title'].head())
df['title'] = df['title'].str.strip()
print(df['title'].head())


# ## Putting it all together
# 
# Now let's make a script that cleans up our spreadsheet and creates a new cleaned up CSV.
# 
# ```{admonition} New function   
# [`df.to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html): Writes the DataFrame to a CSV file.
# ```

# In[11]:


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

print(df.head())
print(df.shape)

df.to_csv('sampleData_cleaned.csv', index=False)


# Beautiful! You should have a lovely new spreadsheet called `'sampleData_cleaned.csv'` with 88 rows and 9 columns. ✨
