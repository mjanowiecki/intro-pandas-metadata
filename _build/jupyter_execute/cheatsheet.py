#!/usr/bin/env python
# coding: utf-8

# # Cheatsheet
# 
# ```{admonition} Files
# :class: important
# You can {Download}`download cheatsheet as a pdf here<./cheatsheet.pdf>`.
# ```
# 
# ## Resources
# [pandas API reference](https://pandas.pydata.org/docs/reference/index.html) 
# 
# [pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
# 
# ## Read and evaluate
# 
# [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html): Reads a CSV file into a DataFrame.
# 
# [`df.head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html): Returns the first n rows of the DataFrame.
# 
# [`df.tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html): Returns the last n rows of the DataFrame.
# 
# [`df.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html): Returns the column labels of the DataFrame.
# 
# [`df.shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html): Returns a tuple (rows, columns) of the DataFrame.
# 
# [`df.empty`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html): Indicates if the DataFrame is empty.
# 
# [`df['title'].unique()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html): Returns unique values of Series.
# 
# [`df['title'].value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html): Returns Series containing counts of unique value in column (example ’title’).
# 
# ## Access rows, columns, and cells
# 
# [`df['title']`](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)or [`df.title`](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html): Select single column with specific name (example ‘title’).
# 
# [`df.loc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html): Access rows & columns by label(s) or a boolean array.
# 
# [`df.iloc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html): Purely integer-location based indexing for selection by position.
# 
# [`df.iat[1, 2]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html?highlight=iat): Access single value by index.
# 
# [`df.at[4, 'A']`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html?highlight=): Access single value by label.
# 
# 
# ## Clean up
# 
# [`pd.isna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html): Detects missing values.
# 
# [`pd.notna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html): Detects non-missing values.
# 
# [`df.dropna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html): Removes missing values from the DataFrame.
# 
# [`df.duplicated()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html): Returns boolean Series of duplicate rows.
# 
# [`df.drop_duplicates()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html): Removes duplicate rows from DataFrame.
# 
# [`Series.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html): Invoke function on values of Series.
# 
# [`Series.str.rstrip()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rstrip.html): Removes trailing characters.
# 
# [`Series.str.zfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html): Pads Series with zeros.
# 
# [`Series.str.strip()`](https://pandas.pydata.org/docs/reference/index.html): Strips whitespaces from Series.
# 
# ## Loop through rows
# 
# [`df.iterrows()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html): Loops through DataFrame rows as (index, Series) pairs.
# 
# ## Merge DataFrames
# 
# [`pd.merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html) : Merge DataFrame or named Series objects with a database-style join.
# 
# `how=“left”` : Merges on all ids from left DataFrame. Ids not in left DataFrame will not be included.
# 
# `how=“right”` : Merges on all ids from right DataFrame. Ids not in right DataFrame will not be included.
# 
# `how=”outer”` : Merges on all ids from both DataFrames.
# 
# `how=“inner”` : Merges only on ids found in both DataFrames. Ids found in only one DataFrame will not be included.
# 
# ## Reshaping
# 
# [`df.explode()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html): Transforms each element of a list-like to a row, replicating index values.
# 
# [`df.pivot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html): Reshape data (produce a “pivot” table) based on column values.
# 
# [`df.pivot_table()`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html): Create a spreadsheet-style pivot table as a DataFrame.
# 
# [`lambda`](https://docs.python.org/3/tutorial/controlflow.html): An anonymous (unnamed) function that applies arguments to various parameters and returns an expression (outcome).
# 
# [`df.melt()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html): Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.
# 
# ## Sort DataFrame
# 
# [`df.sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html): Sort by the values along either axis.
# 
# ## Create new CSV
# 
# [`df.to_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html): Writes the DataFrame to a CSV file

# In[ ]:




