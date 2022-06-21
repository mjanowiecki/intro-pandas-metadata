#!/usr/bin/env python
# coding: utf-8

# (basics-df)=
# # 1. Basics of `Series` and `DataFrames`
# 
# ## pandas documentation
# 
# First, I want to give you a quick tour of the [pandas documentation website](https://pandas.pydata.org/pandas-docs/stable/index.html). This documentation is essential to using pandas and I refer back to it literally all the time.
# 
# [pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html): The User Guide covers all of pandas by topic area. Each of the subsections introduces a topic (such as “working with missing data”), and discusses how pandas approaches the problem, with many examples throughout.
# 
# [pandas API reference](https://pandas.pydata.org/pandas-docs/stable/reference/index.html): This page gives an overview of all public pandas objects, functions and methods.
# 
# ## What is a `DataFrame`?
# 
# There are two main concepts that are essential to using pandas.
# 
# The first important concept is a `DataFrame`. In pandas, a `DataFrame` is a table of data organized and accessed by **rows** and **columns**. In many ways, it is equivalent to a basic spreadsheet or CSV file. Here's a visual of what our sampleData.csv looks like as a `DataFrame`.
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download sampleData.csv here<./sampleData.csv>`.
# ```
# 
# ```{image} img/dataframe.jpg
# :alt: Visual of DataFrame
# :width: 2000px
# :align: left
# ```
# 
# **Indexes:**
# By default, pandas assigns an `index` to every row and every column in a `DataFrame`.
# 
# The `index` (position) is an integer that starts at 0 and counts up.
# 
# - 50 rows → row index from 0 to 49
# 
# - 10 columns → column index from 0 to 9
# ```{hint}
# When `index` is used generically, it refers to the row index rather than the column index.
# ```
# For rows, the `index` is typically identical to the row label, but sometimes people change the `index` or row labels to be strings or letters.
# 
# - 10 rows → row index from A to J
# 
# **Labels:**
# 
# - Column labels correspond to the name of each column. They are typically a string, but can be numbers too.
# - Most of the time, column labels of a `DataFrame` are equivalent to the "column headers" (or first row) seen in most spreadsheet editors.
# - For 3rd column in our `DataFrame`, the column index is `2` while the column label is "creator".
# 
# ## What is a `Series`?
# 
# The second important concept is a `Series`. In pandas, a `Series` is equivalent to a column in a CSV or spreadsheet. `DataFrames` are composed of 2 or more `Series`.
# 
# `Series` also have a row index or label. Here is an example of a `Series` (or column) named "title" from sampleData.csv.
# 
# ```{image} img/series.png
# :alt: Visual of DataFrame
# :width: 1000px
# :align: left
# ```

# In[ ]:





# ## Make a `DataFrame`
# 
# To use pandas, we need to import the library. Typically, pandas is abbreviated as `pd`. 

# In[1]:


import pandas as pd


# Now, let's use the pandas function `read_csv()` to read sampleData.csv into a `DataFrame`. 
# 
# ```{admonition} New function    
# [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html): Reads a CSV file into a DataFrame.
# ```
# 
# Let's give our resulting `DataFrame` the commonly used variable name `df`, although we could call it whatever we want. Let's also print `df` to see what it looks like in the terminal.

# In[2]:


filename = 'sampleData.csv'
df = pd.read_csv(filename)
print(df)


# While this doesn't print out every row or column of df, it helps us see the overall structure of the `DataFrame`. pandas also has many useful functions to help get a closer look at your data. Let's try some!
# 
# ```{admonition} New function
# [`pd.read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html): Converts a JSON string to a DataFrame or Series.
# ```
# ```{admonition} New function
# [`pd.read_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html): Reads an Excel file into a DataFrame.
# ```
# ```{admonition} New function
# [`pd.read_sql()`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html): Reads SQL database table into a DataFrame.
# ```
# ```{admonition} New function
# [`pd.from_dict()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html): Creates a  DataFrame from dictionary or an array of dictionaries.
# ```
# 
# ## View your `DataFrame`
# 
# Sometimes it's nice to get an overview of your data without having to scroll through a bunch of rows. `head()` and `tail()` are really great for this. 
# 
# Use `head()` on your `DataFrame` to see the first 5 rows with column labels, and use `tail()` to see the last 5 rows with column labels. You can change the number of rows by putting a different value in the parentheses.
# 
# ```{admonition} New function
# [`df.head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html): Returns the first n rows of the DataFrame.
# ```
# ```{admonition} New function
# [`df.tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html): Returns the last n rows of the DataFrame.
# ```

# In[3]:


print(df.head())


# In[4]:


print(df.tail(12))


# Pandas also offers many properties to understand your `DataFrame`. Let's try them out. 
# 
# ```{admonition} New property
# [`df.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html): Returns the column labels of the DataFrame.
# ```
# ```{admonition} New property
# [`df.shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html): Returns a tuple (rows, columns) representing the DataFrame.
# ```
# ```{admonition} New property
# [`df.empty`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html): Indicates if the DataFrame is empty.
# ```

# In[5]:


print(df.columns)
print(df.shape)
print(df.empty)


# When we printed `df.columns`, we got a list of 10 column labels.
# 
# When we printed `df.shape`, we got the result `(90, 10)`. This means our `DataFrame` has 90 rows and 10 columns.
# 
# When we printed `df.empty`, we got the result `False`. This means our `DataFrame` is NOT empty.
# 
# ## Access a row
# 
# There are two main way to access a row. The first is by using `.loc[]`, which grabs a row by its **label**. 
# 
# Typically, the index label is the same as the row integer (but not always, remember you can change the index labels to be anything you want). The default row index starts at 0, and counts up by 1. Let's access the 11th row.
# 
# ```{admonition} New function
# [`df.loc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html): Access a group of rows and columns by label(s) or a boolean array.
# ```

# In[6]:


row_11 = df.loc[10]
print(row_11)


# The second way to access a row is by using `.iloc[]`, which grabs a row by its **integer**. 
# 
# The row integer will remain the same regardless of your index labels. Rows integers always start at 0, and count up by 1. Let's access the 11th row.
# 
# ```{admonition} New function
# [`df.iloc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html): Purely integer-location based indexing for selection by position.
# ```   

# In[7]:


row_11 = df.iloc[10]
print(row_11)


# You can also grab sections of rows using both of these functions. Guess what rows each function will bring up.<br>
# 
# ```{hint}
# These work a lot like list indexing!
# ```

# In[8]:


print(df.iloc[30:41])


# In[9]:


print(df.iloc[[0, 30, 60]])


# ❓ **What's up with the extra brackets in `df.iloc[[0, 30, 60]]`** ❓
# 
# To make sure that the function is taking your list of rows as a list --not as 3 distinct parameters-- you've got to put your values in a list bracket. The example below gives the same result, and hopefully helps to show how we get double brackets when putting a list in `.iloc[]`.

# In[10]:


rowsToGrab = [0, 30, 60]
print(df.iloc[rowsToGrab])


# ## Access a Series
# 
# There are two main ways to access a specific column (also known as a `Series`) by its label in a `DataFrame`. 
# 
# 1. Dot notation
#    - Uses the column label as a property of the `DataFrame`.
#    - Example: `df.column_name`
# 2. Bracket notation
#    - Places column label string in brackets to select part of the `DataFrame`.
#    - Example: `df['column_name']`
# 
# Let's try both options.

# In[11]:


degree_discipline = df.degree_discipline
print(degree_discipline)


# In[12]:


degree_discipline = df['degree_discipline']
print(degree_discipline)


# In most cases, both notations work equally well! Sometimes though, dot notation will fail. If that happens, just switch to bracket notation. 
# 
# ## Access a specific cell
# 
# There are also a bunch of ways to look at a specific cell -- here's some!
# 
# We can add a column label (2nd parameter value) to `.loc[]` to grab a cell value by its index label and column name.

# In[13]:


print(df.loc[9, 'degree_discipline'])


# We can also add a column integer (second parameter value) to `.iloc[]` to grab a cell value by its row integer position and its column integer position. 
# 
# ```{hint}
# To figure out the integer of your column, start counting at 0 at the leftmost column.
# ```

# In[14]:


print(df.iloc[9, 5])


# We can also use `iat[]` and `at[]` to view a single cell.
# 
# ```{admonition} New function
# [`df.iat[]`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iat.html): Access single value by index.
# ```
# ```{admonition} New function
# [`df.at[]`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html): Access single value by label.
# ``` 

# In[15]:


print(df.at[9, 'degree_discipline'])
print(df.iat[9,5])


# ## Get descriptive stats
# 
# There are also many functions in pandas to get computational or descriptive stats about your Series or DataFrames. Here's a quick look at my two favorites (check out the full lists for [Series](https://pandas.pydata.org/docs/reference/series.html#computations-descriptive-stats) and [DataFrames](https://pandas.pydata.org/docs/reference/frame.html#computations-descriptive-stats) here).
# 
# 
# ```{admonition} New function
# [`df[].unique()`](https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.Series.unique.html): Returns unique values of Series.
# ```
# ```{admonition} New function
# [`df[].value_counts()`](https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.Series.value_counts.html): Returns Series containing counts of unique value in column.      
# ```

# In[16]:


department_unique = df['degree_department'].unique()
print(department_unique)

unique_list = list(department_unique)
print(unique_list)


# In[17]:


department_counts = df['degree_department'].value_counts()
print(department_counts)


# In[ ]:




